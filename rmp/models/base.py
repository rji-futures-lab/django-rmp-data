"""
Customized Django model subclasses
"""
from django.db import models
from rmp.managers import BaseRMPManager


class BaseRMPModel(models.Model):
    """
    Base, abstract class for RMP data models.
    """
    @classmethod
    def get_concrete_fields(cls):
        """
        Return a list of fields that are declared on the model.
        """
        return [f for f in cls._meta.get_fields() if f.concrete]

    @classmethod
    def get_blank_field_names(cls):
        """
        Return a list of char field on model.
        """
        return [
            getattr(f, 'copy_from_name', f.name)
            for f in cls.get_concrete_fields()
            if f.blank
        ]

    @classmethod
    def get_null_field_names(cls):
        """
        Return a list of fields that allow NULL values.
        """
        return [
            getattr(f, 'copy_from_name', f.name)
            for f in cls.get_concrete_fields()
            if f.null
        ]

    @classmethod
    def get_source_column_mapping(cls):
        """
        Returns a dict mapping model field names to csv column names.
        """
        mapping = {}

        for f in cls.get_concrete_fields():
            mapping[f.name] = getattr(
                f, 'copy_from_name', f.name
            )

        return mapping

    objects = BaseRMPManager()

    class Meta:
        abstract = True  
