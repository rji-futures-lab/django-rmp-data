"""
Models for processed RMP data.
"""
from django.db import models


class RmpAccChem(models.Model):
    accchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    accident_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    quantity_lbs = models.DecimalField(max_digits=65535, decimal_places=65535)
    percent_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    num_acc_flam = models.DecimalField(max_digits=65535, decimal_places=65535)
    cas = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_type = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'rmp_acc_chem'


class RmpAccFlam(models.Model):
    flammixchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    accchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'rmp_acc_flam'


class RmpChemCd(models.Model):
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_name = models.CharField(max_length=-1)
    cas2 = models.CharField(max_length=-1, blank=True, null=True)
    threshold = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_type = models.BooleanField(blank=True, null=True)
    cbi_flag = models.BooleanField()
    chemical_owner = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rmp_chem_cd'


class RmpDeregCd(models.Model):
    dereg = models.DecimalField(max_digits=65535, decimal_places=65535)
    dereg_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_dereg_cd'


class RmpDochanCd(models.Model):
    dochan = models.CharField(max_length=-1)
    dochan_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_dochan_cd'


class RmpDoctypCd(models.Model):
    doctyp = models.CharField(max_length=-1)
    doctyp_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_doctyp_cd'


class RmpEventsCd(models.Model):
    events = models.CharField(max_length=-1)
    events_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_events_cd'


class RmpExecSumLen(models.Model):
    rmp_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    byte_count = models.DecimalField(max_digits=65535, decimal_places=65535)
    suspect_count = models.DecimalField(max_digits=65535, decimal_places=65535)
    line_count = models.DecimalField(max_digits=65535, decimal_places=65535)
    edited_yn = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'rmp_exec_sum_len'


class RmpLldescCd(models.Model):
    lldesc = models.CharField(max_length=-1)
    lldesc_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_lldesc_cd'


class RmpLlmethCd(models.Model):
    primary_key = models.DecimalField(max_digits=65535, decimal_places=65535)
    llmeth = models.CharField(max_length=-1)
    llmeth_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_llmeth_cd'


class RmpPhysCd(models.Model):
    phys = models.CharField(max_length=-1)
    phys_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_phys_cd'


class RmpPrevent2Chem(models.Model):
    primary_key = models.DecimalField(max_digits=65535, decimal_places=65535)
    prevent_2_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    procchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'rmp_prevent_2_chem'


class RmpPrevent3Chem(models.Model):
    primary_key = models.DecimalField(max_digits=65535, decimal_places=65535)
    prevent_3_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    procchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'rmp_prevent_3_chem'


class RmpProcChem(models.Model):
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
        managed = False
        db_table = 'rmp_proc_chem'


class RmpProcFlam(models.Model):
    flammixchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    procchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'rmp_proc_flam'


class RmpProcNaics(models.Model):
    procnaics_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    process_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    naics = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_prevent_2 = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_prevent_3 = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'rmp_proc_naics'


class RmpRejectCd(models.Model):
    reject = models.CharField(max_length=-1)
    reject_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_reject_cd'


class RmpScenCd(models.Model):
    scen = models.CharField(max_length=-1)
    scen_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_scen_cd'


class RmpSubmitCd(models.Model):
    submit = models.CharField(max_length=-1)
    submit_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_submit_cd'


class RmpTopoCd(models.Model):
    topo = models.CharField(max_length=-1)
    topo_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_topo_cd'


class RmpWindCd(models.Model):
    wind = models.CharField(max_length=-1)
    wind_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_wind_cd'
