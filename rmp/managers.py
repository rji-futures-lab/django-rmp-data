"""
Customized Django model manager subclasses.
"""
import os
from django.conf import settings
from postgres_copy import CopyManager


class BaseRMPManager(CopyManager):
    """
    Base manager for RMP data models.
    """
    def copy_from_raw_csv(self):
        """
        Copy contents of a raw .csv file into model.
        """
        model = self.model

        source_file = getattr(
            model, 'source_file', model._meta.db_table
        )
        filename = '%s.csv' % source_file
        path = os.path.join(settings.RMP_RAW_DATA_DIR, filename)

        options = dict(mapping=model.get_source_column_mapping())

        blank_fields = model.get_blank_field_names()
        null_fields = model.get_null_field_names()

        if len(blank_fields) > 0:
            options['force_not_null'] = blank_fields

        if len(null_fields):
            options['force_null'] = null_fields

        return super().from_csv(path, **options)
