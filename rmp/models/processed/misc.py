"""
Models for processed RMP data.
"""
import os
from django.conf import settings
from django.db import models
from django.db.models import F, Max, OuterRef, Subquery, Sum, Count, Case, When, Value
from rmp.fields import (
    CopyFromBigIntegerField,
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDateField,
    CopyFromDateTimeField,
    CopyFromDecimalField,
    CopyFromForeignKey,
    CopyFromIntegerField,
    CopyFromOneToOneField,
    CopyFromTextField,
    CopyFromFloatField,
)
from rmp.models import raw as raw_models
from rmp.models import processed as processed_models
from rmp.models.base import BaseRMPModel

class PreventionProgram2(BaseRMPModel): #rmp_prevent_2
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='prevent_2_id',
    )
    procnaics = CopyFromForeignKey(
        'ProcNaics',
        on_delete=models.CASCADE
    )
    safety_info_date = CopyFromCharField(blank=True, max_length=8)
    # safety_info_date = CopyFromDateField(blank=True)
    fr_nfpa58 = CopyFromBooleanField()
    fr_osha = CopyFromBooleanField()
    fr_astm = CopyFromBooleanField()
    fr_ansi = CopyFromBooleanField()
    fr_asme = CopyFromBooleanField()
    fr_none = CopyFromBooleanField()
    fr_other = CopyFromCharField(max_length=200, blank=True)
    fr_comments = CopyFromCharField(max_length=200, blank=True)
    haz_review_date = CopyFromCharField(blank=True, max_length=8)
    # haz_review_date = CopyFromDateField(blank=True)
    change_comp_date = CopyFromCharField(blank=True, max_length=8)
    # change_comp_date = CopyFromDateField(blank=True)
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
    ms_sprinklersys = CopyFromBooleanField()
    ms_dikes = CopyFromBooleanField()
    ms_firewalls = CopyFromBooleanField()
    ms_blastwalls = CopyFromBooleanField()
    ms_delugesystem = CopyFromBooleanField()
    ms_watercurtain = CopyFromBooleanField()
    ms_enclosure = CopyFromBooleanField()
    ms_neutralization = CopyFromBooleanField()
    ms_none = CopyFromBooleanField()
    ms_other = CopyFromCharField(max_length=200, blank=True)
    md_processarea = CopyFromBooleanField()
    md_perimetermon = CopyFromBooleanField()
    md_none = CopyFromBooleanField()
    md_other = CopyFromCharField(max_length=200, blank=True)
    ch_reduceinv = CopyFromBooleanField()
    ch_increaseinv = CopyFromBooleanField()
    ch_changeparam = CopyFromBooleanField()
    ch_proccontrol = CopyFromBooleanField()
    ch_procdetect= CopyFromBooleanField()
    ch_perimetermon = CopyFromBooleanField()
    ch_mitigationsys = CopyFromBooleanField()
    ch_nonerequired = CopyFromBooleanField()
    ch_none = CopyFromBooleanField()
    ch_other = CopyFromCharField(max_length=200, blank=True)
    proc_review_date = CopyFromCharField(blank=True, max_length=8)
    # proc_review_date = CopyFromDateField(blank=True)
    train_review_date = CopyFromCharField(blank=True, max_length=8)
    # train_review_date = CopyFromDateField(blank=True)
    tr_classroom = CopyFromBooleanField()
    tr_onthejob = CopyFromBooleanField()
    tr_other = CopyFromCharField(max_length=200, blank=True)
    ct_writtentest = CopyFromBooleanField()
    ct_oraltest = CopyFromBooleanField()
    ct_demonstration = CopyFromBooleanField()
    ct_observation = CopyFromBooleanField()
    ct_other = CopyFromCharField(max_length=200, blank=True)
    maint_review_date = CopyFromCharField(blank=True, max_length=8)
    # maint_review_date = CopyFromDateField(blank=True)
    maint_inspect_date = CopyFromCharField(blank=True, max_length=8)
    # maint_inspect_date = CopyFromDateField(blank=True)
    equip_tested = CopyFromCharField(max_length=200, blank=True)
    comp_audit_date = CopyFromCharField(blank=True, max_length=8)
    # comp_audit_date = CopyFromDateField(blank=True)
    audit_comp_date = CopyFromCharField(blank=True, max_length=8)
    # audit_comp_date = CopyFromDateField(blank=True)
    inc_invest_date = CopyFromCharField(blank=True, max_length=8)
    # inc_invest_date = CopyFromDateField(blank=True)
    inc_change_date = CopyFromCharField(blank=True, max_length=8)
    # inc_change_date = CopyFromDateField(blank=True)
    most_recent_date = CopyFromCharField(blank=True, max_length=8)
    # most_recent_date = CopyFromDateField(blank=True)
    cbi_flag = CopyFromBooleanField()
    num_prevent_2_chem = CopyFromIntegerField()
    num_prev2text = CopyFromIntegerField()
    num_prev2_text = CopyFromIntegerField()

    source_file = 'rmp_prevent_2'


class PreventionProgram3(BaseRMPModel):
    prevent_id = CopyFromIntegerField(
        primary_key=True,
        source_column='prevent_3_id',
    )
    procnaics = CopyFromForeignKey(
        'ProcNaics',
        on_delete=models.CASCADE
    )
    safety_info_date = CopyFromCharField(blank=True, max_length=8)
    # safety_info_date = CopyFromDateField(null=True)
    last_pha_date = CopyFromCharField(blank=True, max_length=8)
    # last_pha_date = CopyFromDateField(null=True)
    pha_whatif = CopyFromBooleanField()
    pha_checklist = CopyFromBooleanField()
    pha_whatifcheck = CopyFromBooleanField()
    pha_hazop = CopyFromBooleanField()
    pha_fmea = CopyFromBooleanField()
    pha_fta = CopyFromBooleanField()
    pha_other = CopyFromCharField(max_length=200, blank=True)
    change_comp_date = CopyFromCharField(blank=True, max_length=8)
    # change_comp_date = CopyFromDateField(null=True)
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
    ms_sprinklersys = CopyFromBooleanField()
    ms_dikes = CopyFromBooleanField()
    ms_firewalls = CopyFromBooleanField()
    ms_blastwalls = CopyFromBooleanField()
    ms_delugesystem = CopyFromBooleanField()
    ms_watercurtain = CopyFromBooleanField()
    ms_enclosure = CopyFromBooleanField()
    ms_neutralization = CopyFromBooleanField()
    ms_none = CopyFromBooleanField()
    ms_other = CopyFromCharField(max_length=200, blank=True)
    md_processarea = CopyFromBooleanField()
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
    proc_review_date = CopyFromCharField(blank=True, max_length=8)
    # proc_review_date = CopyFromDateField(null=True)
    train_review_date = CopyFromCharField(blank=True, max_length=8)
    # train_review_date = CopyFromDateField(null=True)
    tr_classroom = CopyFromBooleanField()
    tr_onthejob = CopyFromBooleanField()
    tr_other = CopyFromCharField(max_length=200, blank=True)
    ct_writtentest = CopyFromBooleanField()
    ct_oraltest  = CopyFromBooleanField()
    ct_demonstration = CopyFromBooleanField()
    ct_observation = CopyFromBooleanField()
    ct_other = CopyFromCharField(max_length=200, blank=True)
    maint_review_date = CopyFromCharField(blank=True, max_length=8)
    # maint_review_date = CopyFromDateField(null=True)
    maint_inspect_date = CopyFromCharField(blank=True, max_length=8)
    # maint_inspect_date = CopyFromDateField(null=True)
    equip_tested = CopyFromCharField(max_length=200, blank=True)
    change_manage_date = CopyFromCharField(blank=True, max_length=8)
    # change_manage_date = CopyFromDateField(null=True)
    change_review_date = CopyFromCharField(blank=True, max_length=8)
    # change_review_date = CopyFromDateField(null=True)
    prestart_rev_date = CopyFromCharField(blank=True, max_length=8)
    # prestart_rev_date = CopyFromDateField(null=True)
    comp_audit_date = CopyFromCharField(blank=True, max_length=8)
    # comp_audit_date = CopyFromDateField(null=True)
    audit_comp_date = CopyFromCharField(blank=True, max_length=8)
    # audit_comp_date = CopyFromDateField(null=True)
    inc_invest_date = CopyFromCharField(blank=True, max_length=8)
    # inc_invest_date = CopyFromDateField(null=True)
    inc_change_date = CopyFromCharField(blank=True, max_length=8)
    # inc_change_date = CopyFromDateField(null=True)
    part_review_date = CopyFromCharField(blank=True, max_length=8)
    # part_review_date = CopyFromDateField(null=True)
    hotwork_rev_date = CopyFromCharField(blank=True, max_length=8)
    # hotwork_rev_date = CopyFromDateField(null=True)
    con_safety_date = CopyFromCharField(blank=True, max_length=8)
    # con_safety_date = CopyFromDateField(null=True)
    con_eval_date = CopyFromCharField(blank=True, max_length=8)
    # con_eval_date = CopyFromDateField(null=True)
    cbi_flag = CopyFromBooleanField()

    # TODO AGGREGATE

    num_prevent_3_chem = CopyFromIntegerField()
    num_prev3text = CopyFromIntegerField()
    num_prev3_text = CopyFromIntegerField()

    source_file = 'rmp_prevent_3'


class EmergencyResponse(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='rmp_id',
    )
    community_erp_yn = CopyFromBooleanField()
    facility_erp_yn = CopyFromBooleanField()
    erp_specific_yn = CopyFromBooleanField()
    erp_inform_yn = CopyFromBooleanField()
    erp_inform_hth_yn = CopyFromBooleanField()
    # erp_review_date = CopyFromDateTimeField(blank=True)
    # erp_training_date = CopyFromDateTimeField(blank=True)
    erp_review_date = CopyFromCharField(max_length=10, blank=True)
    erp_training_date = CopyFromCharField(max_length=10, blank=True)
    coord_agency= CopyFromCharField(max_length=250, blank=True)
    coord_phone = CopyFromCharField(max_length=10, blank=True)
    subto_osha191038 = CopyFromBooleanField()
    subto_osha191020 = CopyFromBooleanField()
    subto_cwa112 = CopyFromBooleanField()
    subto_rcra264= CopyFromBooleanField()
    subto_opa90 = CopyFromBooleanField()
    subto_state_epcra = CopyFromBooleanField()
    subto_other = CopyFromCharField(max_length=200, blank=True)

    source_file = 'rmp_response'




class ProcNaics(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='procnaics_id',
    )
    process = CopyFromForeignKey(
        'Process',
        on_delete=models.CASCADE
    )
    naics = CopyFromIntegerField()
    num_prevent_2 = CopyFromIntegerField()
    num_prevent_3 = CopyFromIntegerField()

    source_file = 'rmp_proc_naics'


class Prev2Text(BaseRMPModel):
    prevent_2 = CopyFromOneToOneField(
        'PreventionProgram2',
        primary_key=True,
        on_delete=models.CASCADE,
        source_column='prevent_2_id',
    )
    desctext = CopyFromTextField()

    source_file = 'rmp_prev2text'


class Prev3Text(BaseRMPModel):
    prevent_3 = CopyFromOneToOneField(
        'PreventionProgram3',
        primary_key=True,
        on_delete=models.CASCADE,
        source_column='prevent_3_id',
    )
    desctext = CopyFromTextField()

    source_file = 'rmp_prev3text'


class Prevent2Chem(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='primary_key',
    )
    prevent_2 = CopyFromForeignKey(
        'PreventionProgram2',
        on_delete=models.CASCADE,
        source_column='prevent_2_id',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.CASCADE
    )

    source_file = 'rmp_prevent_2_chem'


class Prevent3Chem(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='primary_key',
    )
    prevent_3 = CopyFromForeignKey(
        'PreventionProgram3',
        on_delete=models.CASCADE,
        source_column='prevent_3_id',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.CASCADE
    )

    source_file = 'rmp_prevent_3_chem'
