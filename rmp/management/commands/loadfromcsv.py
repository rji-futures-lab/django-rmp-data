"""Load RMP model from a csv file."""
import os
from django.apps import apps
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand, CommandError
from django.db.models.deletion import ProtectedError
from django.db.utils import DataError, IntegrityError
from rmp.models.helpers import get_model_by_source_file
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Load RMP model from a csv file.
    """
    help = "Load RMP model from a csv file."

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str)
        parser.add_argument(
            '-f',
            '--flush',
            action='store_true',
            dest='flush',
            help='Flush current data first',
        )

    def handle(self, *args, **options):
        """
        Handle the command.
        """
        self.model_name = options['model_name']

        try:
            self.model = apps.get_model('rmp', self.model_name)
        except LookupError:
            error_msg = "  %s is not a defined model." % self.model_name
            self.stdout.write(
                self.style.ERROR(error_msg)
            )
        else:
            if options['flush']:
                self.flush()
            self.load()   
    
    def flush(self):
        """
        Delete all model instances.
        """
        self.stdout.write("  Flushing %s..." % self.model_name, ending="")
        try:
            delete_count = self.model.objects.all().delete()
        except ProtectedError:
            msg = "%s currently has instances referenced \
through a protected foreign key." % self.model_name
            self.stdout.write(
                self.style.ERROR('\n  %s' % msg)
            )
        else:
            print(delete_count)

    def load(self):
        """
        Load model from csv file.
        """
        self.stdout.write("  Loading %s..." % self.model_name, ending="")
        try:
            insert_count = self.model.objects.copy_from_csv()
        except (AttributeError, DataError, IntegrityError, ValueError) as e:
            self.stdout.write(
                self.style.ERROR('\n  %s' % e)
            )
        else:
            count_w_commas = "{:,}".format(insert_count)
            self.stdout.write(
                self.style.SUCCESS("%s records inserted" % count_w_commas)
            )
