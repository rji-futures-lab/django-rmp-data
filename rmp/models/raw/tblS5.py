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
        source_column='FlammableID',
        primary_key=True,
    )
    ProcessChemicalID = CopyFromForeignKey(
        'tblS1ProcessChemicals',
        source_column='ProcessChemicalID',
        on_delete=models.PROTECT,
    )
    AnalyticalBasis = CopyFromCharField(
        source_column='AnalyticalBasis',
        max_length=255,
        blank=True,
    )
    Scenario = CopyFromCharField(
        source_column='Scenario',
        max_length=200,
        null=True,
    )
    QuantityReleased = CopyFromFloatField(
        source_column='QuantityReleased',
        null=True,
    )
    EndpointUsed = CopyFromCharField(
        source_column='EndpointUsed',
        max_length=30,
        blank=True,
    )
    LFL_Value = CopyFromFloatField(
        source_column='LFL_Value',
        null=True,
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
        source_column='PR_Schools',
    )
    PR_Residences = CopyFromBooleanField(
        source_column='PR_Residences',
    )
    PR_Hospitals = CopyFromBooleanField(
        source_column='PR_Hospitals',
    )
    PR_Prisons = CopyFromBooleanField(
        source_column='PR_Prisons',
    )
    PR_PublicRecreation = CopyFromBooleanField(
        source_column='PR_PublicRecreation',
    )
    PR_Comm_Ind = CopyFromBooleanField(
        source_column='PR_Comm_Ind',
    )
    PR_OtherType = CopyFromCharField(
        source_column='PR_OtherType',
        max_length=200,
        blank=True,
    )
    ER_NatlStateParks = CopyFromBooleanField(
        source_column='ER_NatlStateParks',
    )
    ER_WildlifeSactuary = CopyFromBooleanField(
        source_column='ER_WildlifeSactuary',
    )
    ER_FedWilderness = CopyFromBooleanField(
        source_column='ER_FedWilderness',
    )
    ER_OtherType = CopyFromCharField(
        source_column='ER_OtherType',
        max_length=200,
        blank=True,
    )
    PM_Dikes = CopyFromBooleanField(
        source_column='PM_Dikes',
    )
    PM_FireWalls = CopyFromBooleanField(
        source_column='PM_FireWalls',
    )
    PM_BlastWalls = CopyFromBooleanField(
        source_column='PM_BlastWalls',
    )
    PM_Enclosures = CopyFromBooleanField(
        source_column='PM_Enclosures',
    )
    PM_OtherType = CopyFromCharField(
        source_column='PM_OtherType',
        max_length=200,
        blank=True,
    )
    AM_SprinklerSystems = CopyFromBooleanField(
        source_column='AM_SprinklerSystems',
    )
    AM_DelugeSystems = CopyFromBooleanField(
        source_column='AM_DelugeSystems',
    )
    AM_WaterCurtain = CopyFromBooleanField(
        source_column='AM_WaterCurtain',
    )
    AM_ExcessFlowValve = CopyFromBooleanField(
        source_column='AM_ExcessFlowValve',
    )
    AM_OtherType = CopyFromCharField(
        source_column='AM_OtherType',
        max_length=200,
        blank=True,
    )
    ptrGraphic = CopyFromCharField(
        source_column='ptrGraphic',
        max_length=12,
        blank=True,
    )
    CBI_Flag = CopyFromBooleanField(
        source_column='CBI_Flag',
    )

    class Meta:
        verbose_name = 'Flammables: Alternative Release Scenario'
