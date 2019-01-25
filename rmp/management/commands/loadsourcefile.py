"""Load raw RMP data from source files into models."""
import os
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DataError
from rmp.models.helpers import get_model_by_source_file
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Load raw RMP data from source files into models.
    """
    help = "Load raw RMP data from source files into models."

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
        )
        parser.add_argument(
            '-f',
            '--flush',
            action='store_true',
            dest='flush',
            help='Flush current data first',
        )
        parser.add_argument(
            '-p',
            '--processed',
            action='store_true',
            dest='processed',
            help='Load processed files',
        )

    def handle(self, *args, **options):
        """
        Handle the command.
        """
        self.file_name = options['file_name']
        self.processed = options['processed']
        self.file_name_no_ext = self.file_name.split('.')[0]
        
        if self.processed:
            self.file_path = os.path.join(
                    settings.RMP_PROCESSED_DATA_DIR, self.file_name
                )
            self.model = get_model_by_source_file(
                self.file_name_no_ext, processed=True
            )
        else:
            self.file_path = os.path.join(
                settings.RMP_RAW_DATA_DIR, self.file_name
            )
            self.model = get_model_by_source_file(self.file_name_no_ext)

        if self.model:
            self.load()
        else:
            error_msg = "  {} is not mapped to a RMP data model.".format(
                options['file_name']
            )
            self.stdout.write(
                self.style.ERROR(error_msg)
            )

    def load(self):
        """
        Load model for it's source file.

        If processed is passed as True, load from the processed file.

        Otherwise, load from the raw file.
        """
        model_name = self.model._meta.object_name

        self.stdout.write("  Loading %s... " % model_name, ending="")
        # self.stdout.flush()
        try:
            insert_count = self.model.objects.copy_from_source_file(
                processed=self.processed
            )
        except (AttributeError, ValueError, DataError) as e:
            self.stdout.write(
                self.style.ERROR('  %s' % e)
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("%s records inserted" % insert_count)
            )
