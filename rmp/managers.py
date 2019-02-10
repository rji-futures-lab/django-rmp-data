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
    def get_default_transform_queryset(self):
        """
        Return a QuerySet with default transformations for raw models.
        """
        annotations = self.model.get_renamed_fields()

        return super().annotate(**annotations)

    def copy_from_csv(self):
        """
        Copy contents of a csv file into model.
        """
        model = self.model
        stage = model.__module__.split('.')[2]
        file_name = '%s.csv' % model._meta.object_name
        file_path = os.path.join(settings.RMP_DATA_DIR, stage, file_name)

        options = dict(mapping=model.get_source_column_mapping())

        blank_fields = model.get_blank_field_names()
        null_fields = model.get_null_field_names()

        # HACK to deal with raw file lacking primary key
        if model._meta.object_name in ['tblRMPError', 'tblExecutiveSummaries']:
            # remove it from the source column mappings and blank fields
            options['mapping'].pop('id')
            blank_fields.remove('id')

        if len(blank_fields) > 0:
            options['force_not_null'] = blank_fields

        if len(null_fields):
            options['force_null'] = null_fields
        
        return super().from_csv(file_path, **options)
