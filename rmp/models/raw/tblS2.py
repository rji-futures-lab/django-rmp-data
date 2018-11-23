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
    toxicid = CopyFromIntegerField(
        primary_key=True,
        source_column='ToxicID',
    )
    processchemicalid = CopyFromForeignKey(
        'tblS1ProcessChemicals',
        on_delete=models.PROTECT,
        source_column='ProcessChemicalID',
    )
    percentweight = CopyFromFloatField(
        source_column='PercentWeight',
        null=True,
    )
    physicalstate = CopyFromCharField(
        source_column='PhysicalState',
        max_length=1,
        blank=True,
        )
    analyticalbasis = CopyFromCharField(
        source_column='AnalyticalBasis',
        max_length=255,
        blank=True,
    )
    scenario = CopyFromBooleanField(
        source_column='Scenario',
        null=True,
    )
    quantityreleased = CopyFromFloatField(
        source_column='QuantityReleased',
        null=True,
    )
    releaseduration = CopyFromFloatField(
        source_column='ReleaseDuration',
        null=True,
    )
    releaserate = CopyFromFloatField(
        source_column='ReleaseRate',
        null=True,
    )
    windspeed = CopyFromFloatField(
        source_column='WindSpeed',
    )
    stabilityclass = CopyFromCharField(
        source_column='StabilityClass',
        max_length=1,
        blank=True,
    )
    topography = CopyFromForeignKey(
        'tlkpTopographyCode',
        on_delete=models.PROTECT,
        source_column='Topography',
        blank=True,
    )
    endpoint_distance = CopyFromFloatField(
        source_column='Distance2Endpoint',
        null=True,
    )
    residentialpopulation = CopyFromBigIntegerField(
        source_column='ResidentialPopulation',
        null=True,
    )
    pr_schools = CopyFromBooleanField(
        source_column='PR_Schools',
    )
    pr_residences = CopyFromBooleanField(
        source_column='PR_Residences',
    )
    pr_hospitals = CopyFromBooleanField(
        source_column='PR_Hospitals',
    )
    pr_prisons = CopyFromBooleanField(
        source_column='PR_Prisons',
    )
    pr_publicrecreation = CopyFromBooleanField(
        source_column='PR_PublicRecreation',
    )
    pr_comm_ind = CopyFromBooleanField(
        source_column='PR_Comm_Ind',
    )
    pr_othertype = CopyFromCharField(
        source_column='PR_OtherType',
        max_length=200,
        blank=True,
    )
    er_natlstateparks = CopyFromBooleanField(
        source_column='ER_NatlStateParks',
    )
    er_wildlifesactuary = CopyFromBooleanField(
        source_column='ER_WildlifeSactuary',
    )
    er_fedwilderness = CopyFromBooleanField(
        source_column='ER_FedWilderness',
    )
    er_othertype = CopyFromCharField(
        source_column='ER_OtherType',
        max_length=200,
        blank=True,
    )
    pm_dikes = CopyFromBooleanField(
        source_column='PM_Dikes',
    )
    pm_enclosures = CopyFromBooleanField(
        source_column='PM_Enclosures',
    )
    pm_berms = CopyFromBooleanField(
        source_column='PM_Berms',
    )
    pm_drains = CopyFromBooleanField(
        source_column='PM_Drains',
    )
    pm_sumps = CopyFromBooleanField(
        source_column='PM_Sumps',
    )
    pm_othertype = CopyFromCharField(
        source_column='PM_OtherType',
        max_length=200,
        blank=True,
    )
    ptrgraphic = CopyFromBooleanField(
        source_column='ptrGraphic',
        max_length=12,
        null=True,
    )
    cbi_flag = CopyFromBooleanField(
        source_column='CBI_Flag',
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
