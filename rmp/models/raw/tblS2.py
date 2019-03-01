"""Models for raw RMP source files with `tblS2...` prefix."""
from django.db import models
from rmp.fields import (
    CopyFromBigIntegerField,
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromFloatField,
    CopyFromIntegerField,
    CopyFromForeignKey,
)
from rmp.models.base import BaseRMPModel


class tblS2ToxicsWorstCase(BaseRMPModel):
    ToxicID = CopyFromIntegerField(
        primary_key=True,
    )
    ProcessChemicalID = CopyFromForeignKey(
        'tblS1ProcessChemicals',
        on_delete=models.PROTECT,
        db_column='ProcessChemicalID',
    )
    PercentWeight = CopyFromFloatField(
        null=True,
    )
    PhysicalState = CopyFromForeignKey(
        'tlkpPhysicalStateCodes',
        db_column='PhysicalState',
        max_length=1,
        blank=True,
        on_delete=models.PROTECT,
    )
    AnalyticalBasis = CopyFromCharField(
        max_length=255,
        blank=True,
    )
    Scenario = CopyFromForeignKey(
        'tlkpS2ScenarioCodes',
        db_column='Scenario',
        blank=True,
        on_delete=models.PROTECT,
    )
    QuantityReleased = CopyFromFloatField(
        null=True,
    )
    ReleaseDuration = CopyFromFloatField(
        null=True,
    )
    ReleaseRate = CopyFromFloatField(
        null=True,
    )
    WindSpeed = CopyFromFloatField()
    StabilityClass = CopyFromCharField(
        # this prob should be CopyFromForeignKey, but I can't figure out which
        # tlkp table it should reference. Values are A-F
        max_length=1,
        blank=True,
    )
    Topography = CopyFromForeignKey(
        'tlkpTopographyCode',
        on_delete=models.PROTECT,
        db_column='Topography',
        blank=True,
    )
    Distance2Endpoint = CopyFromFloatField(
        null=True,
    )
    ResidentialPopulation = CopyFromBigIntegerField(
        null=True,
    )
    PR_Schools = CopyFromBooleanField(
    )
    PR_Residences = CopyFromBooleanField(
    )
    PR_Hospitals = CopyFromBooleanField(
    )
    PR_Prisons = CopyFromBooleanField(
    )
    PR_PublicRecreation = CopyFromBooleanField(
    )
    PR_Comm_Ind = CopyFromBooleanField(
    )
    PR_OtherType = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    ER_NatlStateParks = CopyFromBooleanField(
    )
    ER_WildlifeSactuary = CopyFromBooleanField(
    )
    ER_FedWilderness = CopyFromBooleanField(
    )
    ER_OtherType = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    PM_Dikes = CopyFromBooleanField(
    )
    PM_Enclosures = CopyFromBooleanField(
    )
    PM_Berms = CopyFromBooleanField(
    )
    PM_Drains = CopyFromBooleanField(
    )
    PM_Sumps = CopyFromBooleanField(
    )
    PM_OtherType = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    ptrGraphic = CopyFromBooleanField(
        max_length=12,
        null=True,
    )
    CBI_Flag = CopyFromBooleanField(
    )

    class Meta:
        verbose_name = 'Toxics: Worst Case Scenario'
        verbose_name_plural = 'Toxics: Worst Case Scenarios'


# class tblS2ToxicsWorstCase_ChangeHistory(BaseRMPModel):
    # toxicchangehistoryid = (
    #     source_column='ToxicChangeHistoryID',
    # )
    # facilitychangehistoryid = (
    #     source_column='FacilityChangeHistoryID',
    # )
    # cdxcorrectioncode = (
    #     source_column='CDXCorrectionCode',
    # )
    # toxicid = (
    #     source_column='ToxicID',
    # )
    # processchemicalid = (
    #     source_column='ProcessChemicalID',
    # )
    # percentweight = (
    #     source_column='PercentWeight',
    # )
    # oldpercentweight = (
    #     source_column='OldPercentWeight',
    # )
    # physicalstate = (
    #     source_column='PhysicalState',
    # )
    # oldphysicalstate = (
    #     source_column='OldPhysicalState',
    # )
    # analyticalbasis = (
    #     source_column='AnalyticalBasis',
    # )
    # oldanalyticalbasis = (
    #     source_column='OldAnalyticalBasis',
    # )
    # scenario = (
    #     source_column='Scenario',
    # )
    # oldscenario = (
    #     source_column='OldScenario',
    # )
    # quantityreleased = (
    #     source_column='QuantityReleased',
    # )
    # oldquantityreleased = (
    #     source_column='OldQuantityReleased',
    # )
    # releaseduration = (
    #     source_column='ReleaseDuration',
    # )
    # oldreleaseduration = (
    #     source_column='OldReleaseDuration',
    # )
    # releaserate = (
    #     source_column='ReleaseRate',
    # )
    # oldreleaserate = (
    #     source_column='OldReleaseRate',
    # )
    # windspeed = (
    #     source_column='WindSpeed',
    # )
    # oldwindspeed = (
    #     source_column='OldWindSpeed',
    # )
    # stabilityclass = (
    #     source_column='StabilityClass',
    # )
    # oldstabilityclass = (
    #     source_column='OldStabilityClass',
    # )
    # topography = (
    #     source_column='Topography',
    # )
    # oldtopography = (
    #     source_column='OldTopography',
    # )
    # distance2endpoint = (
    #     source_column='Distance2Endpoint',
    # )
    # olddistance2endpoint = (
    #     source_column='OldDistance2Endpoint',
    # )
    # residentialpopulation = (
    #     source_column='ResidentialPopulation',
    # )
    # oldresidentialpopulation = (
    #     source_column='OldResidentialPopulation',
    # )
    # pr_schools = (
    #     source_column='PR_Schools',
    # )
    # oldpr_schools = (
    #     source_column='OldPR_Schools',
    # )
    # pr_residences = (
    #     source_column='PR_Residences',
    # )
    # oldpr_residences = (
    #     source_column='OldPR_Residences',
    # )
    # pr_hospitals = (
    #     source_column='PR_Hospitals',
    # )
    # oldpr_hospitals = (
    #     source_column='OldPR_Hospitals',
    # )
    # pr_prisons = (
    #     source_column='PR_Prisons',
    # )
    # oldpr_prisons = (
    #     source_column='OldPR_Prisons',
    # )
    # pr_publicrecreation = (
    #     source_column='PR_PublicRecreation',
    # )
    # oldpr_publicrecreation = (
    #     source_column='OldPR_PublicRecreation',
    # )
    # pr_comm_ind = (
    #     source_column='PR_Comm_Ind',
    # )
    # oldpr_comm_ind = (
    #     source_column='OldPR_Comm_Ind',
    # )
    # pr_othertype = (
    #     source_column='PR_OtherType',
    # )
    # oldpr_othertype = (
    #     source_column='OldPR_OtherType',
    # )
    # er_natlstateparks = (
    #     source_column='ER_NatlStateParks',
    # )
    # older_natlstateparks = (
    #     source_column='OldER_NatlStateParks',
    # )
    # er_wildlifesactuary = (
    #     source_column='ER_WildlifeSactuary',
    # )
    # older_wildlifesactuary = (
    #     source_column='OldER_WildlifeSactuary',
    # )
    # er_fedwilderness = (
    #     source_column='ER_FedWilderness',
    # )
    # older_fedwilderness = (
    #     source_column='OldER_FedWilderness',
    # )
    # er_othertype = (
    #     source_column='ER_OtherType',
    # )
    # older_othertype = (
    #     source_column='OldER_OtherType',
    # )
    # pm_dikes = (
    #     source_column='PM_Dikes',
    # )
    # oldpm_dikes = (
    #     source_column='OldPM_Dikes',
    # )
    # pm_enclosures = (
    #     source_column='PM_Enclosures',
    # )
    # oldpm_enclosures = (
    #     source_column='OldPM_Enclosures',
    # )
    # pm_berms = (
    #     source_column='PM_Berms',
    # )
    # oldpm_berms = (
    #     source_column='OldPM_Berms',
    # )
    # pm_drains = (
    #     source_column='PM_Drains',
    # )
    # oldpm_drains = (
    #     source_column='OldPM_Drains',
    # )
    # pm_sumps = (
    #     source_column='PM_Sumps',
    # )
    # oldpm_sumps = (
    #     source_column='OldPM_Sumps',
    # )
    # pm_othertype = (
    #     source_column='PM_OtherType',
    # )
    # oldpm_othertype = (
    #     source_column='OldPM_OtherType',
    # )
    # ptrgraphic = (
    #     source_column='ptrGraphic',
    # )
    # oldptrgraphic = (
    #     source_column='OldptrGraphic',
    # )
