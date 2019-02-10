"""Update the RMP database."""
from os import listdir
from os.path import isfile, join
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DataError
from rmp.models.helpers import get_models
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Update the RMP database."""
    help = "Update the RMP database."

    def handle(self, *args, **options):
        """
        Handle the command.
        """
        self.stdout.write('  Flushing current data from tables...', ending='')
        management.call_command(
            'flush', verbosity=options['verbosity'], interactive=False
        )
        self.stdout.write(
            self.style.SUCCESS('OK')
        )
        # handle raw files
        self.stdout.write(
            self.style.MIGRATE_HEADING('Loading raw files. '), ending=""
        )
        self.load_from_dir(settings.RMP_RAW_DATA_DIR)

        # handle transformations
        processed_models = [
            m for m in get_models('processed').values()
        ]
        transform_header = self.style.MIGRATE_HEADING(
            'Writing %s transformed .csv files:' % len(processed_models)
        )
        self.stdout.write(transform_header)
        for m in processed_models:
            management.call_command('transformtocsv', m._meta.object_name)
        self.stdout.write(
            self.style.SUCCESS('Done.')
        )

        # handle processed files
        self.stdout.write(
            self.style.MIGRATE_HEADING('Loading processed files. '), ending=""
        )
        self.load_from_dir(settings.RMP_PROCESSED_DATA_DIR)

    def load_from_dir(self, path):
        """
        """
        files = [ f for f in listdir(path) if isfile(join(path, f)) ]
        file_count_header = self.style.MIGRATE_HEADING(
            '%s files to load:' % len(files)
        )
        self.stdout.write(file_count_header)
        for f in sorted(files):
            model_name = f.split('.')[0]
            management.call_command('loadfromcsv', model_name)
        self.stdout.write(
            self.style.SUCCESS('Done.')
        )
