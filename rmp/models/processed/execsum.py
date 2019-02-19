"""
Models for processed RMP data.
"""
import os
from django.conf import settings
from django.db import models
from django.db.models import F, Max, OuterRef, Subquery, Sum, Count, Case, When, Value
from rmp.fields import (
    CopyFromBigIntegerField,
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDateField,
    CopyFromDateTimeField,
    CopyFromDecimalField,
    CopyFromForeignKey,
    CopyFromIntegerField,
    CopyFromOneToOneField,
    CopyFromTextField,
    CopyFromFloatField,
)
from rmp.models import raw as raw_models
from rmp.models.base import BaseRMPModel

class ExecutiveSummary(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='rmp_id',
    )
    summary_text = CopyFromTextField(
        source_column='execsum',
        blank=True,
    )

    @classmethod
    def get_transform_queryset(self):
        qs = raw_models.tblExecutiveSummaries.objects.filter(
            ESSeqNum=Subquery(
                raw_models.tblExecutiveSummaries.objects.filter(
                    FacilityID=OuterRef('FacilityID'),
                ).values('FacilityID_id').annotate(
                    max_seqnum=Max('ESSeqNum')
                ).values('max_seqnum')[:1]
            )
        ).annotate(
            rmp_id=F('FacilityID'),
            execsum=F('SummaryText')
        )

        return qs


class ExecutiveSummaryLength(BaseRMPModel):
    rmp_id = CopyFromIntegerField(
        primary_key=True,
    )
    byte_count = CopyFromIntegerField()
    suspect_count = CopyFromIntegerField()
    line_count = CopyFromIntegerField()
    edited_yn = CopyFromCharField(max_length=1)

    source_file = 'rmp_exec_sum_len'
