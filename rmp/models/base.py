"""
Customized Django model subclasses
"""
import os
from django.conf import settings
from django.core.files.storage import get_storage_class
from django.db import models
from django.db.models import F
from rmp.managers import BaseRMPManager
from rmp.utils import camelcase_to_underscore


class BaseRMPModel(models.Model):
    """
    Base, abstract class for RMP data models.
    """
    @classmethod
    def get_blank_field_names(cls):
        """
        Return a list of char fields on the model.
        """
        return [
            getattr(f, 'copy_from_name', f.name)
            for f in cls._meta.concrete_fields if f.blank
        ]

    @classmethod
    def get_copyable_fields(cls):
        """
        Return a list of fields that are concrete and not auto_created.
        """
        return [
            f for f in cls._meta.concrete_fields if not f.auto_created
        ]

    @classmethod
    def get_null_field_names(cls):
        """
        Return a list of fields that allow NULL values.
        """
        return [
            getattr(f, 'copy_from_name', f.name)
            for f in cls._meta.concrete_fields
            if f.null
        ]

    @classmethod
    def get_renamed_fields(cls):
        """
        Return dict w renamed fields to old field names (as F() exps).
        """
        return {
            camelcase_to_underscore(f.name): F(f.name) 
            for f in cls.get_copyable_fields()
        }

    @classmethod
    def get_source_column_mapping(cls):
        """
        Returns a dict mapping model field names to csv column names.
        """
        mapping = {}

        for f in cls._meta.concrete_fields:
            mapping[f.name] = getattr(
                f, 'copy_from_name', f.name
            )

        return mapping

    @classmethod
    def get_transform_queryset(cls):
        """
        Should be implemented on RMP model subclasses.
        """
        model_name = cls._meta.object_name
        msg = '%s does not have get_transform_queryset() defined' % model_name
    
        raise NotImplementedError(msg)

    @classmethod
    def transform_to_csv(cls):
        """
        Export transformed data to a csv file.
        """
        fields = [
            getattr(f, 'copy_from_name', f.name) 
            for f in cls.get_copyable_fields()
        ]
        file_name = '%s.csv' % cls._meta.object_name

        storage = get_storage_class()()
        file_path = os.path.join(
            settings.RMP_DATA_LOCATION, 'processed', file_name
        )

        with storage.open(file_path, mode='wb') as f:
            # not providing headers here...duh
            result = cls.get_transform_queryset().to_csv(f, *fields)

        return result

    @classmethod
    def get_prefixed_boolean_fields(cls, prefix):

        fields = [
            f for f in cls._meta.get_fields()
            if f.name[0:len(prefix)] == prefix and (
                f.name not in [
                    prefix + 'other_type', 
                    prefix + 'other',
                ]
            )
        ]

        return fields

    objects = BaseRMPManager()

    class Meta:
        abstract = True  
