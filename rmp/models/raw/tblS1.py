"""Models for raw RMP source files with `tblS1...` prefix."""
from django.db import models
from rmp.fields import (
    CopyFromBigIntegerField,
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDateTimeField,
    CopyFromDecimalField,
    CopyFromEmailField,
    CopyFromForeignKey,
    CopyFromIntegerField,
    CopyFromURLField,
)
from rmp.models import BaseRMPModel


class tblS1Facilities(BaseRMPModel):
    FacilityID = CopyFromIntegerField(
        primary_key=True,
        verbose_name='RMP Identifier',
        help_text='Unique identifier for all RMPs submitted by a specific '
                  'facility (assigned by Reporting Center for first-time '
                  'submission). * After this number is assigned to the first '
                  'submission for a facility, subsequent submissions for the '
                  'same facility must include this identifier.',
    )
    FacilityName = CopyFromCharField(
        max_length=255,
        blank=True,
        verbose_name='1.1.a Facility Name',
        help_text='Facility name specific to the site.',
    )
    FacilityStr1 = CopyFromCharField(
        max_length=35,
        blank=True,
        verbose_name='1.5.a Facility Street - Line 1',
        help_text='Facility Street - Line 1 using local street and road '
                  'designations. No post office box numbers or rural route '
                  'numbers. This is not the mailing address.',
    )
    FacilityStr2 = CopyFromCharField(
        max_length=35,
        blank=True,
        verbose_name='1.5.b Facility Street - Line 2',
        help_text='Facility Street Address - Line 2',
    )
    FacilityCity = CopyFromCharField(
        max_length=19,
        verbose_name='1.5.c Facility City',
        help_text='The name of the city, town, or village where the '
                  'facility is located.',
    )
    FacilityState = CopyFromForeignKey(
        'tlkpStateFIPSCodes',
        on_delete=models.PROTECT,
        related_name='facilitystate',
        verbose_name='1.5.d Facility State',
        help_text='The U.S. Postal Service abbreviation for the state in '
                  'which the facility is located.',
    )
    FacilityZipCode = CopyFromCharField(
        max_length=5,
        verbose_name='1.5.e Facility ZIP Code',
        help_text='The Zoning Improvement Plan (ZIP) Code assigned to the '
                  'facility by the U.S. Postal Service which represents a '
                  'geographic area that facilitates mail delivery.',
    )
    Facility4DigitZipExt = CopyFromCharField(
        max_length=4,
        blank=True,
        verbose_name='1.5.e Facility ZIP Extention',
        help_text='The four-digit extension code that represents the '
                  'geographic segment that is a sub-unit of the ZIP Code and '
                  'further refines the exact location of the facility.',
    )
    FacilityCountyFIPS = CopyFromForeignKey(
        'tlkpCountyFIPSCodes',
        on_delete=models.PROTECT,
        blank=True,
        verbose_name='1.5.f Facility County',
        help_text='Federal Information Processing Standard (FIPS) code for '
                  'county in which the facility is located.',
    )
    LEPC = CopyFromCharField(
        max_length=30,
        blank=True,
        verbose_name='1.10 LEPC',
        help_text='Local Emergency Planning Committee (LEPC) associated with '
                  'the facility county. For LEPC information refer to the '
                  'LEPC/SERC Net Web site at http://www.RTK.NET:80/lepc. Must '
                  'cover all or part of the Facility County.',
    )
    FacilityLatDecDegs = CopyFromDecimalField(
        max_digits=9,
        decimal_places=7,
        verbose_name='1.5.g Facility Latitude (Decimal Degrees)',
        help_text='Facility Latitude in decimal degrees.',
    )
    FacilityLongDecDegs = CopyFromDecimalField(
        max_digits=10,
        decimal_places=7,
        verbose_name='1.5.h Facility Longitude (Decimal Degrees)',
        help_text='Facility Longitude in decimal degrees.',
    )
    ValidLatLongFlag = CopyFromCharField(
        max_length=1,
        blank=True,
        source_column='ValidLatLongFlag',
        verbose_name='Valid Lat/Long Flag',
        help_text='Flag used to indicate whether the Latitude/Longitude is '
                  'valid.',
    )
    LatLongMethod = CopyFromForeignKey(
        'tlkpLatLongMethods',
        to_field='method_code',
        on_delete=models.PROTECT,
        blank=True,
        source_column='LatLongMethod',
        verbose_name='1.5.i Lat/Long Method',
        help_text='Code representing method used to obtain latitude or '
                  'longitude data. Codes can be obtained from Method '
                  'Accuracy Description (MAD) Version 6.1 Information Coding '
                  'Standards as implemented in Envirofacts Locational '
                  'Reference Tables (EF LRT). '
                  'http://www.epa.gov/enviro/html/lrt/lrt_over.html',
    )
    LatLongDescription = CopyFromCharField(
        max_length=2,
        blank=True,
        verbose_name='1.5.j Lat/Long Description',
        help_text='Code for the physical place corresponding to the coordinate.'
                  ' Codes can be obtained from MAD Version 6.1 Standard as '
                  'implemented in Envirofacts Locational Reference Tables (EF '
                  'LRT). http://www.epa.gov/enviro/html/lrt/lrt_over.html',
    )
    FacilityURL = CopyFromURLField(
        max_length=100,
        blank=True,
        verbose_name='1.9.c Facility or Parent Company WWW Homepage Address',
        help_text='Facility or Parent Company homepage web address.',
    )
    FacilityPhoneNumber = CopyFromCharField(
        max_length=10,
        blank=True,
        verbose_name='1.9.b Facility Public Contact Phone Number',
        help_text='Facility phone number for public inquiries to contact '
                  'owner, 112(r) person responsible, etc.',
    )
    FacilityEmailAddress = CopyFromEmailField(
        max_length=100,
        blank=True,
        verbose_name='1.9.a Facility or Parent Company E-mail Address',
        help_text='The text that represents the electronic mail (email) '
                  'address for the facility or parent company.',
    )
    FacilityDUNS = CopyFromCharField(
        max_length=9,
        verbose_name='1.4.a Facility DUNS',
        help_text='The Data Universal Numbering System (DUNS) number assigned '
                  'by Dun & Bradstreet to the facility.',
    )
    ParentCompanyName = CopyFromCharField(
        max_length=250,
        blank=True,
        verbose_name='1.1.b Parent Company #1 Name',
        help_text='First Parent Company Name.',
    )
    Company2Name = CopyFromCharField(
        max_length=50,
        blank=True,
        verbose_name='1.1.c Parent Company #2 Name',
        help_text='Second Parent Company name for joint ventures.',
    )
    CompanyDUNS = CopyFromCharField(
        max_length=9,
        verbose_name='1.4.b Parent Company #1 DUNS',
        help_text='The DUNS Number assigned by Dun & Bradstreet to the parent '
                  'of the company of interest.',
    )
    Company2DUNS = CopyFromCharField(
        max_length=9,
        verbose_name='1.4.c Parent Company #2 DUNS',
        help_text='If your facility is owned by a joint venture, this is the '
                  'DUNS Number assigned by Dun & Bradstreet to the second '
                  'parent company.',
    )
    OperatorName = CopyFromCharField(
        max_length=250,
        blank=True,
        verbose_name='1.6.a Owner/Operator Name',
        help_text='Name of the person or entity that owns or operates the '
                  'facility.',
    )
    OperatorPhone = CopyFromCharField(
        max_length=10,
        blank=True,
        verbose_name='1.6.b Owner/Operator Phone',
        help_text='Phone number for the Owner or Operator.',
    )
    OperatorStr1 = CopyFromCharField(
        max_length=35,
        blank=True,
        verbose_name='1.6.c Owner/Operator Street - Line 1',
        help_text='Line 1 of the business street mailing address for the '
                  'Owner or Operator.',
    )
    OperatorStr2 = CopyFromCharField(
        max_length=35,
        blank=True,
        verbose_name='1.6.d Owner/Operator Street - Line 2',
        help_text='Line 2 of the business street mailing address for the '
                  'Owner or Operator.',
    )
    OperatorCity = CopyFromCharField(
        max_length=19,
        blank=True,
        verbose_name='1.6.e Owner/Operator City',
        help_text='City for the business mailing address for the Owner or '
                  'Operator.',
    )
    OperatorStateFIPS = CopyFromForeignKey(
        'tlkpStateFIPSCodes',
        on_delete=models.PROTECT,
        blank=True,
        verbose_name='1.6.f Owner/Operator State',
        help_text='The U.S. Postal Service state abbreviation for the address '
                  'of the Owner or Operator.',
    )
    OperatorZipCode = CopyFromCharField(
        max_length=5,
        blank=True,
        verbose_name='1.6.g Owner/Operator ZIP Code',
        help_text='ZIP Code for the business mailing address of the Owner or '
                  'Operator.',
    )
    OperatorZipCodeExt = CopyFromCharField(
        max_length=4,
        blank=True,
        verbose_name='1.6.g Owner/Operator ZIP four-digit extention code',
        help_text='The four-digit extension code that represents the '
                  'geographic segment that is a subunit of the ZIP Code and '
                  'further refines the business mailing address of the Owner '
                  'or Operator.',
    )
    RMPContact = CopyFromCharField(
        max_length=35,
        blank=True,
        verbose_name='1.7.a Name of Person Responsible for RMP Implementaion',
        help_text='Person or position responsible for RMP implementation '
                  '(40 CFR Part 68).',
    )
    RMPTitle = CopyFromCharField(
        max_length=250,
        blank=True,
        verbose_name='1.7.b Title/Position of Person Responsible for RMP '
                     'Implementaion',
        help_text='Title of person or position responsible for RMP '
                  'implementation (40 CFR Part 68).',
    )
    EmergencyContactName = CopyFromCharField(
        max_length=250,
        blank=True,
        verbose_name='1.8.a Emergency Contact Name',
        help_text='Name of person designated as the emergency contact for the '
                  'facility.',
    )
    EmergencyContactTitle = CopyFromCharField(
        max_length=35,
        blank=True,
        verbose_name='1.8.b Emergency Contact Title',
        help_text='Title or job classification of the emergency contact.',
    )
    EmergencyContactPhone = CopyFromCharField(
        max_length=10,
        blank=True,
        verbose_name='1.8.c Emergency Contact Phone',
        help_text='Phone number where the emergency contact can be reached '
                  'during normal working hours.',
    )
    Phone24 = CopyFromCharField(
        max_length=10,
        blank=True,
        verbose_name='1.8.d 24-Hour Phone',
        help_text='Number where emergency contact can be reached during '
                  'non-working hours, such as a beeper number.',
    )
    EmergencyContactExt_PIN = CopyFromCharField(
        max_length=10,
        blank=True,
        verbose_name='1.8.e 24-Hour Phone Extention/PIN',
        help_text='Phone extension or pager number for the 24-Hour Phone.',
    )
    FTE = CopyFromIntegerField(
        null=True,
        verbose_name='1.11 Number of Full Time Employees (FTEs)',
        help_text='Number of full-time equivalent employees.',
    )
    OtherEPAFacilityID = CopyFromCharField(
        max_length=15,
        null=True,
        verbose_name='1.3 Other EPA Systems Program Facility Identifier',
        help_text='The unique identification number assigned to a facility by '
                  'the Facility Index System (FINDS) (or if not known, the '
                  'Resource Conservation and Recovery Act (RCRA), Emergency '
                  'Planning and Community Right-to-Know Act (EPCRA), TRI, or '
                  'other EPA facility identifier).',
    )
    EPAFacilityID = CopyFromForeignKey(
        'tblFacility',
        on_delete=models.PROTECT,
        verbose_name='1.2 EPA Facility Identifier',
        help_text='1.2 EPA Facility Identifier',
    )
    OSHA_PSM = CopyFromBooleanField(
        verbose_name='1.12.a Covered by: OSHA PSM',
        help_text='Occupational Safety and Health Act (OSHA) Process Safety '
                  'Management (PSM) Standard. Question covers all processes '
                  'at the facility; if any process at the facility is '
                  'subject to OSHA PSM, must answer “Y” even if the PSM '
                  'process is not covered by this Rule.',
        )
    EPCRA_302 = CopyFromBooleanField(
        verbose_name='1.12.b Covered by: EPCRA 302',
        help_text='EPCRA Section 302 pertains to the Extremely Hazardous '
                  'Substances list. Any facility with a toxic regulated '
                  'substance above the threshold quantity in a process is '
                  'subject to EPCRA 302. If the facility is covered for only '
                  'flammable regulated substances, the facility is not '
                  'subject to 40 CFR 355 for those substances, although the '
                  'facility may be for toxic substances not affected by this '
                  'Rule.',
    )
    CAA_TitleV = CopyFromBooleanField(
        verbose_name='1.12.c CAA Title V',
        help_text='Indicate if your facility has a CAA Title V Operating '
                  'Permit with “Y.” CAA Title V Air Operating Permit ID '
                  'Title V (Part 70) of the Clean Air Act (40CFR70) '
                  'requires major sources of air pollution to obtain '
                  'permits.',
    )
    ClearAirOpPermitID = CopyFromCharField(
        max_length=15,
        null=True,
        verbose_name='1.12.d Air Operating Permit ID',
        help_text='Unique identifier for a CAA Title V Air Operating Permit '
                  'or state equivalent ID.',
    )
    SafetyInspectionDate = CopyFromDateTimeField(
        null=True,
        verbose_name='1.12.d Air Operating Permit ID',
        help_text='Unique identifier for a CAA Title V Air Operating Permit '
                  'or state equivalent ID.',
    )
    SafetyInspectionBy = CopyFromCharField(
        max_length=50,
        blank=True,
        verbose_name='1.15 Last Safety Inspection Performed by:',
        help_text='A designation representing the external agency that '
                  'performed the last safety inspection. One or more of the '
                  'following is expected: OSHA State OSHA EPA State EPA Fire '
                  'Department Never had a safety inspection Other',
    )
    OSHARanking = CopyFromBooleanField(
        verbose_name='1.13 OSH Star or Merit Ranking',
        help_text="A stationary source with a Star or Merit ranking under "
                  "OSHA's voluntary protection program shall be exempt from "
                  "audits under paragraph (b)(2) and (b)(7) of [Section 68.220"
                  " - audits].",
    )
    PredictiveFilingFlag = CopyFromBooleanField(
        verbose_name='Predictive Filing Flag',
        help_text="An indication that the submitter is using Predictive "
                  "Filing for the facility's RMP.",
    )
    SubmissionType = CopyFromCharField(
        max_length=1,
        blank=True,
        verbose_name='Submission Type',
        help_text='Submission Type “F” - First-time submission “R” - '
                  'Resubmission “C” - Correction of existing RMP',
    )
    RMPDescription = CopyFromCharField(
        max_length=50,
        blank=True,
        verbose_name='RMP Description',
        help_text='RMP Description is an optional description for the whole '
                  'RMP. RMP Description is not accessible to RMP*Info on the '
                  'Web.',
    )
    NoAccidents = CopyFromBooleanField(
        verbose_name='No Accidents Flag',
        help_text='Optional Flag to Indicate whether there are any accidents '
                  'to report.',
    )
    ForeignStateProv = CopyFromCharField(
        max_length=35,
        blank=True,
        verbose_name='1.6.f Foreign State or Province',
        help_text='If the Owner or Operator (reported in 1.6.a) has an '
                  'address outside the USA as his or her primary mailing '
                  'address, enter the name of the foreign state or province. '
                  'If the primary address is in the USA, or if there is no '
                  'state or province in the foreign mailing address, leave '
                  'this field blank.',
    )
    ForeignZipCode = CopyFromCharField(
        max_length=14,
        blank=True,
        verbose_name='',
        help_text='',
    )
    ForeignCountry = CopyFromForeignKey(
        'tlkpForeignCountry',
        on_delete=models.PROTECT,
        related_name='foreigncountry',
        blank=True,
        verbose_name='',
        help_text='',
    )
    CBI_Flag = CopyFromBooleanField(
        verbose_name='',
        help_text='',
    )
    CompletionCheckDate = CopyFromDateTimeField(
        verbose_name='',
        help_text='',
    )
    ErrorReportDate = CopyFromDateTimeField(
        null=True,
        verbose_name='',
        help_text='',
    )
    ReceiptDate = CopyFromCharField(
        max_length=25,
        verbose_name='',
        help_text='',
    )
    GraphicsIndicator = CopyFromBooleanField(
        verbose_name='',
        help_text='',
    )
    AttachmentsIndicator = CopyFromBooleanField(
        verbose_name='',
        help_text='',
    )
    CertificationReceivedFlag = CopyFromBooleanField(
        verbose_name='',
        help_text='',
    )
    SubmissionMethod = CopyFromCharField(
        max_length=50,
        blank=True,
        verbose_name='',
        help_text='',
    )
    CBISubstantiationFlag = CopyFromBooleanField(
        verbose_name='',
        help_text='',
    )
    ElectronicWaiverReceivedFlag = CopyFromBooleanField(
        verbose_name='',
        help_text='',
    )
    PostmarkDate = CopyFromDateTimeField(
        null=True,
        verbose_name='',
        help_text='',
    )
    RMPCompleteFlag = CopyFromBooleanField(
        verbose_name='',
        help_text='',
    )
    DeRegistrationDate = CopyFromDateTimeField(
        null=True,
        verbose_name='',
        help_text='',
    )
    DeRegistrationEffectiveDate = CopyFromDateTimeField(
        null=True,
        verbose_name='',
        help_text='',
    )
    AnniversaryDate = CopyFromDateTimeField(
        verbose_name='',
        help_text='',
    )
    CBIFlag = CopyFromBooleanField(
        verbose_name='',
        help_text='',
    )
    CBIUnsanitizedVersionFlag = CopyFromBooleanField(
        verbose_name='',
        help_text='',
    )
    VersionNumber = CopyFromCharField(
        max_length=200,
        blank=True,
        verbose_name='',
        help_text='',
    )
    FRS_Lat = CopyFromDecimalField(
        null=True,
        max_digits=17,
        decimal_places=15,
        verbose_name='',
        help_text='',
    )
    FRS_Long = CopyFromDecimalField(
        null=True,
        max_digits=17,
        decimal_places=14,
        verbose_name='',
        help_text='',
    )
    FRS_Description = CopyFromCharField(
        max_length=40,
        blank=True,
        verbose_name='',
        help_text='',
    )
    FRS_Method = CopyFromCharField(
        max_length=60,
        blank=True,
        verbose_name='',
        help_text='',
    )
    HorizontalAccMeasure = CopyFromCharField(
        max_length=6,
        blank=True,
        verbose_name='',
        help_text='',
    )
    HorizontalRefDatumCode = CopyFromCharField(
        max_length=3,
        blank=True,
    )
    SourceMapScaleNumber = CopyFromCharField(
        max_length=10,
        blank=True,
        verbose_name='',
        help_text='',
    )
    EmergencyContactEmail = CopyFromEmailField(
        max_length=100,
        blank=True,
        verbose_name='',
        help_text='',
    )
    RMPPreparerName = CopyFromCharField(
        max_length=70,
        blank=True,
        verbose_name='',
        help_text='',
    )
    RMPPreparerStreet1 = CopyFromCharField(
        max_length=35,
        blank=True,
        verbose_name='',
        help_text='',
    )
    RMPPreparerStreet2 = CopyFromCharField(
        max_length=35,
        blank=True,
        verbose_name='',
        help_text='',
    )
    RMPPreparerCity = CopyFromCharField(
        max_length=30,
        blank=True,
        verbose_name='',
        help_text='',
    )
    RMPPreparerState = CopyFromForeignKey(
        'tlkpStateFIPSCodes',
        on_delete=models.PROTECT,
        related_name='rmppreparerstate',
        blank=True,
        verbose_name='',
        help_text='',
    )
    RMPPreparerZIP = CopyFromCharField(
        max_length=5,
        blank=True,
        verbose_name='',
        help_text='',
    )
    RMPPreparerZIP4Ext = CopyFromCharField(
        max_length=4,
        blank=True,
        verbose_name='',
        help_text='',
    )
    RMPPreparerTelephone = CopyFromCharField(
        max_length=10,
        blank=True,
        verbose_name='',
        help_text='',
    )
    RMPPreparerForeignStateOrProvince = CopyFromCharField(
        max_length=35,
        blank=True,
        verbose_name='',
        help_text='',
    )
    RMPPreparerForeignCountry = CopyFromForeignKey(
        'tlkpForeignCountry',
        on_delete=models.PROTECT,
        related_name='rmppreparerforeigncountry',
        blank=True,
        verbose_name='',
        help_text='',
    )
    RMPPreparerForeignPostalCode = CopyFromCharField(
        max_length=14,
        blank=True,
        verbose_name='',
        help_text='',
    )
    RMPSubmissionReasonCode = CopyFromForeignKey(
        'tlkpSubmissionReasonCodes',
        on_delete=models.PROTECT,
        source_column='RMPSubmissionReasonCode',
        blank=True,
        verbose_name='',
        help_text='',
    )
    RMPEmail = CopyFromEmailField(
        max_length=100,
        blank=True,
        verbose_name='',
        help_text='',
    )
    DeregistrationReasonCode = CopyFromForeignKey(
        'tlkpDeregistrationReason',
        on_delete=models.PROTECT,
        blank=True,
        verbose_name='',
        help_text='',
    )
    DeregistrationReasonOtherText = CopyFromCharField(
        max_length=80,
        blank=True,
        verbose_name='',
        help_text='',
    )

    source_file = 'tblS1Facilities'

    class Meta:
        verbose_name = 'Registration Information'
        verbose_name_plural = 'Registration Information'


class tblS1FlammableMixtureChemicals(BaseRMPModel):
    FlamMixChemID = CopyFromIntegerField(
        primary_key=True,
        verbose_name='Flam Mix Chem ID',
        help_text='Unique identifier for the Section 1 Flammable Mixture '
                  'Chemicals record destination table. Generated by '
                  'RMP*Submit and 3rd-party programs.',
    )
    ProcessChemicalID = CopyFromForeignKey(
        'tbls1ProcessChemicals',
        on_delete=models.PROTECT,
        verbose_name='Process Chemical ID',
        help_text='Unique number used to identify each chemical within a '
                  'single RMP. Generated by RMP*Submit and 3rd-party '
                  'programs.',
    )
    ChemicalID = CopyFromForeignKey(
        'tlkpChemicals',
        on_delete=models.PROTECT,
        verbose_name='Chemical ID',
        help_text='Chemical Abstract Service (CAS) registry number for the '
                  'flammable chemical.',
    )

    class Meta:
        verbose_name = 'Registration Information'
        verbose_name_plural = 'Registration Information'


class tblS1ProcessChemicals(BaseRMPModel):
    ProcessChemicalID = CopyFromIntegerField(
        primary_key=True,
        verbose_name='Process Chemical ID',
        help_text='Unique number used to identify each chemical within a '
                  'single RMP. Generated by RMP*Submit and 3rd-party programs.'
    )
    ProcessID = CopyFromForeignKey(
        'tblS1Processes',
        on_delete=models.PROTECT,
        verbose_name='Process ID',
        help_text='Unique number used to identify each covered process within '
                  'an RMP from Section 1 Program Level for the Covered '
                  'Process. Generated by RMP*Submit and 3rd-party programs.',
    )
    ChemicalID = CopyFromForeignKey(
        'tlkpChemicals',
        on_delete=models.PROTECT,
        verbose_name='Chemical ID',
        help_text='Chemical Abstract Service (CAS) registry number for the '
                  'chemical.',
    )
    Quantity = CopyFromDecimalField(
        max_digits=28,
        decimal_places=16,
        null=True,
        verbose_name='1.17.c.3 Quantity',
        help_text='The maximum inventory quantity of the regulated substance '
                  'or mixture in the process in pounds.',
    )
    CBI_Flag = CopyFromBooleanField(
        verbose_name='CBI Flag',
        help_text='An indication that the quantity was claimed as CBI.',
    )

    class Meta:
        verbose_name = 'Process: Chemical'
        verbose_name_plural = 'Process: Chemicals'


class tblS1ProcessNAICS(BaseRMPModel):
    Process_NAICS_ID = CopyFromIntegerField(
        primary_key=True,
        verbose_name='Process NAICS ID',
        help_text='Unique number used to identify each NAICS code within a '
                  'covered process in an RMP. Generated by RMP*Submit and '
                  '3rd-party programs.',
    )
    ProcessID = CopyFromForeignKey(
        'tblS1Processes',
        on_delete=models.PROTECT,
        verbose_name='Process ID',
        help_text='Unique number used to identify each covered process in an '
                  'RMP reported in Section 1. Generated by RMP*Submit and 3rd-'
                  'party programs.',
    )
    NAICSCode = CopyFromForeignKey(
        'tlkpNAICS',
        on_delete=models.PROTECT,
        verbose_name='1.17.b NAICS Code',
        help_text='The 5- or 6-digit NAICS Code.',
    )

    source_file = 'tblS1Process_NAICS'

    class Meta:
        verbose_name = 'Process: NAICS Code'
        verbose_name_plural = 'Process: NAICS Code'


class tblS1Processes(BaseRMPModel):
    ProcessID = CopyFromIntegerField(
        primary_key=True,
        verbose_name='Process ID',
        help_text='Unique number used to identify each process within the '
                  'RMP. The same number will not necessarily be assigned to '
                  'the same process for an RMP in a resubmission.',
    )
    AltID = CopyFromCharField(
        max_length=25,
        blank=True,
        verbose_name='Process Description',
        help_text='Optional Process Description.',
    )
    FacilityID = CopyFromForeignKey(
        'tblFacility',
        on_delete=models.PROTECT,
        verbose_name='Facility ID',
        help_text='Unique identifier for all RMPs submitted by a specific '
                  'facility (assigned by Reporting Center for first-time '
                  'submission). * After this number is assigned to the first '
                  'submission for a facility, subsequent submissions for the '
                  'same facility must include this identifier.',
    )
    ProgramLevel = CopyFromCharField(
        max_length=1,
        verbose_name='1.17.a Program Level',
        help_text='Program category, (e.g., Program Level 1, 2, or 3), to '
                  'identify with which program level the process complies.',
    )
    CBI_Flag = CopyFromBooleanField(
        verbose_name='CBI Flag',
        help_text='If Process Record Contains CBI Data.',
    )

    class Meta:
        verbose_name = 'Process'
        verbose_name_plural = 'Process'
