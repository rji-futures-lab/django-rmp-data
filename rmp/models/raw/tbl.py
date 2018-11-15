"""Models for RMP source files with `tbl...` prefix."""
from django.db import models
from rmp.fields import (
    CopyFromBigIntegerField,
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDateTimeField,
    CopyFromDecimalField,
    CopyFromIntegerField,
    CopyFromForeignKey,
    CopyFromTextField,
)
from rmp.models import BaseRMPModel


class tblFacility(BaseRMPModel):
    epafacilityid = CopyFromBigIntegerField(
        source_column='EPAFacilityID',
        verbose_name='EPA Facility Identifier',
        primary_key=True,
        help_text='Unique identifier for all RMPs submitted by a specific '
                  'facility (assigned by Reporting Center for first-time '
                  'submission). * After this number is assigned to the first '
                  'submission for a facility, subsequent submissions for the '
                  'same facility must include this identifier.'
    )
    facilityname = CopyFromCharField(
        source_column='FacilityName',
        verbose_name='Facility Name',
        max_length=200,
        help_text='Facility name specific to the site.',
    )
    marplotid = CopyFromCharField(
        source_column='MarplotID',
        max_length=100,
        blank=True,
        verbose_name='Marplot Identifier',
        help_text='Future link to Marplot',
    ) 
    cameoid = CopyFromCharField(
        source_column='CameoID',
        max_length=100,
        blank=True,
        verbose_name='Cameo Identifier',
        help_text='Future Link to CAMEO',
    )
    rmpid = CopyFromIntegerField(# <--ForeignKey to what????
        source_column='RMPID',
    ) 
    facilitystr1 = CopyFromCharField(
        source_column='FacilityStr1',
        max_length=35,
        blank=True,
    )
    facilitystr2 = CopyFromCharField(
        source_column='FacilityStr2',
        max_length=35,
        blank=True,
    )
    facilitycity = CopyFromCharField(
        source_column='FacilityCity',
        max_length=19,
    )
    facilitystate = CopyFromForeignKey(
        'tlkpStateFIPSCodes',
        on_delete=models.PROTECT,
        source_column='FacilityState',
        max_length=2,
    )
    facilityzipcode = CopyFromCharField(
        source_column='FacilityZipCode',
        max_length=5,
    )
    facility4digitzipext = CopyFromCharField(
        source_column='Facility4DigitZipExt',
        max_length=4,
        blank=True,
    )
    facilitycountyfips = CopyFromForeignKey(
        'TlkpCountyFIPSCodes',
        on_delete=models.PROTECT,
        source_column='FacilityCountyFIPS',
        blank=True,
    )
    countoffacilityid = CopyFromIntegerField(
        source_column='CountOfFacilityID',
    )
    facilitylatdecdegs = CopyFromDecimalField(
        source_column='FacilityLatDecDegs',
        decimal_places=15,
        max_digits=18,
        null=True,
    )
    facilitylongdecdegs = CopyFromDecimalField(
        source_column='FacilityLongDecDegs',
        decimal_places=15,
        max_digits=18,
        null=True,
    )

    class Meta:
        verbose_name = 'RMP Facility Information'
        verbose_name_plural = 'RMP Facility Information'


class tblExecutiveSummaries(BaseRMPModel):
    esseqnum = CopyFromIntegerField(
        source_column='ESSeqNum',
        verbose_name='Executive Summary Sequence Number',
        help_text='Unique sequence number for the executive summary.',
    )
    facilityid = CopyFromForeignKey(
        'Tblfacility',
        on_delete=models.PROTECT,
        source_column='FacilityID',
        verbose_name='Facility ID',
        help_text='Unique identifier for all RMPs submitted by a specific '
                  'facility (assigned by Reporting Center for first-time '
                  'submission). * After this number is assigned to the first '
                  'submission for a facility, subsequent submissions for the '
                  'same facility must include this identifier.',
    )
    summarytext = CopyFromTextField(
        source_column='SummaryText',
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
        'tblFacility',
        on_delete=models.PROTECT,
        source_column='FacilityID',
        verbose_name='Facility ID',
        help_text='Unique identifier for all RMPs submitted by a specific '
                  'facility (assigned by Reporting Center for first-time '
                  'submission). * After this number is assigned to the first '
                  'submission for a facility, subsequent submissions for the '
                  'same facility must include this identifier.',
    )
    SequenceNumber = CopyFromIntegerField(
        source_column='SequenceNumber',
        verbose_name='Sequence Number',
        help_text='Unique sequence number.',
    )
    ErrorText = CopyFromTextField(
        source_column='ErrorText',
        verbose_name='Error Text',
        help_text='Error message text.',
    )

    class Meta:
        verbose_name = 'RMP ValidationError'
        verbose_name_plural = 'RMP ValidationErrors'


class tblRMPTrack(BaseRMPModel):
    trackid = CopyFromBigIntegerField(
        source_column='TrackID',
        primary_key=True,
        verbose_name='Track ID',
        help_text='Unique number used to identify each RMP Tracking record.',

    )
    epafacilityid = CopyFromForeignKey(
        'tblFacility',
        on_delete=models.PROTECT,
        source_column='EPAFacilityID',
        db_column='epafacilityid',
        null=True,
        verbose_name='EPA Facility ID',
        help_text='Unique identifier for all RMPs submitted by a specific '
                  'facility (assigned by Reporting Center for first-time '
                  'submission). * After this number is assigned to the first '
                  'submission for a facility, subsequent submissions for the '
                  'same facility must include this identifier.',
    )
    receiptdate = CopyFromDateTimeField(
        source_column='ReceiptDate',
        verbose_name='Receipt Date',
        help_text='The date the diskettes or paper submission was received by '
                  'the Records Center.',
    )
    postmarkdate = CopyFromDateTimeField(
        source_column='PostmarkDate',
        verbose_name='Postmark Date',
        help_text='The postmark date of the RMP received material.',
    )
    facilityname1 = CopyFromCharField(
        source_column='FacilityName1',
        max_length=50,
        verbose_name='Facility Name 1',
        help_text='The first line of the facility name.',
    )
    facilityname2 = CopyFromCharField(
        source_column='FacilityName2',
        max_length=50,
        blank=True,
        verbose_name='Facility Name 2',
        help_text='The second line of the facility name.',
    )
    facilitystreet1 = CopyFromCharField(
        source_column='FacilityStreet1',
        max_length=35,
        verbose_name='Facility Street 1',
        help_text='The text which contains the first line of the mailing '
                  'address of the facility.',
    )
    facilitystreet2 = CopyFromCharField(
        source_column='FacilityStreet2',
        max_length=35,
        blank=True,
        verbose_name='Facility Street 2',
        help_text='The text which contains the second line of the mailing '
                  'address of the facility.',
    )
    facilitycity = CopyFromCharField(
        source_column='FacilityCity',
        max_length=20,
        verbose_name='Facility City',
        help_text='The name of the city in which the facility is located.',
    )
    facilitystate = CopyFromForeignKey(
        'tlkpStateFIPSCodes',
        on_delete=models.PROTECT,
        source_column='FacilityState',
        verbose_name='Facility State',
        help_text='The two-character FIPS abbreviation for the state in which '
                  'the facility is located.',
    )
    facilityzip = CopyFromCharField(
        source_column='FacilityZip',
        max_length=5,
        verbose_name='Facility Zip',
        help_text='The code which represents the Zoning Improvement Plan (ZIP)'
                  ' zone of the facility mailing address.',
    )
    facilityzip4 = CopyFromCharField(
        source_column='FacilityZip4',
        max_length=4,
        blank=True,
        verbose_name='Facility Zip4',
        help_text='The code which represents the Zoning Improve Plan (ZIP) '
                  'Geographic Segment of the facility mailing address.',
    )
    documenthandle = CopyFromForeignKey(
        'tlkpDocHandle',
        on_delete=models.PROTECT,
        blank=True,
        source_column='DocumentHandle',
        verbose_name='Document Handle',
        help_text='The code which represents the method of handling used for '
                  'the RMP submission.',
    )
    comments = CopyFromTextField(
        source_column='Comments',
        verbose_name='Comments',
        blank=True,
        help_text='The text which contains comments about the RMP submission.',
    )
    documenttype = CopyFromForeignKey(
        'tlkpDocType',
        on_delete=models.PROTECT,
        blank=True,
        source_column='DocumentType',
        verbose_name='Document Type',
        help_text='The code which represents the type of the document to which'
                  ' the RMP Tracking record applies.',
    )
    rejectionreason = CopyFromForeignKey(
        'tlkpRejectReason',
        on_delete=models.PROTECT,
        source_column='RejectionReason',
        verbose_name='Rejection Reason',
        help_text='The code which represents the reason the RMP submission '
                  'could not be processed.',
    )
    resolutiondate = CopyFromDateTimeField(
        source_column='ResolutionDate',
        null=True,
        verbose_name='Resolution Date',
        help_text='The date on which the problems which prevented the RMP from'
                  ' being processed were finally resolved.',
    )
    insertdate = CopyFromDateTimeField(
        source_column='InsertDate',
        null=True,
    )

    class Meta:
        verbose_name = 'RMP Tracking'
        verbose_name_plural = 'RMP Tracking'
