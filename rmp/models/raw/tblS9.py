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
    FacilityID = CopyFromOneToOneField(
        'tblS1Facilities',
        on_delete=models.PROTECT,
    )
    ER_CommunityPlan = CopyFromBooleanField(
    )
    ER_FacilityPlan = CopyFromBooleanField(
    )
    ER_ResponseActions = CopyFromBooleanField(
    )
    ER_PublicInfoProcedures = CopyFromBooleanField(
    )
    ER_EmergencyHealthCare = CopyFromBooleanField(
    )
    ER_ReviewDate = CopyFromDateTimeField(
        null=True,
    )
    ERTrainingDate = CopyFromDateTimeField(
        null=True,
    )
    CoordinatingAgencyName = CopyFromCharField(
        max_length=250,
        blank=True,
    )
    CoordinatingAgencyPhone = CopyFromCharField(
        source_column='CoordinatingAgencyPhone',
        max_length=10,
        blank=True,
    )
    FR_OSHA1910_38 = CopyFromBooleanField(
    )
    FR_OSHA1910_120 = CopyFromBooleanField(
    )
    FR_SPCC = CopyFromBooleanField(
    )
    FR_RCRA = CopyFromBooleanField(
    )
    FR_OPA90 = CopyFromBooleanField(
    )
    FR_EPCRA = CopyFromBooleanField(
    )
    FR_OtherRegulation = CopyFromCharField(
        max_length=200,
        blank=True,
    )

    class Meta:
        verbose_name = 'Emergency Response Plan'
        verbose_name_plural = 'Emergency Response Plans'
