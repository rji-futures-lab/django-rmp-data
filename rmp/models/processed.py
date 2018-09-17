"""
Models for processed RMP data.
"""
from django.db import models


class AccChem(models.Model):
    accchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    accident_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    quantity_lbs = models.DecimalField(max_digits=65535, decimal_places=65535)
    percent_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    num_acc_flam = models.DecimalField(max_digits=65535, decimal_places=65535)
    cas = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_type = models.BooleanField()

    class Meta:
        db_table = 'rmp_acc_chem'


class AccFlam(models.Model):
    flammixchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    accchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        db_table = 'rmp_acc_flam'


class ChemCd(models.Model):
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_name = models.CharField(max_length=-1)
    cas2 = models.CharField(max_length=-1, blank=True, null=True)
    threshold = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_type = models.BooleanField(blank=True, null=True)
    cbi_flag = models.BooleanField()
    chemical_owner = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        db_table = 'rmp_chem_cd'


class DeregCd(models.Model):
    dereg = models.DecimalField(max_digits=65535, decimal_places=65535)
    dereg_tr = models.CharField(max_length=-1)

    class Meta:
        db_table = 'rmp_dereg_cd'


class DochanCd(models.Model):
    dochan = models.CharField(max_length=-1)
    dochan_tr = models.CharField(max_length=-1)

    class Meta:
        db_table = 'rmp_dochan_cd'


class DoctypCd(models.Model):
    doctyp = models.CharField(max_length=-1)
    doctyp_tr = models.CharField(max_length=-1)

    class Meta:
        db_table = 'rmp_doctyp_cd'


class EventsCd(models.Model):
    events = models.CharField(max_length=-1)
    events_tr = models.CharField(max_length=-1)

    class Meta:
        db_table = 'rmp_events_cd'


class ExecSumLen(models.Model):
    rmp_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    byte_count = models.DecimalField(max_digits=65535, decimal_places=65535)
    suspect_count = models.DecimalField(max_digits=65535, decimal_places=65535)
    line_count = models.DecimalField(max_digits=65535, decimal_places=65535)
    edited_yn = models.BooleanField()

    class Meta:
        db_table = 'rmp_exec_sum_len'


class LldescCd(models.Model):
    lldesc = models.CharField(max_length=-1)
    lldesc_tr = models.CharField(max_length=-1)

    class Meta:
        db_table = 'rmp_lldesc_cd'


class LlmethCd(models.Model):
    primary_key = models.DecimalField(max_digits=65535, decimal_places=65535)
    llmeth = models.CharField(max_length=-1)
    llmeth_tr = models.CharField(max_length=-1)

    class Meta:
        db_table = 'rmp_llmeth_cd'


class PhysCd(models.Model):
    phys = models.CharField(max_length=-1)
    phys_tr = models.CharField(max_length=-1)

    class Meta:
        db_table = 'rmp_phys_cd'


class Prevent2Chem(models.Model):
    primary_key = models.DecimalField(max_digits=65535, decimal_places=65535)
    prevent_2_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    procchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        db_table = 'rmp_prevent_2_chem'


class Prevent3Chem(models.Model):
    primary_key = models.DecimalField(max_digits=65535, decimal_places=65535)
    prevent_3_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    procchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        db_table = 'rmp_prevent_3_chem'


class ProcChem(models.Model):
    procchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    process_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    quantity_lbs = models.DecimalField(max_digits=65535, decimal_places=65535)
    cbi_flag = models.BooleanField()
    num_alt_flam = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_alt_tox = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_prevent_2_chem = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_prevent_3_chem = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_proc_flam = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_worst_flam = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_worst_tox = models.DecimalField(max_digits=65535, decimal_places=65535)
    cas = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_type = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'rmp_proc_chem'


class ProcFlam(models.Model):
    flammixchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    procchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        db_table = 'rmp_proc_flam'


class ProcNaics(models.Model):
    procnaics_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    process_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    naics = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_prevent_2 = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_prevent_3 = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        db_table = 'rmp_proc_naics'


class RejectCd(models.Model):
    reject = models.CharField(max_length=-1)
    reject_tr = models.CharField(max_length=-1)

    class Meta:
        db_table = 'rmp_reject_cd'


class ScenCd(models.Model):
    scen = models.CharField(max_length=-1)
    scen_tr = models.CharField(max_length=-1)

    class Meta:
        db_table = 'rmp_scen_cd'


class SubmitCd(models.Model):
    submit = models.CharField(max_length=-1)
    submit_tr = models.CharField(max_length=-1)

    class Meta:
        db_table = 'rmp_submit_cd'


class TopoCd(models.Model):
    topo = models.CharField(max_length=-1)
    topo_tr = models.CharField(max_length=-1)

    class Meta:
        db_table = 'rmp_topo_cd'


class WindCd(models.Model):
    wind = models.CharField(max_length=-1)
    wind_tr = models.CharField(max_length=-1)

    class Meta:
        db_table = 'rmp_wind_cd'
