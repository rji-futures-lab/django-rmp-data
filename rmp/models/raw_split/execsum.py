"""
tblExecutiveSummaries
execSumLen?
"""

class Tblexecutivesummaries(BaseRMPModel):
    esseqnum = models.CopyFromIntegerField(primary_key=True) # Field name made lowercase.
    facilityid = models.CopyFromForeignKey()  # Field name made lowercase.
    summarytext = models.CopyFromTextField() # Field name made lowercase.

    source_file = 'tblExecutiveSummaries'

    class Meta:
        db_table = 'tblExecutiveSummaries'
