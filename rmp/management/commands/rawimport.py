import os
from django.conf import settings
from django.core.management.base import BaseCommand
from rmp.models import (
    AccChem,
    AccFlam,
    Tbls6AccidentChemicals,
)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.load_model(AccChem)
        self.load_model(AccFlam)
        self.load_model(Tbls6AccidentChemicals)

    def load_model(self, model):
        """
        Load the model.
        """
        print('Loading %s' % model._meta.object_name)

        model.objects.all().delete()

        copy_options = dict()

        if model._meta.object_name == 'Tbls6AccidentChemicals':
            in_file_name = '%s.csv' % model._meta.db_table
            in_file_path = os.path.join(
                settings.RMP_DATA_DIR, 'raw', in_file_name
            )
        else:
            in_file_name = '%s.tsv' % model._meta.db_table
            in_file_path = os.path.join(
                settings.RMP_DATA_DIR, 'processed', in_file_name
            )
            copy_options['delimiter'] = '\t'
            copy_options['null'] = "NULL"

        print(in_file_path)

        nullable_fields = self.get_null_fields(model)
        blankable_fields = self.get_blank_fields(model)

        if len(nullable_fields) > 0:
            copy_options['force_null'] = nullable_fields

        if len(blankable_fields) > 0:
            copy_options['force_not_null'] = blankable_fields

        insert_count = model.objects.from_csv(
            in_file_path, **copy_options
        )
        print("%s records inserted" % insert_count)

        return insert_count

    def get_blank_fields(self, model):
        """
        Return a list of char field on model.
        """
        return [f.name for f in model._meta.get_fields() if f.blank]

    def get_null_fields(self, model):
        """
        Return a list of fields that allow NULL values.
        """
        return [f.name for f in model._meta.get_fields() if f.null]
