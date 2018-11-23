"""Models for raw RMP source files with `tblS6...` prefix."""
from django.db import models
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDateTimeField,
    CopyFromFloatField,
    CopyFromIntegerField,
    CopyFromForeignKey,
)
from rmp.models.base import BaseRMPModel


class tblS6AccidentChemicals(BaseRMPModel):
    accidentchemicalid = CopyFromIntegerField(
        source_column='AccidentChemicalID',
        primary_key=True,
    )
    accidenthistoryid = CopyFromForeignKey(
        'tblS6AccidentHistory',
        source_column='AccidentHistoryID',
        on_delete=models.PROTECT,
    )
    chemicalid = CopyFromForeignKey(
        'tlkpChemicals',
        source_column='ChemicalID',
        on_delete=models.PROTECT,
    )
    quantityreleased = CopyFromFloatField(
        source_column='QuantityReleased',
        null=True,
    )
    percentweight = CopyFromFloatField(
        source_column='PercentWeight',
        null=True,
    )

    class Meta:
        verbose_name = 'Accident History: Chemicals'
        verbose_name_plural = 'Accident History: Chemicals'


class tblS6AccidentHistory(BaseRMPModel):
    accidenthistoryid = CopyFromIntegerField(
        source_column='AccidentHistoryID',
        primary_key=True,
    )
    facilityid = CopyFromForeignKey(
        'Tbls1Facilities',
        source_column='FacilityID',
        on_delete=models.PROTECT,
    )
    accidentdate = CopyFromDateTimeField(
        source_column='AccidentDate',
        null=True,
    )
    accidenttime = CopyFromCharField(
        source_column='AccidentTime',
        max_length=4,
        blank=True,
    )
    naicscode = CopyFromForeignKey(
        'tlkpNAICS',
        source_column='NAICSCode',
        on_delete=models.PROTECT,
        blank=True,
    )
    accidentreleaseduration = CopyFromCharField(
        source_column='AccidentReleaseDuration',
        max_length=5,
        blank=True,
    )
    re_gas = CopyFromBooleanField(
        source_column='RE_Gas',
    )
    re_spill = CopyFromBooleanField(
        source_column='RE_Spill',
    )
    re_fire = CopyFromBooleanField(
        source_column='RE_Fire',
    )
    re_explosion = CopyFromBooleanField(
        source_column='RE_Explosion',
    )
    re_reactiveincident = CopyFromBooleanField(
        source_column='RE_ReactiveIncident',
    )
    rs_storagevessel = CopyFromBooleanField(
        source_column='RS_StorageVessel',
    )
    rs_piping = CopyFromBooleanField(
        source_column='RS_Piping',
    )
    rs_processvessel = CopyFromBooleanField(
        source_column='RS_ProcessVessel',
    )
    rs_transferhose = CopyFromBooleanField(
        source_column='RS_TransferHose',
    )
    rs_valve = CopyFromBooleanField(
        source_column='RS_Valve',
    )
    rs_pump = CopyFromBooleanField(
        source_column='RS_Pump',
    )
    rs_joint = CopyFromBooleanField(
        source_column='RS_Joint',
    )
    otherreleasesource = CopyFromCharField(
        source_column='OtherReleaseSource',
        max_length=200,
        blank=True,
    )
    windspeed = CopyFromFloatField(
        source_column='WindSpeed',
        null=True,
    )
    windspeedunitcode = CopyFromForeignKey(
        'tlkpWindSpeedUnitCodes',
        source_column='WindSpeedUnitCode',
        on_delete=models.PROTECT,
        blank=True,
    )
    winddirection = CopyFromCharField(
        source_column='WindDirection',
        max_length=3,
        blank=True,
    )
    temperature = CopyFromFloatField(
        source_column='Temperature',
        null=True,
    )
    stabilityclass = CopyFromCharField(
        source_column='StabilityClass',
        max_length=1,
        blank=True,
    )
    precipitation = CopyFromBooleanField(
        source_column='Precipitation',
    )
    weatherunknown = CopyFromBooleanField(
        source_column='WeatherUnknown',
    )
    deathsworkers = CopyFromIntegerField(
        source_column='DeathsWorkers',
        null=True,
    )
    deathspublicresponders = CopyFromIntegerField(
        source_column='DeathsPublicResponders',
        null=True,
    )
    deathspublic = CopyFromIntegerField(
        source_column='DeathsPublic',
        null=True,
    )
    injuriesworkers = CopyFromIntegerField(
        source_column='InjuriesWorkers',
        null=True,
    )
    injuriespublicresponders = CopyFromIntegerField(
        source_column='InjuriesPublicResponders',
        null=True,
    )
    injuriespublic = CopyFromIntegerField(
        source_column='InjuriesPublic',
        null=True,
    )
    onsitepropertydamage = CopyFromFloatField(
        source_column='OnsitePropertyDamage',
        null=True,
    )
    offsitedeaths = CopyFromBooleanField(
        source_column='OffsiteDeaths',
        null=True,
    )
    hospitalization = CopyFromFloatField(
        source_column='Hospitalization',
        null=True,
    )
    medicaltreatment = CopyFromFloatField(
        source_column='MedicalTreatment',
        null=True,
    )
    evacuated = CopyFromFloatField(
        source_column='Evacuated',
        null=True,
    )
    shelteredinplace = CopyFromFloatField(
        source_column='ShelteredInPlace',
        null=True,
    )
    offsitepropertydamage = CopyFromFloatField(
        source_column='OffsitePropertyDamage',
        null=True,
    )
    ed_kills = CopyFromBooleanField(
        source_column='ED_Kills',
    )
    ed_minordefoliation = CopyFromBooleanField(
        source_column='ED_MinorDefoliation',
    )
    ed_watercontamination = CopyFromBooleanField(
        source_column='ED_WaterContamination',
    )
    ed_soilcontamination = CopyFromBooleanField(
        source_column='ED_SoilContamination',
    )
    ed_other = CopyFromCharField(
        source_column='ED_Other',
        max_length=200,
        blank=True,
    )
    initiatingevent = CopyFromForeignKey(
        'tlkpS6InitiatingEvents',
        source_column='InitiatingEvent',
        on_delete=models.PROTECT,
        blank=True,
    )
    cf_equipmentfailure = CopyFromBooleanField(
        source_column='CF_EquipmentFailure',
    )
    cf_humanerror = CopyFromBooleanField(
        source_column='CF_HumanError',
    )
    cf_improperprocedure = CopyFromBooleanField(
        source_column='CF_ImproperProcedure',
    )
    cf_overpressurization = CopyFromBooleanField(
        source_column='CF_Overpressurization',
    )
    cf_upsetcondition = CopyFromBooleanField(
        source_column='CF_UpsetCondition',
    )
    cf_bypasscondition = CopyFromBooleanField(
        source_column='CF_BypassCondition',
    )
    cf_maintenance = CopyFromBooleanField(
        source_column='CF_Maintenance',
    )
    cf_processdesignfailure = CopyFromBooleanField(
        source_column='CF_ProcessDesignFailure',
    )
    cf_unsuitableequipment = CopyFromBooleanField(
        source_column='CF_UnsuitableEquipment',
    )
    cf_unusualweather = CopyFromBooleanField(
        source_column='CF_UnusualWeather',
    )
    cf_managementerror = CopyFromBooleanField(
        source_column='CF_ManagementError',
    )
    cf_other = CopyFromCharField(
        source_column='CF_Other',
        max_length=200,
        blank=True,
    )
    offsiterespondersnotify = CopyFromCharField(
        source_column='OffsiteRespondersNotify',
        max_length=25,
        blank=True,
    )
    ci_improvedequipment = CopyFromBooleanField(
        source_column='CI_ImprovedEquipment',
    )
    ci_revisedmaintenance = CopyFromBooleanField(
        source_column='CI_RevisedMaintenance',
    )
    ci_revisedtraining = CopyFromBooleanField(
        source_column='CI_RevisedTraining',
    )
    ci_revisedopprocedures = CopyFromBooleanField(
        source_column='CI_RevisedOpProcedures',
    )
    ci_newprocesscontrols = CopyFromBooleanField(
        source_column='CI_NewProcessControls',
    )
    ci_newmitigationsystems = CopyFromBooleanField(
        source_column='CI_NewMitigationSystems',
    )
    ci_revisederplan = CopyFromBooleanField(
        source_column='CI_RevisedERPlan',
    )
    ci_changedprocess = CopyFromBooleanField(
        source_column='CI_ChangedProcess',
    )
    ci_reducedinventory = CopyFromBooleanField(
        source_column='CI_ReducedInventory',
    )
    ci_none = CopyFromBooleanField(
        source_column='CI_None',
    )
    ci_othertype = CopyFromCharField(
        source_column='CI_OtherType',
        max_length=200,
        blank=True,
    )
    cbi_flag = CopyFromBooleanField(
        source_column='CBI_Flag',
    )

    class Meta:
        verbose_name = 'Accident History'
        verbose_name_plural = 'Accident History'


class tblS6FlammableMixtureChemicals(BaseRMPModel):
    flammixchemid = CopyFromIntegerField(
        source_column='FlamMixChemID',
        primary_key=True,
    )
    accidentchemicalid = CopyFromForeignKey(
        'Tbls6Accidentchemicals',
        source_column='AccidentChemicalID',
        on_delete=models.PROTECT,
    )
    chemicalid = CopyFromForeignKey(
        'tlkpChemicals',
        source_column='ChemicalID',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'Accident History: Flammable Mixture Chemicals'
        verbose_name_plural = 'Accident History: Flammable Mixture Chemicals'
