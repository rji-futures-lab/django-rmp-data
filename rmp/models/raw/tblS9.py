"""Models for raw RMP source files with `tblS9...` prefix."""
from django.db import models
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDateTimeField,
    CopyFromDecimalField,
    CopyFromForeignKey,
    CopyFromIntegerField,
    CopyFromOneToOneField,
)
from rmp.models.base import BaseRMPModel


class tblS9EmergencyResponses(BaseRMPModel):
    facilityid = CopyFromOneToOneField(
        'tblS1Facilities',
        source_column='FacilityID',
        on_delete=models.PROTECT,
    )
    er_communityplan = CopyFromBooleanField(
        source_column='ER_CommunityPlan',
    )
    er_facilityplan = CopyFromBooleanField(
        source_column='ER_FacilityPlan',
    )
    er_responseactions = CopyFromBooleanField(
        source_column='ER_ResponseActions',
    )
    er_publicinfoprocedures = CopyFromBooleanField(
        source_column='ER_PublicInfoProcedures',
    )
    er_emergencyhealthcare = CopyFromBooleanField(
        source_column='ER_EmergencyHealthCare',
    )
    er_reviewdate = CopyFromDateTimeField(
        source_column='ER_ReviewDate',
        null=True,
    )
    ertrainingdate = CopyFromDateTimeField(
        source_column='ERTrainingDate',
        null=True,
    )
    coordinatingagencyname = CopyFromCharField(
        source_column='CoordinatingAgencyName',
        max_length=250,
        blank=True,
    )
    coordinatingagencyphone = CopyFromCharField(
        source_column='CoordinatingAgencyPhone',
        max_length=10, 
        blank=True,
    )
    fr_osha1910_38 = CopyFromBooleanField(
        source_column='FR_OSHA1910_38',
    )
    fr_osha1910_120 = CopyFromBooleanField(
        source_column='FR_OSHA1910_120',
    )
    fr_spcc = CopyFromBooleanField(
        source_column='FR_SPCC',
    )
    fr_rcra = CopyFromBooleanField(
        source_column='FR_RCRA',
    )
    fr_opa90 = CopyFromBooleanField(
        source_column='FR_OPA90',
    )
    fr_epcra = CopyFromBooleanField(
        source_column='FR_EPCRA',
    )
    fr_otherregulation = CopyFromCharField(
        source_column='FR_OtherRegulation',
        max_length=200,
        blank=True,
    )

    class Meta:
        verbose_name = 'Emergency Response Plan'
        verbose_name_plural = 'Emergency Response Plans'
