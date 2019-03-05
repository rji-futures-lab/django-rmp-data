"""Models for raw RMP source files with `tblS6...` prefix."""
from django.db import models
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDateTimeField,
    CopyFromFloatField,
    CopyFromIntegerField,
    CopyFromForeignKey,
    CopyFromManyToManyField,
)
from rmp.models.base import BaseRMPModel

class tblS6AccidentHistory(BaseRMPModel):
    AccidentHistoryID = CopyFromIntegerField(
        primary_key=True,
    )
    FacilityID = CopyFromForeignKey(
        'tblS1Facilities',
        db_column='FacilityID',
        on_delete=models.PROTECT,
    )
    AccidentDate = CopyFromDateTimeField(
        null=True,
    )
    AccidentTime = CopyFromCharField(
        max_length=4,
        blank=True,
    )
    NAICSCode = CopyFromForeignKey(
        'tlkpNAICS',
        db_column='NAICSCode',
        on_delete=models.PROTECT,
        blank=True,
    )
    AccidentReleaseDuration = CopyFromCharField(
        max_length=5,
        blank=True,
    )
    RE_Gas = CopyFromBooleanField(
    )
    RE_Spill = CopyFromBooleanField(
    )
    RE_Fire = CopyFromBooleanField(
    )
    RE_Explosion = CopyFromBooleanField(
    )
    RE_ReactiveIncident = CopyFromBooleanField(
    )
    RS_StorageVessel = CopyFromBooleanField(
    )
    RS_Piping = CopyFromBooleanField(
    )
    RS_ProcessVessel = CopyFromBooleanField(
    )
    RS_TransferHose = CopyFromBooleanField(
    )
    RS_Valve = CopyFromBooleanField(
    )
    RS_Pump = CopyFromBooleanField(
    )
    RS_Joint = CopyFromBooleanField(
    )
    OtherReleaseSource = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    WindSpeed = CopyFromFloatField(
        null=True,
    )
    WindSpeedUnitCode = CopyFromForeignKey(
        'tlkpWindSpeedUnitCodes',
        db_column='WindSpeedUnitCode',
        on_delete=models.PROTECT,
        blank=True,
    )
    WindDirection = CopyFromCharField(
        max_length=3,
        blank=True,
    )
    Temperature = CopyFromFloatField(
        null=True,
    )
    StabilityClass = CopyFromCharField(
        max_length=1,
        blank=True,
    )
    Precipitation = CopyFromBooleanField(
    )
    WeatherUnknown = CopyFromBooleanField(
    )
    DeathsWorkers = CopyFromIntegerField(
        null=True,
    )
    DeathsPublicResponders = CopyFromIntegerField(
        null=True,
    )
    DeathsPublic = CopyFromIntegerField(
        null=True,
    )
    InjuriesWorkers = CopyFromIntegerField(
        null=True,
    )
    InjuriesPublicResponders = CopyFromIntegerField(
        null=True,
    )
    InjuriesPublic = CopyFromIntegerField(
        null=True,
    )
    OnsitePropertyDamage = CopyFromFloatField(
        null=True,
    )
    OffsiteDeaths = CopyFromBooleanField(
        null=True,
    )
    Hospitalization = CopyFromFloatField(
        null=True,
    )
    MedicalTreatment = CopyFromFloatField(
        null=True,
    )
    Evacuated = CopyFromFloatField(
        null=True,
    )
    ShelteredInPlace = CopyFromFloatField(
        null=True,
    )
    OffsitePropertyDamage = CopyFromFloatField(
        null=True,
    )
    ED_Kills = CopyFromBooleanField(
    )
    ED_MinorDefoliation = CopyFromBooleanField(
    )
    ED_WaterContamination = CopyFromBooleanField(
    )
    ED_SoilContamination = CopyFromBooleanField(
    )
    ED_Other = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    InitiatingEvent = CopyFromForeignKey(
        'tlkpS6InitiatingEvents',
        db_column='InitiatingEvent',
        on_delete=models.PROTECT,
        blank=True,
    )
    CF_EquipmentFailure = CopyFromBooleanField(
    )
    CF_HumanError = CopyFromBooleanField(
    )
    CF_ImproperProcedure = CopyFromBooleanField(
    )
    CF_Overpressurization = CopyFromBooleanField(
    )
    CF_UpsetCondition = CopyFromBooleanField(
    )
    CF_BypassCondition = CopyFromBooleanField(
    )
    CF_Maintenance = CopyFromBooleanField(
    )
    CF_ProcessDesignFailure = CopyFromBooleanField(
    )
    CF_UnsuitableEquipment = CopyFromBooleanField(
    )
    CF_UnusualWeather = CopyFromBooleanField(
    )
    CF_ManagementError = CopyFromBooleanField(
    )
    CF_Other = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    OffsiteRespondersNotify = CopyFromCharField(
        max_length=25,
        blank=True,
    )
    CI_ImprovedEquipment = CopyFromBooleanField(
    )
    CI_RevisedMaintenance = CopyFromBooleanField(
    )
    CI_RevisedTraining = CopyFromBooleanField(
    )
    CI_RevisedOpProcedures = CopyFromBooleanField(
    )
    CI_NewProcessControls = CopyFromBooleanField(
    )
    CI_NewMitigationSystems = CopyFromBooleanField(
    )
    CI_RevisedERPlan = CopyFromBooleanField(
    )
    CI_ChangedProcess = CopyFromBooleanField(
    )
    CI_ReducedInventory = CopyFromBooleanField(
    )
    CI_None = CopyFromBooleanField(
    )
    CI_OtherType = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    CBI_Flag = CopyFromBooleanField(
    )

    class Meta:
        verbose_name = 'Accident History'
        verbose_name_plural = 'Accident History'


class tblS6AccidentChemicals(BaseRMPModel):
    AccidentChemicalID = CopyFromIntegerField(
        primary_key=True,
    )
    AccidentHistoryID = CopyFromForeignKey(
        'tblS6AccidentHistory',
        db_column='AccidentHistoryID',
        on_delete=models.PROTECT,
    )
    ChemicalID = CopyFromForeignKey(
        'tlkpChemicals',
        db_column='ChemicalID',
        on_delete=models.PROTECT,
    )
    QuantityReleased = CopyFromFloatField(
        null=True,
    )
    PercentWeight = CopyFromFloatField(
        null=True,
    )

    class Meta:
        verbose_name = 'Accident History: Chemicals'
        verbose_name_plural = 'Accident History: Chemicals'


class tblS6FlammableMixtureChemicals(BaseRMPModel):
    FlamMixChemID = CopyFromIntegerField(
        primary_key=True,
    )
    AccidentChemicalID = CopyFromForeignKey(
        'tblS6AccidentChemicals',
        db_column='AccidentChemicalID',
        on_delete=models.PROTECT,
    )
    ChemicalID = CopyFromForeignKey(
        'tlkpChemicals',
        db_column='ChemicalID',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'Accident History: Flammable Mixture Chemicals'
        verbose_name_plural = 'Accident History: Flammable Mixture Chemicals'
