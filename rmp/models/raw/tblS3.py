"""Models for RMP source files with `tblS3...` prefix."""
from django.db import models
from rmp.fields import (
    CopyFromBigIntegerField,
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromFloatField,
    CopyFromForeignKey,
    CopyFromIntegerField,
)
from rmp.models.base import BaseRMPModel


class tblS3ToxicsAltReleases(BaseRMPModel):
    toxicid = CopyFromIntegerField(
        source_column='ToxicID',
        primary_key=True,
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
    physicalstate = CopyFromForeignKey(
        'tlkpPhysicalStateCodes',
        on_delete=models.PROTECT,
        source_column='PhysicalState',
        blank=True,
    )
    analyticalbasis = CopyFromCharField(
        source_column='AnalyticalBasis',
        max_length=255,
        blank=True,
    )
    scenario = CopyFromCharField(
        source_column='Scenario',
        max_length=200,
        blank=True,
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
        null=True,
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
    am_sprinklersystems = CopyFromBooleanField(
        source_column='AM_SprinklerSystems',
    )
    am_delugesystems = CopyFromBooleanField(
        source_column='AM_DelugeSystems',
    )
    am_watercurtain = CopyFromBooleanField(
        source_column='AM_WaterCurtain',
    )
    am_neutralization = CopyFromBooleanField(
        source_column='AM_Neutralization',
    )
    am_excessflowvalve = CopyFromBooleanField(
        source_column='AM_ExcessFlowValve',
    )
    am_flares = CopyFromBooleanField(
        source_column='AM_Flares',
    )
    am_scrubbers = CopyFromBooleanField(
        source_column='AM_Scrubbers',
    )
    am_emergencyshutdown = CopyFromBooleanField(
        source_column='AM_EmergencyShutdown',
    )
    am_othertype = CopyFromCharField(
        source_column='AM_OtherType',
        max_length=200,
        blank=True,
    )
    ptrgraphic = CopyFromCharField(
        source_column='ptrGraphic',
        max_length=12,
        blank=True,
    )
    cbi_flag = CopyFromBooleanField(
        source_column='CBI_Flag',
    )

    class Meta:
        verbose_name = 'Toxics: Alternative Release Scenario'
