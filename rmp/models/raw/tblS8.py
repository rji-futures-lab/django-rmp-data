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
    PrimaryKey = CopyFromIntegerField(
        primary_key=True,
    )
    PreventionProgram2ID = CopyFromForeignKey(
        'tblS8PreventionProgram2',
        on_delete=models.PROTECT
    )
    ProcessChemicalID = CopyFromForeignKey(
        'tblS1ProcessChemicals',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'Prevention Program: Program Level 2 Chemicals'
        verbose_name_plural = 'Prevention Program: Program Level 2 Chemicals'


class tblS8PreventionProgram2(BaseRMPModel):
    PreventionProgram2ID = CopyFromIntegerField(
        primary_key=True,
    )
    Process_NAICS_ID = CopyFromForeignKey(
        'tblS1ProcessNAICS',
        on_delete=models.PROTECT,
    )
    SafetyReviewDate = CopyFromDateTimeField(
        null=True,
    )
    FR_NFPA58 = CopyFromBooleanField(
    )
    FR_OSHA = CopyFromBooleanField(
    )
    FR_ASTM = CopyFromBooleanField(
    )
    FR_ANSI = CopyFromBooleanField(
    )
    FR_ASME = CopyFromBooleanField(
    )
    FR_None = CopyFromBooleanField(
    )
    FR_OtherType = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    FR_Comments = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    HazardReviewDate = CopyFromDateTimeField(
        null=True,
    )
    ChangeCompletionDate = CopyFromDateTimeField(
        null=True,
    )
    MH_ToxicRelease = CopyFromBooleanField(
    )
    MH_Fire = CopyFromBooleanField(
    )
    MH_Explosion = CopyFromBooleanField(
    )
    MH_RunawayReaction = CopyFromBooleanField(
    )
    MH_Polymerization = CopyFromBooleanField(
    )
    MH_Overpressurization = CopyFromBooleanField(
    )
    MH_Corrosion = CopyFromBooleanField(
    )
    MH_Overfilling = CopyFromBooleanField(
    )
    MH_Contamination = CopyFromBooleanField(
    )
    MH_EquipmentFailure = CopyFromBooleanField(
    )
    MH_CoolingLoss = CopyFromBooleanField(
    )
    MH_Earthquake = CopyFromBooleanField(
    )
    MH_Floods = CopyFromBooleanField(
    )
    MH_Tornado = CopyFromBooleanField(
    )
    MH_Hurricanes = CopyFromBooleanField(
    )
    MH_OtherType = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    PC_Vents = CopyFromBooleanField(
    )
    PC_ReliefValves = CopyFromBooleanField(
    )
    PC_CheckValves = CopyFromBooleanField(
    )
    PC_Scrubbers = CopyFromBooleanField(
    )
    PC_Flares = CopyFromBooleanField(
    )
    PC_ManualShutoffs = CopyFromBooleanField(
    )
    PC_AutomaticShutoffs = CopyFromBooleanField(
    )
    PC_Interlocks = CopyFromBooleanField(
    )
    PC_Alarms = CopyFromBooleanField(
    )
    PC_KeyedBypass = CopyFromBooleanField(
    )
    PC_EmergencyAirSupply = CopyFromBooleanField(
    )
    PC_EmergencyPower = CopyFromBooleanField(
    )
    PC_BackupPump = CopyFromBooleanField(
    )
    PC_GroundingEquipment = CopyFromBooleanField(
    )
    PC_InhibitorAddition = CopyFromBooleanField(
    )
    PC_RuptureDisks = CopyFromBooleanField(
    )
    PC_ExcessFlowDevice = CopyFromBooleanField(
    )
    PC_QuenchSystem = CopyFromBooleanField(
    )
    PC_PurgeSystem = CopyFromBooleanField(
    )
    PC_None = CopyFromBooleanField(
    )
    PC_OtherType = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    MS_SprinklerSystem = CopyFromBooleanField(
    )
    MS_Dikes = CopyFromBooleanField(
    )
    MS_FireWalls = CopyFromBooleanField(
    )
    MS_BlastWalls = CopyFromBooleanField(
    )
    MS_DelugeSystem = CopyFromBooleanField(
    )
    MS_WaterCurtain = CopyFromBooleanField(
    )
    MS_Enclosure = CopyFromBooleanField(
    )
    MS_Neutralization = CopyFromBooleanField(
    )
    MS_None = CopyFromBooleanField(
    )
    MS_OtherType = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    MD_ProcessAreaDetectors = CopyFromBooleanField(
    )
    MD_PerimeterMonitors = CopyFromBooleanField(
    )
    MD_None = CopyFromBooleanField(
    )
    MD_OtherType = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    CH_ChemicalReduction = CopyFromBooleanField(
    )
    CH_ChemicalIncrease = CopyFromBooleanField(
    )
    CH_ChangeProcessParameters = CopyFromBooleanField(
    )
    CH_InstallProcessControls = CopyFromBooleanField(
    )
    CH_InstallProcessDetection = CopyFromBooleanField(
    )
    CH_InstallPerimeterMonitoring = CopyFromBooleanField(
    )
    CH_InstallMitigationSystems = CopyFromBooleanField(
    )
    CH_NoneRequired = CopyFromBooleanField(
    )
    CH_None = CopyFromBooleanField(
    )
    CH_OtherChanges = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    OpProceduresReviewDate = CopyFromDateTimeField(
        null=True,
    )
    TrainingReviewDate = CopyFromDateTimeField(
        null=True,
    )
    TR_Classroom = CopyFromBooleanField(
    )
    TR_OnTheJob = CopyFromBooleanField(
    )
    TR_OtherType = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    CT_WrittenTest = CopyFromBooleanField(
    )
    CT_OralTest = CopyFromBooleanField(
    )
    CT_Demonstration = CopyFromBooleanField(
    )
    CT_Observation = CopyFromBooleanField(
    )
    CT_OtherType = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    MaintenanceReviewDate = CopyFromDateTimeField(
        null=True,
    )
    EquipmentInspectionDate = CopyFromDateTimeField(
        null=True,
    )
    EquipmentTested = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    ComplianceAuditDate = CopyFromDateTimeField(
        null=True,
    )
    AuditCompletionDate = CopyFromDateTimeField(
        null=True,
    )
    IncidentInvestigationDate = CopyFromDateTimeField(
        null=True,
    )
    investigationchangedate = CopyFromDateTimeField(
        null=True,
    )
    MostRecentChangeDate = CopyFromDateTimeField(
        null=True,
    )
    CBI_Flag = CopyFromBooleanField(
    )
    Description = CopyFromTextField(
        blank=True,
    )

    class Meta:
        verbose_name = 'Prevention Program: Program Level 2'
        verbose_name_plural = 'Prevention Program: Program Level 2'
