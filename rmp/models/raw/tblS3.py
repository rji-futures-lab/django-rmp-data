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
    ToxicID = CopyFromIntegerField(
        primary_key=True,
    )
    ProcessChemicalID = CopyFromForeignKey(
        'tblS1ProcessChemicals',
        db_column='ProcessChemicalID',
        on_delete=models.PROTECT,
    )
    PercentWeight = CopyFromFloatField(
        null=True,
    )
    PhysicalState = CopyFromForeignKey(
        'tlkpPhysicalStateCodes',
        db_column='PhysicalState',
        on_delete=models.PROTECT,
        blank=True,
    )
    AnalyticalBasis = CopyFromCharField(
        max_length=255,
        blank=True,
    )
    Scenario = CopyFromCharField(
        max_length=200,
        blank=True,
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
    WindSpeed = CopyFromFloatField(
        null=True,
    )
    StabilityClass = CopyFromCharField(
        max_length=1,
        blank=True,
    )
    Topography = CopyFromForeignKey(
        'tlkpTopographyCode',
        db_column='Topography',
        on_delete=models.PROTECT,
        blank=True,
    )
    Distance2Endpoint = CopyFromFloatField(
        source_column='Distance2Endpoint',
        null=True,
    )
    ResidentialPopulation = CopyFromBigIntegerField(
        source_column='ResidentialPopulation',
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
    AM_SprinklerSystems = CopyFromBooleanField(
    )
    AM_DelugeSystems = CopyFromBooleanField(
    )
    AM_WaterCurtain = CopyFromBooleanField(
    )
    AM_Neutralization = CopyFromBooleanField(
    )
    AM_ExcessFlowValve = CopyFromBooleanField(
    )
    AM_Flares = CopyFromBooleanField(
    )
    AM_Scrubbers = CopyFromBooleanField(
    )
    AM_EmergencyShutdown = CopyFromBooleanField(
    )
    AM_OtherType = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    ptrGraphic = CopyFromCharField(
        max_length=12,
        blank=True,
    )
    CBI_Flag = CopyFromBooleanField(
    )

    class Meta:
        verbose_name = 'Toxics: Alternative Release Scenario'
