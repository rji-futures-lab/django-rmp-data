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
from .base import BaseRMPModelx

class Tbls5Flammablesaltreleases(BaseRMPModel):
    flammableid = models.CopyFromIntegerField(primary_key=True)
    processchemicalid = models.CopyFromForeignKey(
        Tbls1Processchemicals,
        on_delete=models.PROTECT,
    )
    analyticalbasis = models.CopyFromCharField(max_length=255, blank=True)
    scenario = models.CopyFromCharField(max_length=200)
    quantityreleased = models.CopyFromDecimalField(max_digits=5, decimal_places=2)
    endpointused = models.CopyFromCharField(max_length=30, blank=True)
    lfl_value = models.CopyFromDecimalField(max_digits=5, decimal_places=1)
    endpoint_distance = models.CopyFromDecimalField(max_digits=5, decimal_places=1)
    residentialpopulation = models.CopyFromCharField(max_length=9, blank=True)
    pr_schools = models.CopyFromBooleanField()
    pr_residences = models.CopyFromBooleanField()
    pr_hospitals = models.CopyFromBooleanField()
    pr_prisons = models.CopyFromBooleanField()
    pr_publicrecreation = models.CopyFromBooleanField()
    pr_comm_ind = models.CopyFromBooleanField()
    pr_othertype = models.CopyFromCharField(max_length=200, blank=True)
    er_natlstateparks = models.CopyFromBooleanField()
    er_wildlifesactuary = models.CopyFromBooleanField()
    er_fedwilderness = models.CopyFromBooleanField()
    er_othertype = models.CopyFromCharField(max_length=200, blank=True)
    pm_dikes = models.CopyFromBooleanField()
    pm_firewalls = models.CopyFromBooleanField()
    pm_blastwalls = models.CopyFromBooleanField()
    pm_enclosures = models.CopyFromBooleanField()
    pm_othertype = models.CopyFromCharField(max_length=200, blank=True)
    am_sprinklersystems = models.CopyFromBooleanField()
    am_delugesystems = models.CopyFromBooleanField()
    am_watercurtain = models.CopyFromBooleanField()
    am_excessflowvalve = models.CopyFromBooleanField()
    am_othertype = models.CopyFromCharField(max_length=200, blank=True)
    ptrgraphic = models.CopyFromCharField(max_length=12, blank=True)
    cbi_flag = models.CopyFromBooleanField()

    source_file = 'tblS5FlammablesAltReleases'

    class Meta:
        db_table = 'tblS5FlammablesAltReleases'
