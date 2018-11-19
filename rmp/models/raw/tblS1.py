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
    facilityid = CopyFromIntegerField(
        primary_key=True,
        source_column='FacilityID',
        verbose_name='RMP Identifier',
        help_text='Unique identifier for all RMPs submitted by a specific '
                  'facility (assigned by Reporting Center for first-time '
                  'submission). * After this number is assigned to the first '
                  'submission for a facility, subsequent submissions for the '
                  'same facility must include this identifier.',
    )
    facilityname = CopyFromCharField(
        max_length=255,
        blank=True,
        source_column='FacilityName',
        verbose_name='1.1.a Facility Name',
        help_text='Facility name specific to the site.',
    )
    facilitystr1 = CopyFromCharField(
        max_length=35,
        blank=True,
        source_column='FacilityStr1',
        verbose_name='1.5.a Facility Street - Line 1',
        help_text='Facility Street - Line 1 using local street and road '
                  'designations. No post office box numbers or rural route '
                  'numbers. This is not the mailing address.',
    )
    facilitystr2 = CopyFromCharField(
        max_length=35,
        blank=True,
        source_column='FacilityStr2',
        verbose_name='1.5.b Facility Street - Line 2',
        help_text='Facility Street Address - Line 2',
    )
    facilitycity = CopyFromCharField(
        max_length=19,
        source_column='FacilityCity',
        verbose_name='1.5.c Facility City',
        help_text='The name of the city, town, or village where the '
                  'facility is located.',
    )
    facilitystate = CopyFromForeignKey(
        'tlkpStateFIPSCodes',
        on_delete=models.PROTECT,
        related_name='facilitystate',
        source_column='FacilityState',
        verbose_name='1.5.d Facility State',
        help_text='The U.S. Postal Service abbreviation for the state in '
                  'which the facility is located.',
    )
    facilityzipcode = CopyFromCharField(
        max_length=5,
        source_column='FacilityZipCode',
        verbose_name='1.5.e Facility ZIP Code',
        help_text='The Zoning Improvement Plan (ZIP) Code assigned to the '
                  'facility by the U.S. Postal Service which represents a '
                  'geographic area that facilitates mail delivery.',
    )
    facility4digitzipext = CopyFromCharField(
        max_length=4,
        blank=True,
        source_column='Facility4DigitZipExt',
        verbose_name='1.5.e Facility ZIP Extention',
        help_text='The four-digit extension code that represents the '
                  'geographic segment that is a sub-unit of the ZIP Code and '
                  'further refines the exact location of the facility.',
    )
    facilitycountyfips = CopyFromForeignKey(
        'tlkpCountyFIPSCodes',
        on_delete=models.PROTECT,
        blank=True,
        source_column='FacilityCountyFIPS',
        verbose_name='1.5.f Facility County',
        help_text='Federal Information Processing Standard (FIPS) code for '
                  'county in which the facility is located.',
    )
    lepc = CopyFromCharField(
        max_length=30,
        blank=True,
        source_column='LEPC',
        verbose_name='1.10 LEPC',
        help_text='Local Emergency Planning Committee (LEPC) associated with '
                  'the facility county. For LEPC information refer to the '
                  'LEPC/SERC Net Web site at http://www.RTK.NET:80/lepc. Must '
                  'cover all or part of the Facility County.',
    )
    facilitylatdecdegs = CopyFromDecimalField(
        max_digits=9,
        decimal_places=7,
        source_column='FacilityLatDecDegs',
        verbose_name='1.5.g Facility Latitude (Decimal Degrees)',
        help_text='Facility Latitude in decimal degrees.',
    )
    facilitylongdecdegs = CopyFromDecimalField(
        max_digits=10,
        decimal_places=7,
        source_column='FacilityLongDecDegs',
        verbose_name='1.5.h Facility Longitude (Decimal Degrees)',
        help_text='Facility Longitude in decimal degrees.',
    )
    validlatlongflag = CopyFromCharField(
        max_length=1,
        blank=True,
        source_column='ValidLatLongFlag',
        verbose_name='Valid Lat/Long Flag',
        help_text='Flag used to indicate whether the Latitude/Longitude is '
                  'valid.',
    )
    latlongmethod = CopyFromForeignKey(
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
    latlongdescription = CopyFromCharField(
        max_length=2,
        blank=True,
        source_column='LatLongDescription',
        verbose_name='1.5.j Lat/Long Description',
        help_text='Code for the physical place corresponding to the coordinate.'
                  ' Codes can be obtained from MAD Version 6.1 Standard as '
                  'implemented in Envirofacts Locational Reference Tables (EF '
                  'LRT). http://www.epa.gov/enviro/html/lrt/lrt_over.html',
    )
    facilityurl = CopyFromURLField(
        max_length=100,
        blank=True,
        source_column='FacilityURL',
        verbose_name='1.9.c Facility or Parent Company WWW Homepage Address',
        help_text='Facility or Parent Company homepage web address.',
    )
    facilityphonenumber = CopyFromCharField(
        max_length=10,
        blank=True,
        source_column='FacilityPhoneNumber',
        verbose_name='1.9.b Facility Public Contact Phone Number',
        help_text='Facility phone number for public inquiries to contact '
                  'owner, 112(r) person responsible, etc.',
    )
    facilityemailaddress = CopyFromEmailField(
        max_length=100,
        blank=True,
        source_column='FacilityEmailAddress',
        verbose_name='1.9.a Facility or Parent Company E-mail Address',
        help_text='The text that represents the electronic mail (email) '
                  'address for the facility or parent company.',
    )
    facilityduns = CopyFromCharField(
        max_length=9,
        source_column='FacilityDUNS',
        verbose_name='1.4.a Facility DUNS',
        help_text='The Data Universal Numbering System (DUNS) number assigned '
                  'by Dun & Bradstreet to the facility.',
    )
    parentcompanyname = CopyFromCharField(
        source_column='ParentCompanyName',
        max_length=250,
        blank=True,
        verbose_name='1.1.b Parent Company #1 Name',
        help_text='First Parent Company Name.',
    )
    company2name = CopyFromCharField(
        source_column='Company2Name',
        max_length=50,
        blank=True,
        verbose_name='1.1.c Parent Company #2 Name',
        help_text='Second Parent Company name for joint ventures.',
    )
    companyduns = CopyFromCharField(
        source_column='CompanyDUNS',
        max_length=9,
        verbose_name='1.4.b Parent Company #1 DUNS',
        help_text='The DUNS Number assigned by Dun & Bradstreet to the parent '
                  'of the company of interest.',
    )
    company2duns = CopyFromCharField(
        source_column='Company2DUNS',
        max_length=9,
        verbose_name='1.4.c Parent Company #2 DUNS',
        help_text='If your facility is owned by a joint venture, this is the '
                  'DUNS Number assigned by Dun & Bradstreet to the second '
                  'parent company.',
    )
    operatorname = CopyFromCharField(
        source_column='OperatorName',
        max_length=250,
        blank=True,
        verbose_name='1.6.a Owner/Operator Name',
        help_text='Name of the person or entity that owns or operates the '
                  'facility.',
    )
    operatorphone = CopyFromCharField(
        source_column='OperatorPhone',
        max_length=10,
        blank=True,
        verbose_name='1.6.b Owner/Operator Phone',
        help_text='Phone number for the Owner or Operator.',
    )
    operatorstr1 = CopyFromCharField(
        source_column='OperatorStr1',
        max_length=35,
        blank=True,
        verbose_name='1.6.c Owner/Operator Street - Line 1',
        help_text='Line 1 of the business street mailing address for the '
                  'Owner or Operator.',
    )
    operatorstr2 = CopyFromCharField(
        source_column='OperatorStr2',
        max_length=35,
        blank=True,
        verbose_name='1.6.d Owner/Operator Street - Line 2',
        help_text='Line 2 of the business street mailing address for the '
                  'Owner or Operator.',
    )
    operatorcity = CopyFromCharField(
        source_column='OperatorCity',
        max_length=19,
        blank=True,
        verbose_name='1.6.e Owner/Operator City',
        help_text='City for the business mailing address for the Owner or '
                  'Operator.',
    )
    operatorstatefips = CopyFromForeignKey(
        'tlkpStateFIPSCodes',
        on_delete=models.PROTECT,
        source_column='OperatorStateFIPS',
        max_length=2,
        blank=True,
        verbose_name='1.6.f Owner/Operator State',
        help_text='The U.S. Postal Service state abbreviation for the address '
                  'of the Owner or Operator.',
    )
    operatorzipcode = CopyFromCharField(
        source_column='OperatorZipCode',
        max_length=5,
        blank=True,
        verbose_name='1.6.g Owner/Operator ZIP Code',
        help_text='ZIP Code for the business mailing address of the Owner or '
                  'Operator.',
    )
    operatorzipcodeext = CopyFromCharField(
        source_column='OperatorZipCodeExt',
        max_length=4,
        blank=True,
        verbose_name='1.6.g Owner/Operator ZIP four-digit extention code',
        help_text='The four-digit extension code that represents the '
                  'geographic segment that is a subunit of the ZIP Code and '
                  'further refines the business mailing address of the Owner '
                  'or Operator.',
    )
    rmpcontact = CopyFromCharField(
        source_column='RMPContact',
        max_length=35,
        blank=True,
        verbose_name='1.7.a Name of Person Responsible for RMP Implementaion',
        help_text='Person or position responsible for RMP implementation '
                  '(40 CFR Part 68).',
    )
    rmptitle = CopyFromCharField(
        source_column='RMPTitle',
        max_length=250,
        blank=True,
        verbose_name='1.7.b Title/Position of Person Responsible for RMP '
                     'Implementaion',
        help_text='Title of person or position responsible for RMP '
                  'implementation (40 CFR Part 68).',
    )
    emergencycontactname = CopyFromCharField(
        source_column='EmergencyContactName',
        max_length=250,
        blank=True,
        verbose_name='1.8.a Emergency Contact Name',
        help_text='Name of person designated as the emergency contact for the '
                  'facility.',
    )
    emergencycontacttitle = CopyFromCharField(
        source_column='EmergencyContactTitle',
        max_length=35,
        blank=True,
        verbose_name='1.8.b Emergency Contact Title',
        help_text='Title or job classification of the emergency contact.',
    )
    emergencycontactphone = CopyFromCharField(
        source_column='EmergencyContactPhone',
        max_length=10,
        blank=True,
        verbose_name='1.8.c Emergency Contact Phone',
        help_text='Phone number where the emergency contact can be reached '
                  'during normal working hours.',
    )
    phone24 = CopyFromCharField(
        source_column='Phone24',
        max_length=10,
        blank=True,
        verbose_name='1.8.d 24-Hour Phone',
        help_text='Number where emergency contact can be reached during '
                  'non-working hours, such as a beeper number.',
    )
    emergencycontactext_pin = CopyFromCharField(
        source_column='EmergencyContactExt_PIN',
        max_length=10,
        blank=True,
        verbose_name='1.8.e 24-Hour Phone Extention/PIN',
        help_text='Phone extension or pager number for the 24-Hour Phone.',
    )
    fte = CopyFromIntegerField(
        source_column='FTE',
        null=True,
        verbose_name='1.11 Number of Full Time Employees (FTEs)',
        help_text='Number of full-time equivalent employees.',
    )
    otherepafacilityid = CopyFromCharField(
        source_column='OtherEPAFacilityID',
        max_length=15,
        null=True,
        verbose_name='1.3 Other EPA Systems Program Facility Identifier',
        help_text='The unique identification number assigned to a facility by '
                  'the Facility Index System (FINDS) (or if not known, the '
                  'Resource Conservation and Recovery Act (RCRA), Emergency '
                  'Planning and Community Right-to-Know Act (EPCRA), TRI, or '
                  'other EPA facility identifier).',
    )
    epafacilityid = CopyFromForeignKey(
        'tblFacility',
        on_delete=models.PROTECT,
        source_column='EPAFacilityID',
        verbose_name='1.2 EPA Facility Identifier',
        help_text='1.2 EPA Facility Identifier',
    )
    osha_psm = CopyFromBooleanField(
        source_column='OSHA_PSM',
        verbose_name='1.12.a Covered by: OSHA PSM',
        help_text='Occupational Safety and Health Act (OSHA) Process Safety '
                  'Management (PSM) Standard. Question covers all processes '
                  'at the facility; if any process at the facility is '
                  'subject to OSHA PSM, must answer “Y” even if the PSM '
                  'process is not covered by this Rule.',
        )
    epcra_302 = CopyFromBooleanField(
        source_column='EPCRA_302',
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
    caa_titlev = CopyFromBooleanField(
        source_column='CAA_TitleV',
        verbose_name='1.12.c CAA Title V',
        help_text='Indicate if your facility has a CAA Title V Operating '
                  'Permit with “Y.” CAA Title V Air Operating Permit ID '
                  'Title V (Part 70) of the Clean Air Act (40CFR70) '
                  'requires major sources of air pollution to obtain '
                  'permits.',
    )
    clearairoppermitid = CopyFromCharField(
        source_column='ClearAirOpPermitID',
        max_length=15,
        null=True,
        verbose_name='1.12.d Air Operating Permit ID',
        help_text='Unique identifier for a CAA Title V Air Operating Permit '
                  'or state equivalent ID.',
    )
    safetyinspectiondate = CopyFromDateTimeField(
        source_column='SafetyInspectionDate',
        null=True,
        verbose_name='1.12.d Air Operating Permit ID',
        help_text='Unique identifier for a CAA Title V Air Operating Permit '
                  'or state equivalent ID.',
    )
    safetyinspectionby = CopyFromCharField(
        source_column='SafetyInspectionBy',
        max_length=50,
        blank=True,
        verbose_name='1.15 Last Safety Inspection Performed by:',
        help_text='A designation representing the external agency that '
                  'performed the last safety inspection. One or more of the '
                  'following is expected: OSHA State OSHA EPA State EPA Fire '
                  'Department Never had a safety inspection Other',
    )
    osharanking = CopyFromBooleanField(
        source_column='OSHARanking',
        verbose_name='1.13 OSH Star or Merit Ranking',
        help_text="A stationary source with a Star or Merit ranking under "
                  "OSHA's voluntary protection program shall be exempt from "
                  "audits under paragraph (b)(2) and (b)(7) of [Section 68.220"
                  " - audits].",
    )
    predictivefilingflag = CopyFromBooleanField(
        source_column='PredictiveFilingFlag',
        verbose_name='Predictive Filing Flag',
        help_text="An indication that the submitter is using Predictive "
                  "Filing for the facility's RMP.",
    )
    submissiontype = CopyFromCharField(
        source_column='SubmissionType',
        max_length=1,
        blank=True,
        verbose_name='Submission Type',
        help_text='Submission Type “F” - First-time submission “R” - '
                  'Resubmission “C” - Correction of existing RMP',
    )
    rmpdescription = CopyFromCharField(
        source_column='RMPDescription',
        max_length=50,
        blank=True,
        verbose_name='RMP Description',
        help_text='RMP Description is an optional description for the whole '
                  'RMP. RMP Description is not accessible to RMP*Info on the '
                  'Web.',
    )
    noaccidents = CopyFromBooleanField(
        source_column='NoAccidents',
        verbose_name='No Accidents Flag',
        help_text='Optional Flag to Indicate whether there are any accidents '
                  'to report.',
    )
    foreignstateprov = CopyFromCharField(
        source_column='ForeignStateProv',
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
    foreignzipcode = CopyFromCharField(
        source_column='ForeignZipCode',
        max_length=14,
        blank=True,
        verbose_name='',
        help_text='',
    )
    foreigncountry = CopyFromForeignKey(
        'tlkpForeignCountry',
        on_delete=models.PROTECT,
        related_name='foreigncountry',
        source_column='ForeignCountry',
        blank=True,
        verbose_name='',
        help_text='',
    )
    cbi_flag = CopyFromBooleanField(
        source_column='CBI_Flag',
        verbose_name='',
        help_text='',
    )
    completioncheckdate = CopyFromDateTimeField(
        source_column='CompletionCheckDate',
        verbose_name='',
        help_text='',
    )
    errorreportdate = CopyFromDateTimeField(
        source_column='ErrorReportDate',
        null=True,
        verbose_name='',
        help_text='',
    )
    receiptdate = CopyFromCharField(
        source_column='ReceiptDate',
        max_length=25,
        verbose_name='',
        help_text='',
    )
    graphicsindicator = CopyFromBooleanField(
        source_column='GraphicsIndicator',
        verbose_name='',
        help_text='',
    )
    attachmentsindicator = CopyFromBooleanField(
        source_column='AttachmentsIndicator',
        verbose_name='',
        help_text='',
    )
    certificationreceivedflag = CopyFromBooleanField(
        source_column='CertificationReceivedFlag',
        verbose_name='',
        help_text='',
    )
    submissionmethod = CopyFromCharField(
        source_column='SubmissionMethod',
        max_length=50,
        blank=True,
        verbose_name='',
        help_text='',
    )
    cbisubstantiationflag = CopyFromBooleanField(
        source_column='CBISubstantiationFlag',
        verbose_name='',
        help_text='',
    )
    electronicwaiverreceivedflag = CopyFromBooleanField(
        source_column='ElectronicWaiverReceivedFlag',
        verbose_name='',
        help_text='',
    )
    postmarkdate = CopyFromDateTimeField(
        source_column='PostmarkDate',
        null=True,
        verbose_name='',
        help_text='',
    )
    rmpcompleteflag = CopyFromBooleanField(
        source_column='RMPCompleteFlag',
        verbose_name='',
        help_text='',
    )
    deregistrationdate = CopyFromDateTimeField(
        source_column='DeRegistrationDate',
        null=True,
        verbose_name='',
        help_text='',
    )
    deregistrationeffectivedate = CopyFromDateTimeField(
        source_column='DeRegistrationEffectiveDate',
        null=True,
        verbose_name='',
        help_text='',
    )
    anniversarydate = CopyFromDateTimeField(
        source_column='AnniversaryDate',
        verbose_name='',
        help_text='',
    )
    cbiflag = CopyFromBooleanField(
        source_column='CBIFlag',
        verbose_name='',
        help_text='',
    )
    cbiunsanitizedversionflag = CopyFromBooleanField(
        source_column='CBIUnsanitizedVersionFlag',
        verbose_name='',
        help_text='',
    )
    versionnumber = CopyFromCharField(
        source_column='VersionNumber',
        max_length=200,
        blank=True,
        verbose_name='',
        help_text='',
    )
    frs_lat = CopyFromDecimalField(
        source_column='FRS_Lat',
        null=True,
        max_digits=17,
        decimal_places=15,
        verbose_name='',
        help_text='',
    )
    frs_long = CopyFromDecimalField(
        source_column='FRS_Long',
        null=True,
        max_digits=17,
        decimal_places=14,
        verbose_name='',
        help_text='',
    )
    frs_description = CopyFromCharField(
        source_column='FRS_Description',
        max_length=40,
        blank=True,
        verbose_name='',
        help_text='',
    )
    frs_method = CopyFromCharField(
        source_column='FRS_Method',
        max_length=60,
        blank=True,
        verbose_name='',
        help_text='',
    )
    horizontalaccmeasure = CopyFromCharField(
        source_column='HorizontalAccMeasure',
        max_length=6,
        blank=True,
        verbose_name='',
        help_text='',
    )
    horizontalrefdatumcode = CopyFromCharField(
        source_column='HorizontalRefDatumCode',
        max_length=3,
        blank=True,
    )
    sourcemapscalenumber = CopyFromCharField(
        source_column='SourceMapScaleNumber',
        max_length=10,
        blank=True,
        verbose_name='',
        help_text='',
    )
    emergencycontactemail = CopyFromEmailField(
        source_column='EmergencyContactEmail',
        max_length=100,
        blank=True,
        verbose_name='',
        help_text='',
    )
    rmppreparername = CopyFromCharField(
        source_column='RMPPreparerName',
        max_length=70,
        blank=True,
        verbose_name='',
        help_text='',
    )
    rmppreparerstreet1 = CopyFromCharField(
        source_column='RMPPreparerStreet1',
        max_length=35,
        blank=True,
        verbose_name='',
        help_text='',
    )
    rmppreparerstreet2 = CopyFromCharField(
        source_column='RMPPreparerStreet2',
        max_length=35,
        blank=True,
        verbose_name='',
        help_text='',
    )
    rmppreparercity = CopyFromCharField(
        source_column='RMPPreparerCity',
        max_length=30,
        blank=True,
        verbose_name='',
        help_text='',
    )
    rmppreparerstate = CopyFromForeignKey(
        'tlkpStateFIPSCodes',
        on_delete=models.PROTECT,
        related_name='rmppreparerstate',
        source_column='RMPPreparerState',
        blank=True,
        verbose_name='',
        help_text='',
    )
    rmppreparerzip = CopyFromCharField(
        source_column='RMPPreparerZIP',
        max_length=5,
        blank=True,
        verbose_name='',
        help_text='',
    )
    rmppreparerzip4ext = CopyFromCharField(
        source_column='RMPPreparerZIP4Ext',
        max_length=4,
        blank=True,
        verbose_name='',
        help_text='',
    )
    rmppreparertelephone = CopyFromCharField(
        source_column='RMPPreparerTelephone',
        max_length=10,
        blank=True,
        verbose_name='',
        help_text='',
    )
    rmppreparerforeignstateorprovince = CopyFromCharField(
        source_column='RMPPreparerForeignStateOrProvince',
        max_length=35,
        blank=True,
        verbose_name='',
        help_text='',
    )
    rmppreparerforeigncountry = CopyFromForeignKey(
        'tlkpForeignCountry',
        on_delete=models.PROTECT,
        related_name='rmppreparerforeigncountry',
        source_column='RMPPreparerForeignCountry',
        max_length=2,
        blank=True,
        verbose_name='',
        help_text='',
    )
    rmppreparerforeignpostalcode = CopyFromCharField(
        source_column='RMPPreparerForeignPostalCode',
        max_length=14,
        blank=True,
        verbose_name='',
        help_text='',
    )
    rmpsubmissionreasoncode = CopyFromForeignKey(
        'tlkpSubmissionReasonCodes',
        on_delete=models.PROTECT,
        source_column='RMPSubmissionReasonCode',
        max_length=3,
        blank=True,
        verbose_name='',
        help_text='',
    )
    rmpemail = CopyFromEmailField(
        source_column='RMPEmail',
        max_length=100,
        blank=True,
        verbose_name='',
        help_text='',
    )
    deregistrationreasoncode = CopyFromForeignKey(
        'tlkpDeregistrationReason',
        on_delete=models.PROTECT,
        source_column='DeregistrationReasonCode',
        max_length=2,
        blank=True,
        verbose_name='',
        help_text='',
    )
    deregistrationreasonothertext = CopyFromCharField(
        source_column='DeregistrationReasonOtherText',
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
    flammixchemid = CopyFromIntegerField(
        primary_key=True,
        source_column='FlamMixChemID',
        verbose_name='Flam Mix Chem ID',
        help_text='Unique identifier for the Section 1 Flammable Mixture '
                  'Chemicals record destination table. Generated by '
                  'RMP*Submit and 3rd-party programs.',
    )
    processchemicalid = CopyFromForeignKey(
        'tbls1ProcessChemicals',
        on_delete=models.PROTECT,
        source_column='ProcessChemicalID',
        verbose_name='Process Chemical ID',
        help_text='Unique number used to identify each chemical within a '
                  'single RMP. Generated by RMP*Submit and 3rd-party '
                  'programs.',
    )
    chemicalid = CopyFromForeignKey(
        'tlkpChemicals',
        on_delete=models.PROTECT,
        source_column='ChemicalID',
        verbose_name='Chemical ID',
        help_text='Chemical Abstract Service (CAS) registry number for the '
                  'flammable chemical.',
    )

    class Meta:
        verbose_name = 'Registration Information'
        verbose_name_plural = 'Registration Information'


class tblS1ProcessChemicals(BaseRMPModel):
    processchemicalid = CopyFromIntegerField(
        primary_key=True,
        source_column='ProcessChemicalID',
        verbose_name='Process Chemical ID',
        help_text='Unique number used to identify each chemical within a '
                  'single RMP. Generated by RMP*Submit and 3rd-party programs.'
    )
    processid = CopyFromForeignKey(
        'tblS1Processes',
        on_delete=models.PROTECT,
        source_column='ProcessID',
        verbose_name='Process ID',
        help_text='Unique number used to identify each covered process within '
                  'an RMP from Section 1 Program Level for the Covered '
                  'Process. Generated by RMP*Submit and 3rd-party programs.',
    )
    chemicalid = CopyFromForeignKey(
        'tlkpChemicals',
        on_delete=models.PROTECT,
        source_column='ChemicalID',
        verbose_name='Chemical ID',
        help_text='Chemical Abstract Service (CAS) registry number for the '
                  'chemical.',
    )
    quantity = CopyFromDecimalField(
        max_digits=28,
        decimal_places=16,
        null=True,
        source_column='Quantity',
        verbose_name='1.17.c.3 Quantity',
        help_text='The maximum inventory quantity of the regulated substance '
                  'or mixture in the process in pounds.',
    )
    cbi_flag = CopyFromBooleanField(
        source_column='CBI_Flag',
        verbose_name='CBI Flag',
        help_text='An indication that the quantity was claimed as CBI.',
    )

    class Meta:
        verbose_name = 'Process: Chemical'
        verbose_name_plural = 'Process: Chemicals'


class tblS1ProcessNAICS(BaseRMPModel):
    process_naics_id = CopyFromIntegerField(
        primary_key=True,
        source_column='Process_NAICS_ID',
        verbose_name='Process NAICS ID',
        help_text='Unique number used to identify each NAICS code within a '
                  'covered process in an RMP. Generated by RMP*Submit and '
                  '3rd-party programs.',
    )
    processid = CopyFromForeignKey(
        'tblS1Processes',
        on_delete=models.PROTECT,
        source_column='ProcessID',
        verbose_name='Process ID',
        help_text='Unique number used to identify each covered process in an '
                  'RMP reported in Section 1. Generated by RMP*Submit and 3rd-'
                  'party programs.',
    )
    naicscode = CopyFromForeignKey(
        'tlkpNAICS',
        on_delete=models.PROTECT,
        source_column='NAICSCode',
        verbose_name='1.17.b NAICS Code',
        help_text='The 5- or 6-digit NAICS Code.',
    )

    source_file = 'tblS1Process_NAICS'

    class Meta:
        verbose_name = 'Process: NAICS Code'
        verbose_name_plural = 'Process: NAICS Code'


class tblS1Processes(BaseRMPModel):
    processid = CopyFromIntegerField(
        primary_key=True,
        source_column='ProcessID',
        verbose_name='Process ID',
        help_text='Unique number used to identify each process within the '
                  'RMP. The same number will not necessarily be assigned to '
                  'the same process for an RMP in a resubmission.',
    )
    altid = CopyFromCharField(
        max_length=25,
        source_column='AltID',
        blank=True,
        verbose_name='Process Description',
        help_text='Optional Process Description.',
    )
    facilityid = CopyFromForeignKey(
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
    programlevel = CopyFromCharField(
        max_length=1,
        source_column='ProgramLevel',
        verbose_name='1.17.a Program Level',
        help_text='Program category, (e.g., Program Level 1, 2, or 3), to '
                  'identify with which program level the process complies.',
    )
    cbi_flag = CopyFromBooleanField(
        source_column='CBI_Flag',
        verbose_name='CBI Flag',
        help_text='If Process Record Contains CBI Data.',
    )

    class Meta:
        verbose_name = 'Process'
        verbose_name_plural = 'Process'
