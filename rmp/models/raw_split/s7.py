"""
tblS7_Prevention_Program_Chemicals.csv
tblS7PreventionProgram3.csv
"""
from django.db import models
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDateTimeField,
    CopyFromDecimalField,
    CopyFromForeignKey,
    CopyFromIntegerField,
    CopyFromTextField,
)
from rmp.models.base import BaseRMPModel


class Tbls7PreventionProgramChemicals(BaseRMPModel):
    primarykey = CopyFromIntegerField(primary_key=True)  # Field name made lowercase.
    preventionprogram3id = CopyFromForeignKey(
        'Tbls7PreventionProgram3',
        on_delete=models.PROTECT,
    )  # Field name made lowercase.
    processchemicalid = CopyFromForeignKey(
        'tbls1ProcessChemicals',
        on_delete=models.PROTECT,
    )  # Field name made lowercase.

    source_file = 'tblS7_Prevention_Program_Chemicals'

    class Meta:
        db_table = 'tblS7_Prevention_Program_Chemicals'


class Tbls7PreventionProgram3(BaseRMPModel):
    preventionprogram3id = CopyFromIntegerField(primary_key=True)
    procnaics_id = CopyFromForeignKey(
        'Tbls1ProcessNaics',
        on_delete=models.CASCADE
    )
    safety_info_date = CopyFromDateTimeField()
    last_pha_date = CopyFromDateTimeField()
    pha_whatif = CopyFromBooleanField()
    pha_checklist = CopyFromBooleanField()
    pha_whatifcheck = CopyFromBooleanField()
    pha_hazop = CopyFromBooleanField()
    pha_fmea = CopyFromBooleanField()
    pha_fta = CopyFromBooleanField()
    pha_other = CopyFromCharField(max_length=200, blank=True)
    change_comp_date = CopyFromDateTimeField()
    mh_toxicrelease = CopyFromBooleanField()
    mh_fire = CopyFromBooleanField()
    mh_explosion = CopyFromBooleanField()
    mh_runawayreact = CopyFromBooleanField()
    mh_polymerization = CopyFromBooleanField()
    mh_overpressure = CopyFromBooleanField()
    mh_corrosion = CopyFromBooleanField()
    mh_overfilling = CopyFromBooleanField()
    mh_contamination = CopyFromBooleanField()
    mh_equipfailure = CopyFromBooleanField()
    mh_cooling_loss = CopyFromBooleanField()
    mh_earthquake = CopyFromBooleanField()
    mh_floods = CopyFromBooleanField()
    mh_tornado = CopyFromBooleanField()
    mh_hurricanes = CopyFromBooleanField()
    mh_othertype = CopyFromCharField(max_length=200, blank=True)
    pc_vents = CopyFromBooleanField()
    pc_reliefvalves = CopyFromBooleanField()
    pc_checkvalves = CopyFromBooleanField()
    pc_scrubbers = CopyFromBooleanField()
    pc_flares = CopyFromBooleanField()
    pc_manualshutoffs = CopyFromBooleanField()
    pc_autoshutoffs = CopyFromBooleanField()
    pc_interlocks = CopyFromBooleanField()
    pc_alarms = CopyFromBooleanField()
    pc_keyedbypass = CopyFromBooleanField()
    pc_emergencyair = CopyFromBooleanField()
    pc_emergencypower = CopyFromBooleanField()
    pc_backuppump = CopyFromBooleanField()
    pc_groundingequip = CopyFromBooleanField()
    pc_inhibitoradd = CopyFromBooleanField()
    pc_rupturedisks = CopyFromBooleanField()
    pc_excessflowdev = CopyFromBooleanField()
    pc_quenchsystem = CopyFromBooleanField()
    pc_purgesystem = CopyFromBooleanField()
    pc_none = CopyFromBooleanField()
    pc_other = CopyFromCharField(max_length=200, blank=True)
    mx_sprinklersys = CopyFromBooleanField()
    ms_dikes = CopyFromBooleanField()
    ms_firewalls = CopyFromBooleanField()
    ms_blastwalls = CopyFromBooleanField()
    ms_delugesystem = CopyFromBooleanField()
    ms_watercurtain = CopyFromBooleanField()
    ms_enclosure = CopyFromBooleanField()
    ms_neutralization = CopyFromBooleanField()
    ms_none = CopyFromBooleanField()
    ms_other = CopyFromCharField(max_length=200, blank=True)
    md_processare = CopyFromBooleanField()
    md_perimetermon = CopyFromBooleanField()
    md_none = CopyFromBooleanField()
    md_other = CopyFromCharField(max_length=200, blank=True)
    ch_reduceinv = CopyFromBooleanField()
    ch_increaseinv = CopyFromBooleanField()
    ch_changeparam = CopyFromBooleanField()
    ch_proccontrol = CopyFromBooleanField()
    ch_procdetect = CopyFromBooleanField()
    ch_perimetermon = CopyFromBooleanField()
    ch_mitigationsys = CopyFromBooleanField()
    ch_nonerequired = CopyFromBooleanField()
    ch_none = CopyFromBooleanField()
    ch_other = CopyFromCharField(max_length=200, blank=True)
    proc_review_date = CopyFromDateTimeField()
    train_review_date = CopyFromDateTimeField()
    tr_classroom = CopyFromBooleanField()
    tr_onthejob = CopyFromBooleanField()
    tr_other = CopyFromCharField(max_length=200, blank=True)
    ct_writtentest = CopyFromBooleanField()
    ct_oraltest  = CopyFromBooleanField()
    ct_demonstration = CopyFromBooleanField()
    ct_observation = CopyFromBooleanField()
    ct_other = CopyFromCharField(max_length=200, blank=True)
    maint_review_date = CopyFromDateTimeField()
    maint_inspect_date = CopyFromDateTimeField()
    equip_tested = CopyFromCharField(max_length=200, blank=True)
    change_manage_date = CopyFromDateTimeField()
    change_review_date = CopyFromDateTimeField()
    prestart_rev_date = CopyFromDateTimeField()
    comp_audit_date = CopyFromDateTimeField()
    audit_comp_date = CopyFromDateTimeField()
    inc_invest_date = CopyFromDateTimeField()
    inc_change_date = CopyFromDateTimeField()
    part_review_date = CopyFromDateTimeField()
    hotwork_rev_date = CopyFromDateTimeField()
    con_safety_date = CopyFromDateTimeField()
    con_eval_date = CopyFromDateTimeField()
    cbi_flag = CopyFromBooleanField()
    description = CopyFromTextField() # TODO to rmp_prev3text with prevention programID

    source_file = 'tblS7PreventionProgram3'

    class Meta:
        db_table = 'tblS7PreventionProgram3'
