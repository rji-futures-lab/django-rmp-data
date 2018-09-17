"""This script turns all of the tables in an mdb file into csv files. It will take a bit to run completely
Note: Must install mdbtools (brew install mdbtools on MacOS) and this file must be in the same directory as the mdb file."""

import sys, subprocess, os

DATABASE = sys.argv[1]

# Get the list of table names with "mdb-tables"
table_names = subprocess.Popen(["mdb-tables", "-1", DATABASE],
                               stdout=subprocess.PIPE,
                               encoding='utf8').communicate()[0]
tables = table_names.split('\n')

# Dump each table as a CSV file using "mdb-export",
# converting " " in table names to "_" for the CSV filenames.
for table in tables:
    if table != '':
        filename = table.replace(" ","_") + ".csv"
        file = open(filename, 'w')
        print("Dumping " + table)
        contents = subprocess.Popen(["mdb-export", DATABASE, table],
                                    stdout=subprocess.PIPE,
                                    encoding='utf8').communicate()[0]
        file.write(contents)
        file.close()
