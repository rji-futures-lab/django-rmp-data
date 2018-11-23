"""Models for RMP source files with `tblS4...` prefix."""
from django.db import models
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromFloatField,
    CopyFromIntegerField,
    CopyFromForeignKey,
)
from rmp.models.base import BaseRMPModel

class tblS4FlammablesWorstCase(BaseRMPModel):
    flammableid = CopyFromIntegerField(
        source_column='FlammableID',
        primary_key=True,
    )
    processchemicalid = CopyFromForeignKey(
        'tblS1ProcessChemicals',
        source_column='ProcessChemicalID',
        on_delete=models.PROTECT,
    )
    analyticalbasis = CopyFromCharField(
        source_column='AnalyticalBasis',
        max_length=255,
        blank=True,
    )
    quantityreleased = CopyFromFloatField(
        source_column='QuantityReleased',
        null=True,
    )
    endpoint_distance = CopyFromFloatField(
        source_column='Distance2Endpoint',
        null=True,
    )
    residentialpopulation = CopyFromCharField(
        source_column='ResidentialPopulation',
        max_length=9,
        blank=True,
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
    pm_blastwalls = CopyFromBooleanField(
        source_column='PM_BlastWalls',
        )
    pm_othertype = CopyFromCharField(
        source_column='PM_OtherType',
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
        verbose_name = 'Flammables: Worst Case Scenario'
