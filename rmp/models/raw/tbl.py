"""Models for RMP source files with `tbl...` prefix."""
from django.db import models
from rmp.fields import (
    CopyFromBigIntegerField,
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDateTimeField,
    CopyFromDecimalField,
    CopyFromForeignKey,
    CopyFromIntegerField,
    CopyFromOneToOneField,
    CopyFromTextField,
)
from rmp.models import BaseRMPModel


class tblFacility(BaseRMPModel):
    EPAFacilityID = CopyFromBigIntegerField(
        verbose_name='EPA Facility Identifier',
        primary_key=True,
        help_text='Unique identifier for all RMPs submitted by a specific '
                  'facility (assigned by Reporting Center for first-time '
                  'submission). * After this number is assigned to the first '
                  'submission for a facility, subsequent submissions for the '
                  'same facility must include this identifier.'
    )
    FacilityName = CopyFromCharField(
        verbose_name='Facility Name',
        max_length=200,
        help_text='Facility name specific to the site.',
    )
    MarplotID = CopyFromCharField(
        max_length=100,
        blank=True,
        verbose_name='Marplot Identifier',
        help_text='Future link to Marplot',
    )
    CameoID = CopyFromCharField(
        max_length=100,
        blank=True,
        verbose_name='Cameo Identifier',
        help_text='Future Link to CAMEO',
    )
    FacilityID = CopyFromOneToOneField(
        'tblS1Facilities',
        source_column='RMPID',
        db_column='FacilityID',
        on_delete=models.PROTECT,
    )
    FacilityStr1 = CopyFromCharField(
        max_length=35,
        blank=True,
    )
    FacilityStr2 = CopyFromCharField(
        max_length=35,
        blank=True,
    )
    FacilityCity = CopyFromCharField(
        max_length=19,
    )
    FacilityState = CopyFromForeignKey(
        'tlkpStateFIPSCodes',
        db_column='FacilityState',
        on_delete=models.PROTECT,
        max_length=2,
    )
    FacilityZipCode = CopyFromCharField(
        max_length=5,
    )
    Facility4DigitZipExt = CopyFromCharField(
        max_length=4,
        blank=True,
    )
    FacilityCountyFIPS = CopyFromForeignKey(
        'TlkpCountyFIPSCodes',
        db_column='FacilityCountyFIPS',
        on_delete=models.PROTECT,
        blank=True,
    )
    CountOfFacilityID = CopyFromIntegerField(
    )
    FacilityLatDecDegs = CopyFromDecimalField(
        decimal_places=15,
        max_digits=18,
        null=True,
    )
    FacilityLongDecDegs = CopyFromDecimalField(
        decimal_places=15,
        max_digits=18,
        null=True,
    )

    class Meta:
        verbose_name = 'RMP Facility Information'
        verbose_name_plural = 'RMP Facility Information'


class tblExecutiveSummaries(BaseRMPModel):
    ESSeqNum = CopyFromIntegerField(
        verbose_name='Executive Summary Sequence Number',
        help_text='Unique sequence number for the executive summary.',
    )
    FacilityID = CopyFromForeignKey(
        'tblS1Facilities',
        db_column='FacilityID',
        on_delete=models.PROTECT,
        verbose_name='Facility ID',
        help_text='Unique identifier for all RMPs submitted by a specific '
                  'facility (assigned by Reporting Center for first-time '
                  'submission). * After this number is assigned to the first '
                  'submission for a facility, subsequent submissions for the '
                  'same facility must include this identifier.',
    )
    SummaryText = CopyFromTextField(
        verbose_name='Executive Summary',
        blank=True,
        help_text='The Executive Summary includes a brief description of the '
                  "facility's risk management program.",
    )

    source_file = 'tblExecutiveSummaries'

    class Meta:
        db_table = 'tblExecutiveSummaries'


class tblRMPError(BaseRMPModel):
    FacilityID = CopyFromForeignKey(
        'tblS1Facilities',
        db_column='FacilityID',
        on_delete=models.PROTECT,
        verbose_name='Facility ID',
        help_text='Unique identifier for all RMPs submitted by a specific '
                  'facility (assigned by Reporting Center for first-time '
                  'submission). * After this number is assigned to the first '
                  'submission for a facility, subsequent submissions for the '
                  'same facility must include this identifier.',
    )
    SequenceNumber = CopyFromIntegerField(
        verbose_name='Sequence Number',
        help_text='Unique sequence number.',
    )
    ErrorText = CopyFromTextField(
        verbose_name='Error Text',
        help_text='Error message text.',
    )

    class Meta:
        verbose_name = 'RMP ValidationError'
        verbose_name_plural = 'RMP ValidationErrors'


class tblRMPTrack(BaseRMPModel):
    TrackID = CopyFromBigIntegerField(
        primary_key=True,
        verbose_name='Track ID',
        help_text='Unique number used to identify each RMP Tracking record.',

    )
    EPAFacilityID = CopyFromForeignKey(
        'tblFacility',
        db_column='EPAFacilityID',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='EPA Facility ID',
        help_text='Unique identifier for all RMPs submitted by a specific '
                  'facility (assigned by Reporting Center for first-time '
                  'submission). * After this number is assigned to the first '
                  'submission for a facility, subsequent submissions for the '
                  'same facility must include this identifier.',
    )
    ReceiptDate = CopyFromDateTimeField(
        verbose_name='Receipt Date',
        help_text='The date the diskettes or paper submission was received by '
                  'the Records Center.',
    )
    PostmarkDate = CopyFromDateTimeField(
        verbose_name='Postmark Date',
        help_text='The postmark date of the RMP received material.',
    )
    FacilityName1 = CopyFromCharField(
        max_length=50,
        verbose_name='Facility Name 1',
        help_text='The first line of the facility name.',
    )
    FacilityName2 = CopyFromCharField(
        max_length=50,
        blank=True,
        verbose_name='Facility Name 2',
        help_text='The second line of the facility name.',
    )
    FacilityStreet1 = CopyFromCharField(
        max_length=35,
        verbose_name='Facility Street 1',
        help_text='The text which contains the first line of the mailing '
                  'address of the facility.',
    )
    FacilityStreet2 = CopyFromCharField(
        max_length=35,
        blank=True,
        verbose_name='Facility Street 2',
        help_text='The text which contains the second line of the mailing '
                  'address of the facility.',
    )
    FacilityCity = CopyFromCharField(
        max_length=20,
        verbose_name='Facility City',
        help_text='The name of the city in which the facility is located.',
    )
    FacilityState = CopyFromForeignKey(
        'tlkpStateFIPSCodes',
        db_column='FacilityState',
        on_delete=models.PROTECT,
        verbose_name='Facility State',
        help_text='The two-character FIPS abbreviation for the state in which '
                  'the facility is located.',
    )
    FacilityZip = CopyFromCharField(
        max_length=5,
        verbose_name='Facility Zip',
        help_text='The code which represents the Zoning Improvement Plan (ZIP)'
                  ' zone of the facility mailing address.',
    )
    FacilityZip4 = CopyFromCharField(
        max_length=4,
        blank=True,
        verbose_name='Facility Zip4',
        help_text='The code which represents the Zoning Improve Plan (ZIP) '
                  'Geographic Segment of the facility mailing address.',
    )
    DocumentHandle = CopyFromForeignKey(
        'tlkpDocHandle',
        db_column='DocumentHandle',
        on_delete=models.PROTECT,
        blank=True,
        verbose_name='Document Handle',
        help_text='The code which represents the method of handling used for '
                  'the RMP submission.',
    )
    Comments = CopyFromTextField(
        verbose_name='Comments',
        blank=True,
        help_text='The text which contains comments about the RMP submission.',
    )
    DocumentType = CopyFromForeignKey(
        'tlkpDocType',
        db_column='DocumentType',
        on_delete=models.PROTECT,
        blank=True,
        verbose_name='Document Type',
        help_text='The code which represents the type of the document to which'
                  ' the RMP Tracking record applies.',
    )
    RejectionReason = CopyFromForeignKey(
        'tlkpRejectReason',
        db_column='RejectionReason',
        on_delete=models.PROTECT,
        verbose_name='Rejection Reason',
        help_text='The code which represents the reason the RMP submission '
                  'could not be processed.',
    )
    ResolutionDate = CopyFromDateTimeField(
        null=True,
        verbose_name='Resolution Date',
        help_text='The date on which the problems which prevented the RMP from'
                  ' being processed were finally resolved.',
    )
    InsertDate = CopyFromDateTimeField(
        null=True,
    )

    class Meta:
        verbose_name = 'RMP Tracking'
        verbose_name_plural = 'RMP Tracking'
