import os
from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # iterate over all the models in the rmp app
        for m in apps.get_app_config('rmp').models.values():
            # get a list of char field that can't be null, 

            if self.can_import(m):
                # flush the table
                m.objects.all().delete()
                in_file_name = '%s.tsv' % m._meta.db_table 
                in_file_path = os.path.join(settings.RMP_DATA_DIR, in_file_name)
                insert_count = m.objects.from_csv(
                    in_file_path, 
                    delimiter='\t',
                    force_not_null=self.get_char_fields(m)
                )
                print("%s records inserted" % insert_count)
            else:
                msg = '%s not attached to CopyManager.' % m._meta.object_name
                print(msg)

    def can_import(self, model):
        """
        Test if a model is importable.
        """
        return hasattr(model.objects, 'from_csv')

    def get_char_fields(self, model):
        """
        Return a list of char field on model.
        """
        return [f.name for f in model._meta.get_fields() if not f.null]
