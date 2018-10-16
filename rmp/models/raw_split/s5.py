"""
tblS5FlammablesAltReleases.csv
"""

from django.db import models
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDecimalField,
    CopyFromIntegerField,
    CopyFromForeignKey,
)
from rmp.models.base import BaseRMPModel

class Tbls5Flammablesaltreleases(BaseRMPModel):
    flammableid = CopyFromIntegerField(primary_key=True)
    processchemicalid = CopyFromForeignKey(
        'Tbls1Processchemicals',
        on_delete=models.PROTECT,
    )
    analyticalbasis = CopyFromCharField(max_length=255, blank=True)
    scenario = CopyFromCharField(max_length=200)
    quantityreleased = CopyFromDecimalField(max_digits=5, decimal_places=2)
    endpointused = CopyFromCharField(max_length=30, blank=True)
    lfl_value = CopyFromDecimalField(max_digits=5, decimal_places=1)
    endpoint_distance = CopyFromDecimalField(max_digits=5, decimal_places=1)
    residentialpopulation = CopyFromCharField(max_length=9, blank=True)
    pr_schools = CopyFromBooleanField()
    pr_residences = CopyFromBooleanField()
    pr_hospitals = CopyFromBooleanField()
    pr_prisons = CopyFromBooleanField()
    pr_publicrecreation = CopyFromBooleanField()
    pr_comm_ind = CopyFromBooleanField()
    pr_othertype = CopyFromCharField(max_length=200, blank=True)
    er_natlstateparks = CopyFromBooleanField()
    er_wildlifesactuary = CopyFromBooleanField()
    er_fedwilderness = CopyFromBooleanField()
    er_othertype = CopyFromCharField(max_length=200, blank=True)
    pm_dikes = CopyFromBooleanField()
    pm_firewalls = CopyFromBooleanField()
    pm_blastwalls = CopyFromBooleanField()
    pm_enclosures = CopyFromBooleanField()
    pm_othertype = CopyFromCharField(max_length=200, blank=True)
    am_sprinklersystems = CopyFromBooleanField()
    am_delugesystems = CopyFromBooleanField()
    am_watercurtain = CopyFromBooleanField()
    am_excessflowvalve = CopyFromBooleanField()
    am_othertype = CopyFromCharField(max_length=200, blank=True)
    ptrgraphic = CopyFromCharField(max_length=12, blank=True)
    cbi_flag = CopyFromBooleanField()

    source_file = 'tblS5FlammablesAltReleases'

    class Meta:
        db_table = 'tblS5FlammablesAltReleases'
