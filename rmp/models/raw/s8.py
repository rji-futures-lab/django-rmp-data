"""
tblS8_Prevention_Program_Chemicals.csv
tblS8PreventionProgram2.csv
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


class Tbls8PreventionProgramChemicals(BaseRMPModel):
    primarykey = CopyFromIntegerField(primary_key=True)  # Field name made lowercase.
    preventionprogram2id = CopyFromForeignKey(
        'Tbls8PreventionProgram2',
        on_delete=models.PROTECT
    )  # Field name made lowercase.
    processchemicalid = CopyFromForeignKey(
        'Tbls1Processchemicals',
        on_delete=models.PROTECT
    )  # Field name made lowercase.

    source_file = 'tblS8_Prevention_Program_Chemicals'

    class Meta:
        db_table = 'tblS8_Prevention_Program_Chemicals'


class Tbls8PreventionProgram2(BaseRMPModel):
    preventionprogram2id = CopyFromIntegerField(primary_key=True)
    process_naics_id = CopyFromForeignKey(
        'Tbls1ProcessNaics',
        on_delete=models.PROTECT,
    )
    safetyreviewdate = CopyFromDateTimeField(blank=True)
    fr_nfpa58 = CopyFromBooleanField()
    fr_osha = CopyFromBooleanField()
    fr_astm = CopyFromBooleanField()
    fr_ansi = CopyFromBooleanField()
    fr_asme = CopyFromBooleanField()
    fr_none = CopyFromBooleanField()
    fr_othertype = CopyFromCharField(max_length=200, blank=True)
    fr_comments = CopyFromCharField(max_length=200, blank=True)
    hazardreviewdate = CopyFromDateTimeField(blank=True)
    changecompletiondate = CopyFromDateTimeField(blank=True)
    mh_toxicrelease = CopyFromBooleanField()
    mh_fire = CopyFromBooleanField()
    mh_explosion = CopyFromBooleanField()
    mh_runawayreaction = CopyFromBooleanField()
    mh_polymerization = CopyFromBooleanField()
    mh_overpressurization = CopyFromBooleanField()
    mh_corrosion = CopyFromBooleanField()
    mh_overfilling = CopyFromBooleanField()
    mh_contamination = CopyFromBooleanField()
    mh_equipmentfailure = CopyFromBooleanField()
    mh_coolingloss = CopyFromBooleanField()
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
    pc_automaticshutoffs = CopyFromBooleanField()
    pc_interlocks = CopyFromBooleanField()
    pc_alarms = CopyFromBooleanField()
    pc_keyedbypass = CopyFromBooleanField()
    pc_emergencyairsupply = CopyFromBooleanField()
    pc_emergencypower = CopyFromBooleanField()
    pc_backuppump = CopyFromBooleanField()
    pc_groundingequipment = CopyFromBooleanField()
    pc_inhibitoraddition = CopyFromBooleanField()
    pc_rupturedisks = CopyFromBooleanField()
    pc_excessflowdevice = CopyFromBooleanField()
    pc_quenchsystem = CopyFromBooleanField()
    pc_purgesystem = CopyFromBooleanField()
    pc_none = CopyFromBooleanField()
    pc_othertype = CopyFromCharField(max_length=200, blank=True)
    ms_sprinklersystem = CopyFromBooleanField()
    ms_dikes = CopyFromBooleanField()
    ms_firewalls = CopyFromBooleanField()
    ms_blastwalls = CopyFromBooleanField()
    ms_delugesystem = CopyFromBooleanField()
    ms_watercurtain = CopyFromBooleanField()
    ms_enclosure = CopyFromBooleanField()
    ms_neutralization = CopyFromBooleanField()
    ms_none = CopyFromBooleanField()
    ms_othertype = CopyFromCharField(max_length=200, blank=True)
    md_processareadetectors = CopyFromBooleanField()
    md_perimetermonitors = CopyFromBooleanField()
    md_none = CopyFromBooleanField()
    md_othertype = CopyFromCharField(max_length=200, blank=True)
    ch_chemicalreduction = CopyFromBooleanField()
    ch_chemicalincrease = CopyFromBooleanField()
    ch_changeprocessparameters = CopyFromBooleanField()
    ch_installprocesscontrols = CopyFromBooleanField()
    ch_installprocessdetection = CopyFromBooleanField()
    ch_installperimetermonitoring = CopyFromBooleanField()
    ch_installmitigationsystems = CopyFromBooleanField()
    ch_nonerequired = CopyFromBooleanField()
    ch_none = CopyFromBooleanField()
    ch_otherchanges = CopyFromCharField(max_length=200, blank=True)
    opproceduresreviewdate = CopyFromDateTimeField(blank=True)
    trainingreviewdate = CopyFromDateTimeField(blank=True)
    tr_classroom = CopyFromBooleanField()
    tr_onthejob = CopyFromBooleanField()
    tr_othertype = CopyFromCharField(max_length=200, blank=True)
    ct_writtentest = CopyFromBooleanField()
    ct_oraltest = CopyFromBooleanField()
    ct_demonstration = CopyFromBooleanField()
    ct_observation = CopyFromBooleanField()
    ct_othertype = CopyFromCharField(max_length=200, blank=True)
    maintenancereviewdate = CopyFromDateTimeField(blank=True)
    equipmentinspectiondate = CopyFromDateTimeField(blank=True)
    equipmenttested = CopyFromCharField(max_length=200, blank=True)
    complianceauditdate = CopyFromDateTimeField(blank=True)
    auditcompletiondate = CopyFromDateTimeField(blank=True)
    incidentinvestigationdate = CopyFromDateTimeField(blank=True)
    investigationchangedate = CopyFromDateTimeField(blank=True)
    mostrecentchangedate = CopyFromDateTimeField(blank=True)
    cbi_flag = CopyFromBooleanField()
    description = CopyFromTextField(blank=True) # TODO to rmp_prev2text with preventionprogramID

    source_file = 'tblS8PreventionProgram2'

    class Meta:
        db_table = 'tblS8PreventionProgram2'
