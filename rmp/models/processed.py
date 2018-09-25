"""
Models for processed RMP data.
"""
from django.db import models


class AccChem(models.Model):
    accchem_id = models.IntegerField(
        primary_key=True,
        verbose_name='Accident Chemical Record ID',
        help_text='A unique ID for each accident chemical record.',
    )
    # TODO: ForeignKeyField candidate
    accident_id = models.IntegerField(
        help_text='The unique ID for each accident record',
    )
    # TODO: ForeignKeyField candidate
    chemical_id = models.IntegerField(
        help_text='The identifying ID for a particular chemical released in an '
                  'accident.',
    )
    quantity_lbs = models.IntegerField(
        verbose_name='Amount Released (lbs)',
        help_text='The amount of the substance released in the accident, in '
                  'pounds, to two significant digits.',
    )
    # TODO: db_fields.tsv says this should be a float field, will decimal work?
    percent_weight = models.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=5,
        verbose_name='Percent Weight (Within Mixture)',
        help_text='The percent weight of a chemical within a mixture released '
                  'in an accident.',
    )
    num_acc_flam = models.IntegerField(
        null=True,
        verbose_name='Number of Flammable Components',
        help_text='The number of listed flammable component chemicals for this'
                  ' chemical record.',
    )
    cas = models.CharField(
        max_length=9,
        verbose_name='CAS number',
        help_text='The identifying CAS number for a chemical.',
    )
    CHEMICAL_TYPE_CHOICES = (
        ('T', 'toxic'),
        ('F', 'flammable'),
    )
    chemical_type = models.CharField(
        max_length=1,
        choices=CHEMICAL_TYPE_CHOICES,
        help_text='"The type of chemical.',
    )

    class Meta:
        db_table = 'rmp_acc_chem'


# TODO: does this table have a primary key, or is it a linking table?
# if the latter, how might we make the model more in line with Django's
# conventions?
class AccFlam(models.Model):
    # TODO: ForeignKeyField candidate
    flammixchem_id = models.IntegerField(
        verbose_name='Flammable Chemical ID',
        help_text='A unique ID for each flammable chemical record.',
    )
    # TODO: ForeignKeyField candidate
    accchem_id = models.IntegerField(
        verbose_name='Accident Chemical Record ID',
        help_text='A unique ID for each accident chemical record.'
    )
    # TODO: ForeignKeyField candidate
    chemical_id = models.IntegerField(
        verbose_name='Chemical ID',
        help_text='The identifying ID for a particular flammable chemical released in an accident.',
    )

    class Meta:
        db_table = 'rmp_acc_flam'


# TODO: this table is not defined in db_field.tsv
class ChemCd(models.Model):
    chemical_id = models.IntegerField(
        primary_key=True,
    )
    chemical_name = models.CharField(
        max_length=92,
    )
    cas2 = models.CharField(
        max_length=10,
        blank=True,
    )
    threshold = models.IntegerField()
    chemical_type = models.CharField(
        max_length=1,
        blank=True,
    )
    cbi_flag = models.BooleanField()
    chemical_owner = models.CharField(
        max_length=3,
        blank=True,
    )

    class Meta:
        db_table = 'rmp_chem_cd'


class DeregCd(models.Model):
    dereg = models.IntegerField(
        primary_key=True,
    )
    dereg_tr = models.CharField(
        max_length=62,
    )

    class Meta:
        db_table = 'rmp_dereg_cd'


class DochanCd(models.Model):
    dochan = models.CharField(max_length=1)
    dochan_tr = models.CharField(max_length=1)

    class Meta:
        db_table = 'rmp_dochan_cd'

# JG: Models below here need a look
# ==================================


class DoctypCd(models.Model):
    doctyp = models.CharField(max_length=1)
    doctyp_tr = models.CharField(max_length=30)

    class Meta:
        db_table = 'rmp_doctyp_cd'


class EventsCd(models.Model):
    events = models.CharField(max_length=1)
    events_tr = models.CharField(max_length=40)

    class Meta:
        db_table = 'rmp_events_cd'


class ExecSumLen(models.Model):
    rmp_id = models.IntegerField(
        primary_key=True,
    )
    byte_count = models.IntegerField(

    )
    suspect_count = models.IntegerField(

    )
    line_count = models.IntegerField(

    )
    edited_yn = models.CharField(max_length=1)

    class Meta:
        db_table = 'rmp_exec_sum_len'


class LldescCd(models.Model):
    lldesc = models.CharField(max_length=2)
    lldesc_tr = models.CharField(max_length=36)

    class Meta:
        db_table = 'rmp_lldesc_cd'


class LlmethCd(models.Model):
    primary_key = models.IntegerField(primary_key=True)
    llmeth = models.CharField(max_length=2)
    llmeth_tr = models.CharField(max_length=83)

    class Meta:
        db_table = 'rmp_llmeth_cd'


class PhysCd(models.Model):
    phys = models.CharField(max_length=1)
    phys_tr = models.CharField(max_length=30)

    class Meta:
        db_table = 'rmp_phys_cd'


class Prevent2Chem(models.Model):
    primary_key = models.IntegerField(primary_key=True)

    # TODO foreign key ?
    prevent_2_id = models.IntegerField()

    # TODO foreign key ?
    procchem_id = models.IntegerField()

    class Meta:
        db_table = 'rmp_prevent_2_chem'


class Prevent3Chem(models.Model):
    primary_key = models.IntegerField(primary_key=True)

    #TODO Foreign key ?
    prevent_3_id = models.IntegerField()

    # TODO Foreign key ?
    procchem_id = models.IntegerField()

    class Meta:
        db_table = 'rmp_prevent_3_chem'

class ProcChem(models.Model):
    procchem_id = models.IntegerField(primary_key=True)

    #TODO Foreign Key?
    process_id = models.IntegerField()
    chemical_id = models.IntegerField()
    quantity_lbs = models.IntegerField()

    cbi_flag = models.BooleanField()
    num_alt_flam = models.IntegerField()
    num_alt_tox = models.IntegerField()
    num_prevent_2_chem = models.IntegerField()
    num_prevent_3_chem = models.IntegerField()
    num_proc_flam = models.IntegerField()
    num_worst_flam = models.IntegerField()
    num_worst_tox =models.IntegerField()
    cas = models.IntegerField()
    chemical_type = models.CharField(max_length=1)

    class Meta:
        db_table = 'rmp_proc_chem'


class ProcFlam(models.Model):
    flammixchem_id = models.IntegerField(primary_key=True)

    #TODO Foreign key?
    procchem_id = models.IntegerField()
    chemical_id = models.IntegerField()

    class Meta:
        db_table = 'rmp_proc_flam'


class ProcNaics(models.Model):
    procnaics_id = models.IntegerField(primary_key=True)

    #TODO Foreign key?
    process_id = models.IntegerField()
    naics = models.IntegerField()
    num_prevent_2 = models.IntegerField()
    num_prevent_3 = models.IntegerField()

    class Meta:
        db_table = 'rmp_proc_naics'


class RejectCd(models.Model):
    reject = models.CharField(max_length=1)
    reject_tr = models.CharField(max_length=59)

    class Meta:
        db_table = 'rmp_reject_cd'


class ScenCd(models.Model):
    scen = models.CharField(max_length=1)
    scen_tr = models.CharField(max_length=27)

    class Meta:
        db_table = 'rmp_scen_cd'


class SubmitCd(models.Model):
    submit = models.CharField(max_length=3)
    submit_tr = models.CharField(max_length=101)

    class Meta:
        db_table = 'rmp_submit_cd'


class TopoCd(models.Model):
    topo = models.CharField(max_length=1)
    topo_tr = models.CharField(max_length=5)

    class Meta:
        db_table = 'rmp_topo_cd'


class WindCd(models.Model):
    wind = models.CharField(max_length=1)
    wind_tr = models.CharField(max_length=13)

    class Meta:
        db_table = 'rmp_wind_cd'
