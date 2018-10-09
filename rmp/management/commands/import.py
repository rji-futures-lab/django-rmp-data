import os
from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # iterate over all the models in the rmp app
        for m in apps.get_app_config('rmp').models.values():

            model_name = m._meta.object_name

            if self.can_import(m):
                print("...loading %s" % model_name)
                # flush the table
                m.objects.all().delete()
                # copy from csv file
                insert_count = m.objects.copy_from_raw_csv()
                print("%s records inserted" % insert_count)
            else:
                msg = '%s not attached to BaseRMPManager.' % model_name
                print(msg)

    def can_import(self, model):
        """
        Test if a model is importable.
        """
        return hasattr(model.objects, 'copy_from_raw_csv')
