"""
tblS7_Prevention_Program_Chemicals.csv
tblS7PreventionProgram3.csv
"""

from django.db import models
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDecimalField,
    CopyFromIntegerField,
    CopyFromForeignKey,
)
from .base import BaseRMPModel

class Tbls7PreventionProgramChemicals(BaseRMPModel):
    primarykey = models.CopyFromIntegerField(primary_key=True)  # Field name made lowercase.
    preventionprogram3id = models.CopyFromForeignKey(

    )  # Field name made lowercase.
    processchemicalid = models.CopyFromForeignKey(
        tbls1ProcessChemicals,
        on_delete=models.PROTECT,
    )  # Field name made lowercase.

    source_file = 'tblS7_Prevention_Program_Chemicals'

    class Meta:
        db_table = 'tblS7_Prevention_Program_Chemicals'

class Tbls7PreventionProgram3(BaseRMPModel):
    preventionprogram3id = models.CopyFromIntegerField(primary_key=True)
    procnaics_id = models.CopyFromForeignKey(
        Tbls1ProcessNaics,
        on_delete=models.CASCADE
    )
    safety_info_date = models.CopyFromDateTime()
    last_pha_date = models.CopyFromDateTime()
    pha_whatif = models.CopyFromBooleanField()
    pha_checklist = models.CopyFromBooleanField()
    pha_whatifcheck = models.CopyFromBooleanField()
    pha_hazop = models.CopyFromBooleanField()
    pha_fmea = models.CopyFromBooleanField()
    pha_fta = models.CopyFromBooleanField()
    pha_other = models.CopyFromCharField(max_length=200, blank=True)
    change_comp_date = models.CopyFromDateTime()
    mh_toxicrelease = models.CopyFromBooleanField()
    mh_fire = models.CopyFromBooleanField()
    mh_explosion = models.CopyFromBooleanField()
    mh_runawayreact = models.CopyFromBooleanField()
    mh_polymerization = models.CopyFromBooleanField()
    mh_overpressure = models.CopyFromBooleanField()
    mh_corrosion = models.CopyFromBooleanField()
    mh_overfilling = models.CopyFromBooleanField()
    mh_contamination = models.CopyFromBooleanField()
    mh_equipfailure = models.CopyFromBooleanField()
    mh_cooling_loss = models.CopyFromBooleanField()
    mh_earthquake = models.CopyFromBooleanField()
    mh_floods = models.CopyFromBooleanField()
    mh_tornado = models.CopyFromBooleanField()
    mh_hurricanes = models.CopyFromBooleanField()
    mh_othertype = models.CopyFromCharField(max_length=200, blank=True)
    pc_vents = models.CopyFromBooleanField()
    pc_reliefvalves = models.CopyFromBooleanField()
    pc_checkvalves = models.CopyFromBooleanField()
    pc_scrubbers = models.CopyFromBooleanField()
    pc_flares = models.CopyFromBooleanField()
    pc_manualshutoffs = models.CopyFromBooleanField()
    pc_autoshutoffs = models.CopyFromBooleanField()
    pc_interlocks = models.CopyFromBooleanField()
    pc_alarms = models.CopyFromBooleanField()
    pc_keyedbypass = models.CopyFromBooleanField()
    pc_emergencyair = models.CopyFromBooleanField()
    pc_emergencypower = models.CopyFromBooleanField()
    pc_backuppump = models.CopyFromBooleanField()
    pc_groundingequip = models.CopyFromBooleanField()
    pc_inhibitoradd = models.CopyFromBooleanField()
    pc_rupturedisks = models.CopyFromBooleanField()
    pc_excessflowdev = models.CopyFromBooleanField()
    pc_quenchsystem = models.CopyFromBooleanField()
    pc_purgesystem = models.CopyFromBooleanField()
    pc_none = models.CopyFromBooleanField()
    pc_other = models.CopyFromCharField(max_length=200, blank=True)
    mx_sprinklersys = models.CopyFromBooleanField()
    ms_dikes = models.CopyFromBooleanField()
    ms_firewalls = models.CopyFromBooleanField()
    ms_blastwalls = models.CopyFromBooleanField()
    ms_delugesystem = models.CopyFromBooleanField()
    ms_watercurtain = models.CopyFromBooleanField()
    ms_enclosure = models.CopyFromBooleanField()
    ms_neutralization = models.CopyFromBooleanField()
    ms_none = models.CopyFromBooleanField()
    ms_other = models.CopyFromCharField(max_length=200, blank=True)
    md_processare = models.CopyFromBooleanField()
    md_perimetermon = models.CopyFromBooleanField()
    md_none = models.CopyFromBooleanField()
    md_other = models.CopyFromCharField(max_length=200, blank=True)
    ch_reduceinv = models.CopyFromBooleanField()
    ch_increaseinv = models.CopyFromBooleanField()
    ch_changeparam = models.CopyFromBooleanField()
    ch_proccontrol = models.CopyFromBooleanField()
    ch_procdetect = models.CopyFromBooleanField()
    ch_perimetermon = models.CopyFromBooleanField()
    ch_mitigationsys = models.CopyFromBooleanField()
    ch_nonerequired = models.CopyFromBooleanField()
    ch_none = models.CopyFromBooleanField()
    ch_other = models.CopyFromCharField(max_length=200, blank=True)
    proc_review_date = models.CopyFromDateTime()
    train_review_date = models.CopyFromDateTime()
    tr_classroom = models.CopyFromBooleanField()
    tr_onthejob = models.CopyFromBooleanField()
    tr_other = models.CopyFromCharField(max_length=200, blank=True)
    ct_writtentest = models.CopyFromBooleanField()
    ct_oraltest  = models.CopyFromBooleanField()
    ct_demonstration = models.CopyFromBooleanField()
    ct_observation = models.CopyFromBooleanField()
    ct_other = models.CopyFromCharField(max_length=200, blank=True)
    maint_review_date = models.CopyFromDateTime()
    maint_inspect_date = models.CopyFromDateTime()
    equip_tested = models.CopyFromCharField(max_length=200, blank=True)
    change_manage_date = models.CopyFromDateTime()
    change_review_date = models.CopyFromDateTime()
    prestart_rev_date = models.CopyFromDateTime()
    comp_audit_date = models.CopyFromDateTime()
    audit_comp_date = models.CopyFromDateTime()
    inc_invest_date = models.CopyFromDateTime()
    inc_change_date = models.CopyFromDateTime()
    part_review_date = models.CopyFromDateTime()
    hotwork_rev_date = models.CopyFromDateTime()
    con_safety_date = models.CopyFromDateTime()
    con_eval_date = models.CopyFromDateTime()
    cbi_flag = models.CopyFromBooleanField()
    description = models.CopyFromTextField() # TODO to rmp_prev3text with prevention programID

    source_file = 'tblS7PreventionProgram3'

    class Meta:
        db_table = 'tblS7PreventionProgram3'
