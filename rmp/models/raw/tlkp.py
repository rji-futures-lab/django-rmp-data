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


class tlkpChemicals(BaseRMPModel):
    ChemicalID = CopyFromIntegerField(
        primary_key=True,
        help_text="Unique Identifier for a Chemical.",
    )
    ChemicalName = CopyFromCharField(
        max_length=92,
        help_text="The name of the regulated chemical above the threshold "
                  "quantity in a Process at the source.",
    )
    CASNumber = CopyFromCharField(
        max_length=10,
        blank=True,
        help_text="Chemical Abstract Service (CAS) registry number for the "
                  "chemical."
    )
    Threshold = CopyFromDecimalField(
        null=True,
        decimal_places=1,
        max_digits=8,
        help_text="Is the chemical quantity limit upon which reporting is "
                  "required."
    )
    ChemType = CopyFromCharField(
        max_length=1,
        choices=CHEMICAL_TYPE_CHOICES,
        blank=True,
        help_text='"Chemical Type - (T)oxic or (F)lammable.',
    )
    flgCBI = CopyFromBooleanField(
        help_text="An indication that the Chemical is determined to be "
                  "Confidential Business Information (CBI). ‘Y’es or ‘N’o."
    )
    ChemOwner = CopyFromCharField(
        max_length=3,
        blank=True,
        help_text="FED or State Abreviation"
    )

    class Meta:
        verbose_name='Lookup: Process Chemical'


class tlkpCountyFIPSCodes(BaseRMPModel):
    State_Code = CopyFromForeignKey(
        'tlkpStateFIPSCodes',
        on_delete=models.PROTECT,
        help_text='The U.S. Postal Service abbreviation for the state in which'
                  ' the facility is located.',
        db_column='State_Code',
    )
    County_Code = CopyFromCharField(
        max_length=2,
        help_text='Federal Information Processing Standard (FIPS) code for the'
                  ' county in which the facility is located.',
    )
    County_Name = CopyFromCharField(
        max_length=30,
        help_text='The name of the county.',
    )
    StateCounty_Code = CopyFromCharField(
        primary_key=True,
        help_text='Concatenation of state_code and county_code(?)',
        max_length=5,
    )

    class Meta:
        verbose_name='Lookup: County FIPS codes'


class tlkpDeregistrationReason(BaseRMPModel):
    LookupCode = CopyFromCharField(
        primary_key=True,
        max_length=2,
        help_text='System generated Unique Primary key.',
    )
    Description = CopyFromCharField(
        max_length=62,
        help_text='Deregulation Reason descriptions.'
    )

    class Meta:
        verbose_name='Lookup: Deregistration Reason'


class tlkpDocHandle(BaseRMPModel):
    LookupCode = CopyFromCharField(
        primary_key=True,
        max_length=1,
        help_text='Primary Key.',
    )
    Description = CopyFromCharField(
        max_length=1,
        help_text='A description of how the document was handled',
    )

    class Meta:
        verbose_name='Lookup: Deregistration Reason'


class tlkpDocType(BaseRMPModel):
    LookupCode = CopyFromCharField(
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the document type.'
    )
    Description = CopyFromCharField(
        max_length=30,
        help_text='Full description of the document type.'
    )

    class Meta:
        verbose_name='Lookup: Doc Type'


class tlkpForeignCountry(BaseRMPModel):
    LookupCode = CopyFromCharField(
        primary_key=True,
        max_length=2,
    )
    Description = CopyFromCharField(
        max_length=50,
    )

    class Meta:
        verbose_name='Lookup: Foreign Country Codes'


class tlkpLatLongDescriptions(BaseRMPModel):
    Feat_Code = CopyFromCharField(
        primary_key=True,
        max_length=2,
        help_text='Unique identifier for each Latitude and longitude '
                  'description.',
    )
    Feat_Desc = CopyFromCharField(
        max_length=36,
        help_text='Latitude and longitude description.',
    )

    class Meta:
        verbose_name='Lookup: Lat/Long Description'


class tlkpLatLongMethods(BaseRMPModel):
    Primary_Key = CopyFromIntegerField(
        primary_key=True,
    )
    Method_Code = CopyFromCharField(
        max_length=2,
        unique=True,
    )
    Method_Desc = CopyFromCharField(
        max_length=83
    )

    class Meta:
        verbose_name='Lookup: Lat/Long Method'


class tlkpNAICS(BaseRMPModel):
    NAICS_CODE = CopyFromCharField(
        primary_key=True,
        max_length=6,
        verbose_name='NAICS Code',
        help_text='The 5- or 6- digit NAICS code.',
    )
    NAICS_DESCRIPTION = CopyFromCharField(
        max_length=118,
        verbose_name='NAICS Description',
        help_text='Description text for the NAICS code.',
    )

    class Meta:
        verbose_name = 'Lookup: NAICS codes'


class tlkpPhysicalStateCodes(BaseRMPModel):
    LookupCode = CopyFromCharField(
        primary_key=True,
        max_length=1,
        help_text='Physical State description.',
    )
    Description = CopyFromCharField(
        max_length=30,
        help_text='System generated Unique Primary key.',
    )

    class Meta:
        verbose_name='Lookup: Physical State Code'


class tlkpRejectReason(BaseRMPModel):
    LookupCode = CopyFromCharField(
        primary_key=True,
        max_length=1,
        help_text='System generated Unique Primary key.',
    )
    Description = CopyFromCharField(
        max_length=59,
        help_text='Rejection Reason descriptions.',
    )

    class Meta:
        verbose_name='Lookup: Reject Reason'


class tlkpS2ScenarioCodes(BaseRMPModel):
    LookupCode = CopyFromCharField(
        primary_key=True,
        max_length=1,
        help_text='System generated Unique Primary key.',
    )
    Description = CopyFromCharField(
        max_length=27,
        help_text='Pick-list text.',
    )

    class Meta:
        verbose_name='Lookup: Toxics Scenario Code'


class tlkpS6InitiatingEvents(BaseRMPModel):
    LookupCode = CopyFromCharField(
        primary_key=True,
        max_length=1,
        help_text='System generated Unique Primary key.',
    )
    Description = CopyFromCharField(
        max_length=40,
        help_text='Pick-list text.',
    )

    class Meta:
        verbose_name='Lookup: Initiating Events'


class tlkpStateFIPSCodes(BaseRMPModel):
    STATE_CODE = CopyFromCharField(
        max_length=2,
        unique=True,
        help_text='Federal Information Processing Standard (FIPS) code for the'
                  ' county in which the facility is located.'

    )
    STATE_ABBR = CopyFromCharField(
        primary_key=True,
        unique=True,
        max_length=2,
        help_text='The U.S. Postal Service abbreviation for the state in which'
                  ' the facility is located.',
    )
    STATE_NAME = CopyFromCharField(
        max_length=30,
        help_text='The state in which the facility is located.',
    )
    REGION = CopyFromCharField(
        help_text='The code which represents the EPA Region in which the state'
                  ' resides.',
        max_length=2,
    )

    class Meta:
        verbose_name='Lookup: State FIPS codes'


class tlkpSubmissionReasonCodes(BaseRMPModel):
    LookupCode = CopyFromCharField(
        primary_key=True,
        max_length=3,
        help_text='System generated Unique Primary key.',
    )
    Description = CopyFromCharField(
        max_length=101,
        help_text='Submission Reason descriptions.',
    )

    class Meta:
        verbose_name='Lookup: Submission Reason Code'


class tlkpTopographyCode(BaseRMPModel):
    LookupCode = CopyFromCharField(
        primary_key=True,
        max_length=1,
        help_text='System generated Unique Primary key.',
    )
    Description = CopyFromCharField(
        max_length=5,
        help_text='A code representing whether the local topography is urban or rural.',
    )

    class Meta:
        verbose_name='Lookup: Topography Code'


class tlkpWindSpeedUnitCodes(BaseRMPModel):
    LookupCode = CopyFromCharField(
        primary_key=True,
        max_length=1,
        help_text='System generated Unique Primary key.',
    )
    Description = CopyFromCharField(
        max_length=13,
        help_text='Wind Speed Unit Descriptions.',
    )

    class Meta:
        verbose_name='Lookup: Wind Speed Unit Codes'
