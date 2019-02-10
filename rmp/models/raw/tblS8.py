"""Models for RMP source files with `tblS8...` prefix."""
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


class tblS8_Prevention_Program_Chemicals(BaseRMPModel):
    primarykey = CopyFromIntegerField(
        source_column='PrimaryKey',
        primary_key=True,
    )
    preventionprogram2id = CopyFromForeignKey(
        'tblS8PreventionProgram2',
        source_column='PreventionProgram2ID',
        on_delete=models.PROTECT
    )
    processchemicalid = CopyFromForeignKey(
        'tblS1ProcessChemicals',
        source_column='ProcessChemicalID',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'Prevention Program: Program Level 2 Chemicals'
        verbose_name_plural = 'Prevention Program: Program Level 2 Chemicals'


class tblS8PreventionProgram2(BaseRMPModel):
    preventionprogram2id = CopyFromIntegerField(
        source_column='PreventionProgram2ID',
        primary_key=True,
    )
    process_naics_id = CopyFromForeignKey(
        'tblS1Process_NAICS',
        source_column='Process_NAICS_ID',
        on_delete=models.PROTECT,
    )
    safetyreviewdate = CopyFromDateTimeField(
        source_column='SafetyReviewDate',
        null=True,
    )
    fr_nfpa58 = CopyFromBooleanField(
        source_column='FR_NFPA58',
    )
    fr_osha = CopyFromBooleanField(
        source_column='FR_OSHA',
    )
    fr_astm = CopyFromBooleanField(
        source_column='FR_ASTM',
    )
    fr_ansi = CopyFromBooleanField(
        source_column='FR_ANSI',
    )
    fr_asme = CopyFromBooleanField(
        source_column='FR_ASME',
    )
    fr_none = CopyFromBooleanField(
        source_column='FR_None',
    )
    fr_othertype = CopyFromCharField(
        source_column='FR_OtherType',
        max_length=200,
        blank=True,
    )
    fr_comments = CopyFromCharField(
        source_column='FR_Comments',
        max_length=200,
        blank=True,
    )
    hazardreviewdate = CopyFromDateTimeField(
        source_column='HazardReviewDate',
        null=True,
    )
    changecompletiondate = CopyFromDateTimeField(
        source_column='ChangeCompletionDate',
        null=True,
    )
    mh_toxicrelease = CopyFromBooleanField(
        source_column='MH_ToxicRelease',
    )
    mh_fire = CopyFromBooleanField(
        source_column='MH_Fire',
    )
    mh_explosion = CopyFromBooleanField(
        source_column='MH_Explosion',
    )
    mh_runawayreaction = CopyFromBooleanField(
        source_column='MH_RunawayReaction',
    )
    mh_polymerization = CopyFromBooleanField(
        source_column='MH_Polymerization',
    )
    mh_overpressurization = CopyFromBooleanField(
        source_column='MH_Overpressurization',
    )
    mh_corrosion = CopyFromBooleanField(
        source_column='MH_Corrosion',
    )
    mh_overfilling = CopyFromBooleanField(
        source_column='MH_Overfilling',
    )
    mh_contamination = CopyFromBooleanField(
        source_column='MH_Contamination',
    )
    mh_equipmentfailure = CopyFromBooleanField(
        source_column='MH_EquipmentFailure',
    )
    mh_coolingloss = CopyFromBooleanField(
        source_column='MH_CoolingLoss',
    )
    mh_earthquake = CopyFromBooleanField(
        source_column='MH_Earthquake',
    )
    mh_floods = CopyFromBooleanField(
        source_column='MH_Floods',
    )
    mh_tornado = CopyFromBooleanField(
        source_column='MH_Tornado',
    )
    mh_hurricanes = CopyFromBooleanField(
        source_column='MH_Hurricanes',
    )
    mh_othertype = CopyFromCharField(
        source_column='MH_OtherType',
        max_length=200,
        blank=True,
    )
    pc_vents = CopyFromBooleanField(
        source_column='PC_Vents',
    )
    pc_reliefvalves = CopyFromBooleanField(
        source_column='PC_ReliefValves',
    )
    pc_checkvalves = CopyFromBooleanField(
        source_column='PC_CheckValves',
    )
    pc_scrubbers = CopyFromBooleanField(
        source_column='PC_Scrubbers',
    )
    pc_flares = CopyFromBooleanField(
        source_column='PC_Flares',
    )
    pc_manualshutoffs = CopyFromBooleanField(
        source_column='PC_ManualShutoffs',
    )
    pc_automaticshutoffs = CopyFromBooleanField(
        source_column='PC_AutomaticShutoffs',
    )
    pc_interlocks = CopyFromBooleanField(
        source_column='PC_Interlocks',
    )
    pc_alarms = CopyFromBooleanField(
        source_column='PC_Alarms',
    )
    pc_keyedbypass = CopyFromBooleanField(
        source_column='PC_KeyedBypass',
    )
    pc_emergencyairsupply = CopyFromBooleanField(
        source_column='PC_EmergencyAirSupply',
    )
    pc_emergencypower = CopyFromBooleanField(
        source_column='PC_EmergencyPower',
    )
    pc_backuppump = CopyFromBooleanField(
        source_column='PC_BackupPump',
    )
    pc_groundingequipment = CopyFromBooleanField(
        source_column='PC_GroundingEquipment',
    )
    pc_inhibitoraddition = CopyFromBooleanField(
        source_column='PC_InhibitorAddition',
    )
    pc_rupturedisks = CopyFromBooleanField(
        source_column='PC_RuptureDisks',
    )
    pc_excessflowdevice = CopyFromBooleanField(
        source_column='PC_ExcessFlowDevice',
    )
    pc_quenchsystem = CopyFromBooleanField(
        source_column='PC_QuenchSystem',
    )
    pc_purgesystem = CopyFromBooleanField(
        source_column='PC_PurgeSystem',
    )
    pc_none = CopyFromBooleanField(
        source_column='PC_None',
    )
    pc_othertype = CopyFromCharField(
        source_column='PC_OtherType',
        max_length=200,
        blank=True,
    )
    ms_sprinklersystem = CopyFromBooleanField(
        source_column='MS_SprinklerSystem',
    )
    ms_dikes = CopyFromBooleanField(
        source_column='MS_Dikes',
    )
    ms_firewalls = CopyFromBooleanField(
        source_column='MS_FireWalls',
    )
    ms_blastwalls = CopyFromBooleanField(
        source_column='MS_BlastWalls',
    )
    ms_delugesystem = CopyFromBooleanField(
        source_column='MS_DelugeSystem',
    )
    ms_watercurtain = CopyFromBooleanField(
        source_column='MS_WaterCurtain',
    )
    ms_enclosure = CopyFromBooleanField(
        source_column='MS_Enclosure',
    )
    ms_neutralization = CopyFromBooleanField(
        source_column='MS_Neutralization',
    )
    ms_none = CopyFromBooleanField(
        source_column='MS_None',
    )
    ms_othertype = CopyFromCharField(
        source_column='MS_OtherType',
        max_length=200,
        blank=True,
    )
    md_processareadetectors = CopyFromBooleanField(
        source_column='MD_ProcessAreaDetectors',
    )
    md_perimetermonitors = CopyFromBooleanField(
        source_column='MD_PerimeterMonitors',
    )
    md_none = CopyFromBooleanField(
        source_column='MD_None',
    )
    md_othertype = CopyFromCharField(
        source_column='MD_OtherType',
        max_length=200,
        blank=True,
    )
    ch_chemicalreduction = CopyFromBooleanField(
        source_column='CH_ChemicalReduction',
    )
    ch_chemicalincrease = CopyFromBooleanField(
        source_column='CH_ChemicalIncrease',
    )
    ch_changeprocessparameters = CopyFromBooleanField(
        source_column='CH_ChangeProcessParameters',
    )
    ch_installprocesscontrols = CopyFromBooleanField(
        source_column='CH_InstallProcessControls',
    )
    ch_installprocessdetection = CopyFromBooleanField(
        source_column='CH_InstallProcessDetection',
    )
    ch_installperimetermonitoring = CopyFromBooleanField(
        source_column='CH_InstallPerimeterMonitoring',
    )
    ch_installmitigationsystems = CopyFromBooleanField(
        source_column='CH_InstallMitigationSystems',
    )
    ch_nonerequired = CopyFromBooleanField(
        source_column='CH_NoneRequired',
    )
    ch_none = CopyFromBooleanField(
        source_column='CH_None',
    )
    ch_otherchanges = CopyFromCharField(
        source_column='CH_OtherChanges',
        max_length=200,
        blank=True,
    )
    opproceduresreviewdate = CopyFromDateTimeField(
        source_column='OpProceduresReviewDate',
        null=True,
    )
    trainingreviewdate = CopyFromDateTimeField(
        source_column='TrainingReviewDate',
        null=True,
    )
    tr_classroom = CopyFromBooleanField(
        source_column='TR_Classroom',
    )
    tr_onthejob = CopyFromBooleanField(
        source_column='TR_OnTheJob',
    )
    tr_othertype = CopyFromCharField(
        source_column='TR_OtherType',
        max_length=200,
        blank=True,
    )
    ct_writtentest = CopyFromBooleanField(
        source_column='CT_WrittenTest',
    )
    ct_oraltest = CopyFromBooleanField(
        source_column='CT_OralTest',
    )
    ct_demonstration = CopyFromBooleanField(
        source_column='CT_Demonstration',
    )
    ct_observation = CopyFromBooleanField(
        source_column='CT_Observation',
    )
    ct_othertype = CopyFromCharField(
        source_column='CT_OtherType',
        max_length=200,
        blank=True,
    )
    maintenancereviewdate = CopyFromDateTimeField(
        source_column='MaintenanceReviewDate',
        null=True,
    )
    equipmentinspectiondate = CopyFromDateTimeField(
        source_column='EquipmentInspectionDate',
        null=True,
    )
    equipmenttested = CopyFromCharField(
        source_column='EquipmentTested',
        max_length=200,
        blank=True,
    )
    complianceauditdate = CopyFromDateTimeField(
        source_column='ComplianceAuditDate',
        null=True,
    )
    auditcompletiondate = CopyFromDateTimeField(
        source_column='AuditCompletionDate',
        null=True,
    )
    incidentinvestigationdate = CopyFromDateTimeField(
        source_column='IncidentInvestigationDate',
        null=True,
    )
    investigationchangedate = CopyFromDateTimeField(
        source_column='InvestigationChangeDate',
        null=True,
    )
    mostrecentchangedate = CopyFromDateTimeField(
        source_column='MostRecentChangeDate',
        null=True,
    )
    cbi_flag = CopyFromBooleanField(
        source_column='CBI_Flag',
    )
    description = CopyFromTextField(
        source_column='Description',
        blank=True,
    )

    class Meta:
        verbose_name = 'Prevention Program: Program Level 2'
        verbose_name_plural = 'Prevention Program: Program Level 2'
