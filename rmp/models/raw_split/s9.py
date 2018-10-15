"""
tblS9EmergencyResponses.csv
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

class Tbls9Emergencyresponses(BaseRMPModel):
    facilityid = models.CopyFromForeignKey(
        Tbls1Facilities,
        on_delete=models.PROTECT,
    )
    er_communityplan = models.CopyFromBooleanField()
    er_facilityplan = models.CopyFromBooleanField()
    er_responseactions = models.CopyFromBooleanField()
    er_publicinfoprocedures = models.CopyFromBooleanField()
    er_emergencyhealthcare = models.CopyFromBooleanField()
    er_reviewdate = models.CopyFromDateTime(blank=True)
    ertrainingdate = models.CopyFromDateTime(blank=True)
    coordinatingagencyname = models.CopyFromCharField(max_length=250, blank=True)
    coordinatingagencyphone = models.CopyFromCharField(max_length=10, blank=True)
    fr_osha1910_38 = models.CopyFromBooleanField()
    fr_osha1910_120 = models.CopyFromBooleanField()
    fr_spcc = models.CopyFromBooleanField()
    fr_rcra = models.CopyFromBooleanField()
    fr_opa90 = models.CopyFromBooleanField()
    fr_epcra = models.CopyFromBooleanField()
    fr_otherregulation = models.CopyFromCharField(max_length=200, blank=True)

    source_file = 'tblS9EmergencyResponses'

    class Meta:
        db_table = 'tblS9EmergencyResponses'
