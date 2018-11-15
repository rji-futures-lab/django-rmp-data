"""Models for RMP "Lookup" source files (have a`tbl...` prefix.)."""
from django.db import models
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDecimalField,
    CopyFromDateTimeField,
    CopyFromIntegerField,
    CopyFromForeignKey,
)
from rmp.models.choices import (
    CHEMICAL_TYPE_CHOICES,
)
from rmp.models.base import BaseRMPModel



class TlkpChemicals(BaseRMPModel):
    chemicalid = CopyFromIntegerField(
        source_column='ChemicalID',
        primary_key=True,
        help_text="Unique Identifier for a Chemical.",
    )
    chemicalname = CopyFromCharField(
        source_column='ChemicalName',
        max_length=92,
        help_text="The name of the regulated chemical above the threshold "
                  "quantity in a Process at the source.",
    )
    casnumber = CopyFromCharField(
        source_column='CASNumber',
        max_length=10,
        blank=True,
        help_text="Chemical Abstract Service (CAS) registry number for the "
                  "chemical."
    )
    threshold = CopyFromDecimalField(
        source_column='Threshold',
        null=True,
        decimal_places=1,
        max_digits=8,
        help_text="Is the chemical quantity limit upon which reporting is "
                  "required."
    )
    chemtype = CopyFromCharField(
        source_column='ChemType',
        max_length=1,
        choices=CHEMICAL_TYPE_CHOICES,
        blank=True,
        help_text='"Chemical Type - (T)oxic or (F)lammable.',
    )
    flgcbi = CopyFromBooleanField(
        source_column='flgCBI',
        help_text="An indication that the Chemical is determined to be "
                  "Confidential Business Information (CBI). ‘Y’es or ‘N’o."
    )
    chemowner = CopyFromCharField(
        source_column='ChemOwner',
        max_length=3,
        blank=True,
        help_text="FED or State Abreviation"
    )

    source_file = 'tlkpChemicals'

    class Meta:
        verbose_name='Lookup: Process Chemical'


class TlkpDeregistrationReason(BaseRMPModel):
    lookupcode = CopyFromIntegerField(
        primary_key=True,
        source_column='LookupCode',
        help_text='System generated Unique Primary key.',
    )
    dereg_tr = CopyFromCharField(
        max_length=62,
        source_column='Description',
        help_text='Deregulation Reason descriptions.'
    )

    source_file = 'tlkpDeregistrationReason'

    class Meta:
        verbose_name='Lookup: Deregistration Reason'


class TlkpDocHandle(BaseRMPModel):
    lookupcode = CopyFromCharField(
        primary_key=True,
        source_column='LookupCode',
        max_length=1,
        help_text='Primary Key.',
    )
    description = CopyFromCharField(
        max_length=1,
        source_column='Description',
        help_text='A description of how the document was handled',
    )

    source_file = 'tlkpDocHandle'
    
    class Meta:
        verbose_name='Lookup: Deregistration Reason'


class TlkpDocType(BaseRMPModel):
    lookupcode = CopyFromCharField(
        source_column='LookupCode',
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the document type.'
    )
    description = CopyFromCharField(
        max_length=30,
        source_column='Description',
        help_text='Full description of the document type.'
    )

    source_file = 'tlkpDocType'
    
    class Meta:
        verbose_name=''


class TlkpLatLongDescriptions(BaseRMPModel):
    feat_code = CopyFromCharField(
        primary_key=True,
        max_length=2,
        source_column='Feat_Code',
        help_text='Unique identifier for each Latitude and longitude '
                  'description.',
    )
    feat_desc = CopyFromCharField(
        max_length=36,
        source_column='Feat_Desc',
        help_text='Latitude and longitude description.',
    )

    source_file = 'tlkpLatLongDescriptions'
    
    class Meta:
        verbose_name='Lookup: Lat/Long Description'


class TlkpLatLongMethods(BaseRMPModel):
    primary_key = CopyFromIntegerField(
        primary_key=True,
        source_column='Primary_Key',
    )
    method_code = CopyFromCharField(
        source_column='Method_Code',
        max_length=2
    )
    method_desc = CopyFromCharField(
        source_column='Method_Desc',
        max_length=83
    )

    source_file = 'tlkpLatLongMethods'
    
    class Meta:
        verbose_name='Lookup: Lat/Long Method'


class TlkpPhysicalStateCodes(BaseRMPModel):
    lookupcode = CopyFromCharField(
        primary_key=True,
        source_column='LookupCode',
        max_length=1,
        help_text='Physical State description.',
    )
    description = CopyFromCharField(
        source_column='Description',
        max_length=30,
        help_text='System generated Unique Primary key.',
    )

    source_file = 'tlkpPhysicalStateCodes'
    
    class Meta:
        verbose_name='Lookup: Physical State Code'


class TlkpRejectReason(BaseRMPModel):
    lookupcode = CopyFromCharField(
        primary_key=True,
        source_column='LookupCode',
        max_length=1,
        help_text='System generated Unique Primary key.',
    )
    description = CopyFromCharField(
        source_column='Description',
        max_length=59,
        help_text='Rejection Reason descriptions.',
    )

    source_file = 'tlkpRejectReason'
    
    class Meta:
        verbose_name='Lookup: Reject Reason'


class TlkpS2ScenarioCodes(BaseRMPModel):
    lookupcode = CopyFromCharField(
        primary_key=True,
        source_column='LookupCode',
        max_length=1,
        help_text='System generated Unique Primary key.',
    )
    description = CopyFromCharField(
        source_column='Description',
        max_length=27,
        help_text='Pick-list text.',
    )

    source_file = 'tlkpS2ScenarioCodes'
    
    class Meta:
        verbose_name='Lookup: Toxics Scenario Code'


class TlkpS6InitiatingEvents(BaseRMPModel):
    lookupcode = CopyFromCharField(
        primary_key=True,
        source_column='LookupCode',
        max_length=1,
        help_text='System generated Unique Primary key.',
    )
    description = CopyFromCharField(
        source_column='Description',
        max_length=40,
        help_text='Pick-list text.',
    )

    source_file = 'tlkpS6InitiatingEvents'
    
    class Meta:
        verbose_name='Lookup: Initiating Events'


class TlkpSubmissionReasonCodes(BaseRMPModel):
    lookupcode = CopyFromCharField(
        primary_key=True,
        source_column='LookupCode',
        max_length=3,
        help_text='System generated Unique Primary key.',
    )
    description = CopyFromCharField(
        source_column='Description',
        max_length=101,
        help_text='Submission Reason descriptions.',
    )

    source_file = 'tlkpSubmissionReasonCodes'
    
    class Meta:
        verbose_name='Lookup: Submission Reason Code'


class TlkpTopographyCode(BaseRMPModel):
    lookupcode = CopyFromCharField(
        primary_key=True,
        source_column='LookupCode',
        max_length=1,
        help_text='System generated Unique Primary key.',
    )
    description = CopyFromCharField(
        source_column='Description',
        max_length=5,
        help_text='A code representing whether the local topography is urban or rural.',
    )

    source_file = 'tlkpTopographyCode'
    
    class Meta:
        verbose_name='Lookup: Topography Code'


class TlkpWindSpeedUnitCodes(BaseRMPModel):
    lookupcode = CopyFromCharField(
        primary_key=True,
        source_column='LookupCode',
        max_length=1,
        help_text='System generated Unique Primary key.',
    )
    description = CopyFromCharField(
        source_column='Description',
        max_length=13,
        help_text='Wind Speed Unit Descriptions.',
    )

    source_file = 'tlkpWindSpeedUnitCodes'
    
    class Meta:
        verbose_name='Lookup: Wind Speed Unit Codes'


class TlkpCountyFIPSCodes(BaseRMPModel):
    state_code = CopyFromForeignKey(
        'tlkpStateFIPSCodes',
        on_delete=models.PROTECT,
        source_column='State_Code',
        help_text='The U.S. Postal Service abbreviation for the state in which'
                  ' the facility is located.',
    )
    county_code = CopyFromCharField(
        max_length=2,
        source_column='County_Code',
        help_text='Federal Information Processing Standard (FIPS) code for the'
                  ' county in which the facility is located.',
    )
    county_name = CopyFromCharField(
        source_column='County_Name',
        max_length=30,
        help_text='The name of the county.',
    )
    statecounty_code = CopyFromCharField(
        primary_key=True,
        source_column='StateCounty_Code',
        help_text='Concatenation of state_code and county_code(?)',
        max_length=5,
    )

    source_file = 'tlkpCountyFIPSCodes'
    
    class Meta:
        verbose_name='Lookup: County FIPS codes'


class TlkpStateFIPSCodes(BaseRMPModel):
    state_code = CopyFromCharField(
        max_length=2,
        source_column='STATE_CODE',
        help_text='Federal Information Processing Standard (FIPS) code for the'
                  ' county in which the facility is located.'
    )
    state_abbr = CopyFromCharField(
        primary_key=True,
        source_column='STATE_ABBR',
        max_length=2,
        help_text='The U.S. Postal Service abbreviation for the state in which'
                  ' the facility is located.',
    )
    state_name = CopyFromCharField(
        source_column='STATE_NAME',
        max_length=30,
        help_text='The state in which the facility is located.',
    )
    region = CopyFromCharField(
        source_column='REGION',
        help_text='The code which represents the EPA Region in which the state'
                  ' resides.',
        max_length=2,
    )

    source_file = 'tlkpStateFIPSCodes'
    
    class Meta:
        verbose_name='Lookup: State FIPS codes'
