import os
from django.conf import settings
from django.db import models
from postgres_copy import CopyManager


class BaseRMPManager(CopyManager):

    def copy_from_raw_csv(self):
        model = self.model

        source_table = getattr(
            model, 'source_file', model._meta.db_table
        )
        filename = '%s.csv' % source_table
        path = os.path.join(settings.RMP_RAW_DATA_DIR, filename)

        options = dict(mapping=model.get_source_column_mapping())

        if model.has_blank_fields:
            options['force_not_null'] = model.get_blank_field_names()

        # if model.has_null_fields:
        #     options['force_null'] = model.get_null_field_names()

        return super().from_csv(path, **options)


class BaseRMPModel(models.Model):

    @classmethod
    def get_blank_field_names(cls):
        """
        Return a list of char field on model.
        """
        return [
            f.copy_from_name for f in cls._meta.get_fields()
            if f.blank
        ]

    @classmethod
    def get_null_field_names(cls):
        """
        Return a list of fields that allow NULL values.
        """
        return [
            f.copy_from_name for f in cls._meta.get_fields()
            if f.null
        ]

    @classmethod
    def has_blank_fields(cls):
        """
        Return True if the model has blankable fields
        """
        return len(cls.get_blank_field_names()) > 0

    @classmethod
    def has_null_fields(cls):
        """
        Return True if the model has nullable fields
        """
        return len(cls.get_null_field_names()) > 0

    @classmethod
    def get_source_column_mapping(cls):
        """
        Returns a dict mapping model field names to csv column names.
        """
        mapping = {}

        for f in cls._meta.get_fields():
            mapping[f.name] = f.source_column or f.name

        return mapping

    objects = BaseRMPManager()

    class Meta:
        abstract = True  


class CopyFromBooleanField(models.fields.BooleanField):
    def __init__(self, *args, **kwargs):
        self.source_column = kwargs.pop('source_column', None)
        super().__init__(*args, **kwargs)

    @property
    def copy_from_name(self):
        return self.source_column or self.name


class CopyFromCharField(models.fields.CharField):
    def __init__(self, *args, **kwargs):
        self.source_column = kwargs.pop('source_column', None)
        super().__init__(*args, **kwargs)

    @property
    def copy_from_name(self):
        return self.source_column or self.name


class CopyFromDecimalField(models.fields.DecimalField):
    def __init__(self, *args, **kwargs):
        self.source_column = kwargs.pop('source_column', None)
        super().__init__(*args, **kwargs)

    @property
    def copy_from_name(self):
        return self.source_column or self.name


class CopyFromIntegerField(models.fields.IntegerField):
    def __init__(self, *args, **kwargs):
        self.source_column = kwargs.pop('source_column', None)
        super().__init__(*args, **kwargs)

    @property
    def copy_from_name(self):
        return self.source_column or self.name
