"""Update the RMP database."""
from os import listdir
from os.path import isfile, join
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DataError
from rmp.transformers import transform_executive_summaries
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Update the RMP database."""
    help = "Update the RMP database."

    def handle(self, *args, **options):
        """
        Handle the command.
        """
        self.stdout.write('  Flushing current data from tables... ', ending='')
        management.call_command('flush', verbosity=options['verbosity'], interactive=False)
        self.stdout.write(
            self.style.SUCCESS('OK')
        )
        # handle raw files
        raw_files = [
            f for f in listdir(settings.RMP_RAW_DATA_DIR)
            if isfile(join(settings.RMP_RAW_DATA_DIR, f))
        ]
        load_header = self.style.MIGRATE_HEADING(
            'Loading %s .csv files:' % len(raw_files)
        )
        self.stdout.write(load_header)
        for f in sorted(raw_files):
            management.call_command('loadsourcefile', f)
        self.stdout.write(self.style.SUCCESS('Done.'))

        transform_executive_summaries()

        # handle processed files
        processed_files = [
            f for f in listdir(settings.RMP_PROCESSED_DATA_DIR)
            if isfile(join(settings.RMP_PROCESSED_DATA_DIR, f))
        ]
        load_header = self.style.MIGRATE_HEADING(
            'Loading %s .tsv files:' % len(raw_files)
        )
        self.stdout.write(load_header)
        for f in sorted(processed_files):
            management.call_command('loadsourcefile', f, processed=True)
        self.stdout.write(self.style.SUCCESS('Done.'))
