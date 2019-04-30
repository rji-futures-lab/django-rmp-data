"""
After running this command, please run the following command from your terminal
mv *.csv ~/Desktop/django-rmp-data/data/rmp/raw
"""

import os, sys, subprocess
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    """
    Opens .mdb file, and turns all of the tables into .csv files
    """
    def add_arguments(self, parser):
        parser.add_argument('database', type=str)

    def handle(self, *args, **kwargs):
        # DATABASE = options['database']
        DATABASE = kwargs['database']
        databasePath = os.path.join(settings.RMP_DATA_LOCATION, DATABASE)

        # Get the list of table names with "mdb-tables"
        table_names = subprocess.Popen(["mdb-tables", "-1", databasePath],
                                       stdout=subprocess.PIPE,
                                       encoding='utf8').communicate()[0]
        tables = table_names.split('\n')

        # Dump each table as a CSV file using "mdb-export",
        # converting " " in table names to "_" for the CSV filenames.
        for table in tables:
            if table != '':
                filename = table.replace(" ","_") + ".csv"
                completeFileName = os.path.join(
                    settings.RMP_DATA_LOCATION, 'raw', filename
                )
                file = open(completeFileName, 'w')
                print("Dumping " + table)
                contents = subprocess.Popen(["mdb-export", databasePath, table],
                                            stdout=subprocess.PIPE,
                                            encoding='utf8').communicate()[0]
                file.write(contents)
                file.close()
