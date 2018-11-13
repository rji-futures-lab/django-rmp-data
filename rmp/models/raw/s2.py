"""
tblS2ToxicsWorstCase.csv
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


class Tbls2Toxicsworstcase(BaseRMPModel):
    toxicid = CopyFromIntegerField(primary_key=True)
    processchemicalid = CopyFromForeignKey(
        'Tbls1Processchemicals',
        on_delete=models.PROTECT
    )
    percentweight = CopyFromDecimalField(max_digits=4, decimal_places=1, blank=True)
    physicalstate = CopyFromCharField(max_length=1, blank=True)
    analyticalbasis = CopyFromCharField(max_length=255, blank=True)
    scenario = CopyFromBooleanField(blank=True)
    quantityreleased = CopyFromDecimalField(max_digits=6, decimal_places=2, blank=True)
    releaseduration = CopyFromDecimalField(max_digits=6, decimal_places=2, blank=True)
    releaserate = CopyFromDecimalField(max_digits=4, decimal_places=1, blank=True)
    windspeed = CopyFromDecimalField(max_digits=4, decimal_places=1, blank=True)
    stabilityclass = CopyFromCharField(max_length=1, blank=True)
    topography = CopyFromCharField(max_length=1, blank=True)
    endpoint_distance = CopyFromDecimalField(max_digits=5, decimal_places=1)
    residentialpopulation = CopyFromBooleanField(blank=True)
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
    pm_enclosures = CopyFromBooleanField()
    pm_berms = CopyFromBooleanField()
    pm_drains = CopyFromBooleanField()
    pm_sumps = CopyFromBooleanField()
    pm_othertype = CopyFromCharField(max_length=200, blank=True)
    ptrgraphic = CopyFromBooleanField(max_length=12, blank=True)
    cbi_flag = CopyFromBooleanField()

    source_file = 'tblS2ToxicsWorstCase'

    class Meta:
        db_table = 'tblS2ToxicsWorstCase'
