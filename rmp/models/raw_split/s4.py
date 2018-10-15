"""
tblS4FlammablesWorstCase.csv
"""

from django.db import models
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDecimalField,
    CopyFromIntegerField,
    CopyFromForeignKey,
)
from .base import BaseRMPModel

class Tbls4Flammablesworstcase(BaseRMPModel):
    flammableid = models.CopyFromIntegerField(primary_key=True)
    processchemicalid = models.CopyFromForeignKey(
        Tbls1Processchemicals,
        on_delete=models.PROTECT
    )
    analyticalbasis = models.CopyFromCharField(max_length=255, blank=True)
    quantityreleased = models.CopyFromDecimalField(max_digits=6, decimal_places=2, blank=True)
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
    pm_blastwalls = models.CopyFromBooleanField()
    pm_othertype = models.CopyFromCharField(max_length=200, blank=True)
    ptrgraphic = models.CopyFromBooleanField(max_length=12, blank=True)
    cbi_flag = models.CopyFromBooleanField()

    source_file = 'tblS4FlammablesWorstCase'

    class Meta:
        db_table = 'tblS4FlammablesWorstCase'
