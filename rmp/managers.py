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
    def copy_from_source_file(self, processed=False):
        """
        Copy contents of a source file into model.

        By default, copy from a .csv file in RMP_RAW_DATA_DIR.

        If True is passed to processed, copy from a .tsv file in
        RMP_PROCESSED_DATA_DIR.
        """
        model = self.model

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

        source_file = getattr(
            model, 'source_file', model._meta.object_name
        )

        if processed:
            source_file = getattr(
                model, 'source_file', model._meta.db_table
            )
            filename = '%s.tsv' % source_file
            path = os.path.join(settings.RMP_PROCESSED_DATA_DIR, filename)
            options['delimiter'] = '\t'
            options['null'] = "NULL"
            options['quote_character'] = '\b' # <- This is a hack:
            # https://stackoverflow.com/questions/20402696/is-it-possible-to-turn-off-quote-processing-in-the-postgres-copy-command-with-cs
            # since postgres assumes " is the quote character, and the data isn't actually
            # quoted, but there are quote chars in the data, and those quote chars
            # are not properly escaped, we are lying and saying the quotes are escaped by 
            # the backspace character.
            # proper way to solve this is to output processed files where the quote
            # chars are properly escaped, the default escape char is "
        else:
            source_file = getattr(
                model, 'source_file', model._meta.object_name
            )
            filename = '%s.csv' % source_file
            path = os.path.join(settings.RMP_RAW_DATA_DIR, filename)
        
        return super().from_csv(path, **options)
