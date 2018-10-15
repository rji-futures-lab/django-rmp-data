"""
tblS8_Prevention_Program_Chemicals.csv
tblS8PreventionProgram2.csv
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

class Tbls8PreventionProgramChemicals(BaseRMPModel):
    primarykey = models.CopyFromIntegerField(primary_key=True)  # Field name made lowercase.
    preventionprogram2id = models.CopyFromForeignKey(
        Tbls8PreventionProgram2,
        on_delete=models.PROTECT
    )  # Field name made lowercase.
    processchemicalid = models.CopyFromForeignKey(
        Tbls1Processchemicals,
        on_delete=models.PROTECT
    )  # Field name made lowercase.

    source_file = 'tblS8_Prevention_Program_Chemicals'

    class Meta:
        db_table = 'tblS8_Prevention_Program_Chemicals'

class Tbls8PreventionProgram2(BaseRMPModel):
    preventionprogram2id = models.CopyFromIntegerField(primary_key=True)
    process_naics_id = models.CopyFromForeignKey(
        tblS1Process_NAICS,
        on_delete=models.PROTECT,
    )
    safetyreviewdate = models.CopyFromDateTime(blank=True)
    fr_nfpa58 = models.CopyFromBooleanField()
    fr_osha = models.CopyFromBooleanField()
    fr_astm = models.CopyFromBooleanField()
    fr_ansi = models.CopyFromBooleanField()
    fr_asme = models.CopyFromBooleanField()
    fr_none = models.CopyFromBooleanField()
    fr_othertype = models.CopyFromCharField(max_length=200, blank=True)
    fr_comments = models.CopyFromCharField(max_length=200, blank=True)
    hazardreviewdate = models.CopyFromDateTime(blank=True)
    changecompletiondate = models.CopyFromDateTime(blank=True)
    mh_toxicrelease = models.CopyFromBooleanField()
    mh_fire = models.CopyFromBooleanField()
    mh_explosion = models.CopyFromBooleanField()
    mh_runawayreaction = models.CopyFromBooleanField()
    mh_polymerization = models.CopyFromBooleanField()
    mh_overpressurization = models.CopyFromBooleanField()
    mh_corrosion = models.CopyFromBooleanField()
    mh_overfilling = models.CopyFromBooleanField()
    mh_contamination = models.CopyFromBooleanField()
    mh_equipmentfailure = models.CopyFromBooleanField()
    mh_coolingloss = models.CopyFromBooleanField()
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
    pc_automaticshutoffs = models.CopyFromBooleanField()
    pc_interlocks = models.CopyFromBooleanField()
    pc_alarms = models.CopyFromBooleanField()
    pc_keyedbypass = models.CopyFromBooleanField()
    pc_emergencyairsupply = models.CopyFromBooleanField()
    pc_emergencypower = models.CopyFromBooleanField()
    pc_backuppump = models.CopyFromBooleanField()
    pc_groundingequipment = models.CopyFromBooleanField()
    pc_inhibitoraddition = models.CopyFromBooleanField()
    pc_rupturedisks = models.CopyFromBooleanField()
    pc_excessflowdevice = models.CopyFromBooleanField()
    pc_quenchsystem = models.CopyFromBooleanField()
    pc_purgesystem = models.CopyFromBooleanField()
    pc_none = models.CopyFromBooleanField()
    pc_othertype = models.CopyFromCharField(max_length=200, blank=True)
    ms_sprinklersystem = models.CopyFromBooleanField()
    ms_dikes = models.CopyFromBooleanField()
    ms_firewalls = models.CopyFromBooleanField()
    ms_blastwalls = models.CopyFromBooleanField()
    ms_delugesystem = models.CopyFromBooleanField()
    ms_watercurtain = models.CopyFromBooleanField()
    ms_enclosure = models.CopyFromBooleanField()
    ms_neutralization = models.CopyFromBooleanField()
    ms_none = models.CopyFromBooleanField()
    ms_othertype = models.CopyFromCharField(max_length=200, blank=True)
    md_processareadetectors = models.CopyFromBooleanField()
    md_perimetermonitors = models.CopyFromBooleanField()
    md_none = models.CopyFromBooleanField()
    md_othertype = models.CopyFromCharField(max_length=200, blank=True)
    ch_chemicalreduction = models.CopyFromBooleanField()
    ch_chemicalincrease = models.CopyFromBooleanField()
    ch_changeprocessparameters = models.CopyFromBooleanField()
    ch_installprocesscontrols = models.CopyFromBooleanField()
    ch_installprocessdetection = models.CopyFromBooleanField()
    ch_installperimetermonitoring = models.CopyFromBooleanField()
    ch_installmitigationsystems = models.CopyFromBooleanField()
    ch_nonerequired = models.CopyFromBooleanField()
    ch_none = models.CopyFromBooleanField()
    ch_otherchanges = models.CopyFromCharField(max_length=200, blank=True)
    opproceduresreviewdate = models.CopyFromDateTime(blank=True)
    trainingreviewdate = models.CopyFromDateTime(blank=True)
    tr_classroom = models.CopyFromBooleanField()
    tr_onthejob = models.CopyFromBooleanField()
    tr_othertype = models.CopyFromCharField(max_length=200, blank=True)
    ct_writtentest = models.CopyFromBooleanField()
    ct_oraltest = models.CopyFromBooleanField()
    ct_demonstration = models.CopyFromBooleanField()
    ct_observation = models.CopyFromBooleanField()
    ct_othertype = models.CopyFromCharField(max_length=200, blank=True)
    maintenancereviewdate = models.CopyFromDateTime(blank=True)
    equipmentinspectiondate = models.CopyFromDateTime(blank=True)
    equipmenttested = models.CopyFromCharField(max_length=200, blank=True)
    complianceauditdate = models.CopyFromDateTime(blank=True)
    auditcompletiondate = models.CopyFromDateTime(blank=True)
    incidentinvestigationdate = models.CopyFromDateTime(blank=True)
    investigationchangedate = models.CopyFromDateTime(blank=True)
    mostrecentchangedate = models.CopyFromDateTime(blank=True)
    cbi_flag = models.CopyFromBooleanField()
    description = models.CopyFromTextField(blank=True) # TODO to rmp_prev2text with preventionprogramID

    source_file = 'tblS8PreventionProgram2'

    class Meta:
        db_table = 'tblS8PreventionProgram2'
