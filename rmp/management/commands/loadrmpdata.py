"""Load RMP data from source files into models."""
import os
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DataError
from rmp.models import get_models
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Load RMP data from source files into models.
    """
    help = "Load RMP data from source files into models."

    def handle(self, *args, **kwargs):
        """
        Handle the command.
        """
        self.stdout.write('...flushing current data from tables...')
        management.call_command('flush', verbosity=1, interactive=False)
        self.stdout.write(
            self.style.SUCCESS('All data tables flushed.')
        )
        for m in get_models('processed').values():
            if 'ChemCd' in str(m):
                # ^^^ HACK until we have all processed models loading
                # from processed files and raw models loading from raw files
                self.load_model(m)
            else:
                self.load_model(m, processed=True)

    def can_load(self, model):
        """
        Test if model has the method necessary for loading.
        """
        return hasattr(model.objects, 'copy_from_source_file')

    def load_model(self, model, processed=False):
        """
        Load model for it's source file.

        If processed is passed as True, load from the processed file.

        Otherwise, load from the raw file.
        """
        model_name = model._meta.object_name

        if self.can_load(model):
            self.stdout.write("...loading %s" % model_name)
            try:
                insert_count = model.objects.copy_from_source_file(processed)
            except (ValueError, DataError) as e:
                self.stderr.write(
                    self.style.ERROR(e)
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS("%s records inserted" % insert_count)
                )
        else:
            msg = '%s not attached to BaseRMPManager.' % model_name
            self.stderr.write(
                self.style.ERROR(msg)
            )
