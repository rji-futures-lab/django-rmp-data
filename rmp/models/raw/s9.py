"""
tblS9EmergencyResponses.csv
"""
from django.db import models
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDateTimeField,
    CopyFromDecimalField,
    CopyFromIntegerField,
    CopyFromForeignKey,
)
from rmp.models.base import BaseRMPModel


class Tbls9Emergencyresponses(BaseRMPModel):
    facilityid = CopyFromForeignKey(
        'Tbls1Facilities',
        on_delete=models.PROTECT,
    )
    er_communityplan = CopyFromBooleanField()
    er_facilityplan = CopyFromBooleanField()
    er_responseactions = CopyFromBooleanField()
    er_publicinfoprocedures = CopyFromBooleanField()
    er_emergencyhealthcare = CopyFromBooleanField()
    er_reviewdate = CopyFromDateTimeField(blank=True)
    ertrainingdate = CopyFromDateTimeField(blank=True)
    coordinatingagencyname = CopyFromCharField(max_length=250, blank=True)
    coordinatingagencyphone = CopyFromCharField(max_length=10, blank=True)
    fr_osha1910_38 = CopyFromBooleanField()
    fr_osha1910_120 = CopyFromBooleanField()
    fr_spcc = CopyFromBooleanField()
    fr_rcra = CopyFromBooleanField()
    fr_opa90 = CopyFromBooleanField()
    fr_epcra = CopyFromBooleanField()
    fr_otherregulation = CopyFromCharField(max_length=200, blank=True)

    source_file = 'tblS9EmergencyResponses'

    class Meta:
        db_table = 'tblS9EmergencyResponses'
