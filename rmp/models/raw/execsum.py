"""
tblExecutiveSummaries
execSumLen?
"""
from django.db import models
from rmp.models import BaseRMPModel
from rmp.fields import (
    CopyFromTextField,
    CopyFromIntegerField,
    CopyFromForeignKey,
)

class Tblexecutivesummaries(BaseRMPModel):
    esseqnum = CopyFromIntegerField(
        primary_key=True,
    )
    facilityid = CopyFromForeignKey(
        'Tblfacility',
        on_delete=models.PROTECT,
    )
    summarytext = CopyFromTextField()

    source_file = 'tblExecutiveSummaries'

    class Meta:
        db_table = 'tblExecutiveSummaries'
