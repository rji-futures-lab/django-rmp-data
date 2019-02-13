"""Models for RMP source files with `tblS5...` prefix."""
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

class tblS5FlammablesAltReleases(BaseRMPModel):
    FlammableID = CopyFromIntegerField(
        primary_key=True,
    )
    ProcessChemicalID = CopyFromForeignKey(
        'tblS1ProcessChemicals',
        db_column='ProcessChemicalID',
        on_delete=models.PROTECT,
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
    EndpointUsed = CopyFromCharField(
        max_length=30,
        blank=True,
    )
    LFL_Value = CopyFromFloatField(
        null=True,
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
    PM_FireWalls = CopyFromBooleanField(
    )
    PM_BlastWalls = CopyFromBooleanField(
    )
    PM_Enclosures = CopyFromBooleanField(
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
    AM_ExcessFlowValve = CopyFromBooleanField(
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
        verbose_name = 'Flammables: Alternative Release Scenario'
