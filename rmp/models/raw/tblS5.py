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
    flammableid = CopyFromIntegerField(
        primary_key=True,
        source_column='FlammableID',
    )
    processchemicalid = CopyFromForeignKey(
        'tblS1ProcessChemicals',
        on_delete=models.PROTECT,
        source_column='ProcessChemicalID',
    )
    analyticalbasis = CopyFromCharField(
        source_column='AnalyticalBasis',
        max_length=255,
        blank=True,
    )
    scenario = CopyFromCharField(
        source_column='Scenario',
        max_length=200,
        null=True,
    )
    quantityreleased = CopyFromFloatField(
        source_column='QuantityReleased',
        null=True,
    )
    endpointused = CopyFromCharField(
        source_column='EndpointUsed',
        max_length=30,
        blank=True,
    )
    lfl_value = CopyFromFloatField(
        source_column='LFL_Value',
        null=True,
    )
    distance2endpoint = CopyFromFloatField(
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
    pm_firewalls = CopyFromBooleanField(
        source_column='PM_FireWalls',
    )
    pm_blastwalls = CopyFromBooleanField(
        source_column='PM_BlastWalls',
    )
    pm_enclosures = CopyFromBooleanField(
        source_column='PM_Enclosures',
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
    am_excessflowvalve = CopyFromBooleanField(
        source_column='AM_ExcessFlowValve',
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
        verbose_name = 'Flammables: Alternative Release Scenario'
