"""Update the RMP database."""
from os.path import isfile, join
from django.conf import settings
from django.core import management
from django.core.files.storage import get_storage_class
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
        raw_files_path = join(settings.RMP_DATA_LOCATION, 'raw')
        self.load_from_storage(raw_files_path)

        # handle transformations
        processed_models = [
            m for m in get_models('processed').values()
            if m._meta.object_name != 'StateCounts'
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
        processed_files_path = join(settings.RMP_DATA_LOCATION, 'processed')
        self.load_from_storage(processed_files_path)

        management.call_command('transformtocsv', 'StateCounts')
        management.call_command('loadfromcsv', 'StateCounts', flush=True)

    def load_from_storage(self, path):
        """
        Iterate over files in path.
        """
        files = self.storage.listdir(path)[1]
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

    @property
    def storage(self):
        self._storage = getattr(
            self, '_storage', get_storage_class()()
        )
        return self._storage
