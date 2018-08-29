This is a dump of RTK NET's copy of the RMP database,
which was obtained from U.S. EPA via FOIA and
last updated by EPA on 4/30/2018.  It has been modified
by RTK NET to add certain data fields and to replace
high-ASCII characters with low-ASCII ones.

1. The database tables can be created through rmp2018_schema.sql
if you are using a relational database.  If not, this file will
still define the table, data field, and index structure.

2. Data tables have been dumped into tab-delimited ASCII in
files ending in .tsv.

3. The top-level relational data table is rmp_facility.  Joins
to other tables are documented in the file db_joins.tsv, a
tab-delimited file with one line per database join.  The fields
in this file are self-explanatory, except:

join_type: 
m = zero to many
o = zero or one
i = one to many
s or x = one to one
orphans_yn: equals y if there are detail table records with no master record
master_count_field: data field in master table with number of detail records
master_max_count: maximum number of detail records per master record

4. Documentation on data fields is given in the file db_fields.tsv,
a tab-delimited file with one line per database field.  Fields in this file
are:

table_name: database table name
field_name: database field name
var_name: data field name as presented to users on RTK NET
field_type: data field type, for example varchar(25)
field_display: yn = Yes/No field.  If the contents of this field begin
with "code", it specifies that the data field is a code and can be interpreted
through a code table.  If a code specification contains "long", the code table
is a database table, and will have its own .fil file.  If it contains "short", 
then the codes and translations will be listed within the db_codes.fil file.
var_desc: a short description of the data field
blank_pct: a calculated percentage showing how often the field is blank

The file db_codes.tsv contains "short" codes and translations as described
above.

5. The file dump.txt contains the output of the SQL program used to dump
the data, which provides a record count of each data table as a check.

6. Additional information about the database can be found in RTK NET's
"About the Data" and "Data Dictionary" pages.
