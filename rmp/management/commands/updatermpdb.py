"""Update the RMP database."""
from os import listdir
from os.path import isfile, join
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DataError
from rmp.models.helpers import get_model_by_source_file
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Update the RMP database."""
    help = "Update the RMP database."

    def handle(self, *args, **options):
        """
        Handle the command.
        """
        raw_files = [
            f for f in listdir(settings.RMP_RAW_DATA_DIR)
            if isfile(join(settings.RMP_RAW_DATA_DIR, f))
        ]

        self.stdout.write('  Flushing current data from tables... ', ending='')
        management.call_command('flush', verbosity=options['verbosity'], interactive=False)
        self.stdout.write(
            self.style.SUCCESS('OK')
        )
        
        load_header = self.style.MIGRATE_HEADING(
            'Loading %s .csv files:' % len(raw_files)
        )
        self.stdout.write(load_header)
        for f in raw_files:
            management.call_command('loadsourcefile', f)

        self.stdout.write(self.style.SUCCESS('Done.'))
