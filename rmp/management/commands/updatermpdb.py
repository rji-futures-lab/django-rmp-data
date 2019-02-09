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
        self.stdout.write('  Flushing current data from tables... ', ending='')
        management.call_command(
            'flush', verbosity=options['verbosity'], interactive=False
        )
        self.stdout.write(
            self.style.SUCCESS('OK')
        )
        # handle raw files
        raw_files = [
            f for f in listdir(settings.RMP_RAW_DATA_DIR)
            if isfile(join(settings.RMP_RAW_DATA_DIR, f))
        ]
        load_header = self.style.MIGRATE_HEADING(
            '%s .csv files to load:' % len(raw_files)
        )
        self.stdout.write(load_header)
        for f in sorted(raw_files):
            management.call_command('loadsourcefile', f)
        self.stdout.write(
            self.style.SUCCESS('Done.')
        )

        # handle transformations
        processed_models = [
            m for m in get_models('processed').values()
        ]
        load_header = self.style.MIGRATE_HEADING(
            'Writing transformed %s .csv files:' % len(processed_models)
        )
        for m in processed_models:
            self.stdout.write(
                "  Writing %s.csv... " % m._meta.object_name, ending=""
            )
            try:
                m.transform_to_csv()
            except NotImplementedError:
                msg = '   Add get_transformations() to {0}'.format(
                    m._meta.object_name
                )
                self.stdout.write(
                    self.style.ERROR(msg)
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS("Done.")
                )

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
