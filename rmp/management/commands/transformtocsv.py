"""Transform model data and write to csv file."""
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
    Transform model data and write to csv file.
    """
    help = "Transform model data and write to csv file."

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str)

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
            self.transform()

    def transform(self):
        """
        Transform model data and write to csv file.
        """
        self.stdout.write(
            "  Writing %s.csv..." % self.model_name, ending=""
        )
        try:
            self.model.transform_to_csv()
        except NotImplementedError as e:
            self.stdout.write(
                self.style.ERROR('\n  %s' % e)
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("Done.")
            )
