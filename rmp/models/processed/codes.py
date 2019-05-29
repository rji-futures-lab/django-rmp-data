"""
Code-related RMP data models.
"""
from django.db.models import F, PROTECT
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDecimalField,
    CopyFromIntegerField,
    CopyFromForeignKey,
)
from rmp.models import BaseRMPModel
from rmp.models import raw as raw_models
from rmp.models.choices import (
    CHEMICAL_TYPES,
)


class ChemCd(BaseRMPModel):
    id = CopyFromIntegerField(
        source_column='ChemicalID',
        primary_key=True,
        help_text="RMP's unique identifier of a chemical substance.",
    )
    chemical_name = CopyFromCharField(
        max_length=92,
        help_text="Chemical substance name.",
    )
    cas2 = CopyFromCharField(
        source_column='CASNumber',
        max_length=10,
        blank=True,
        help_text="Chemical Abstracts Service (CAS) registry number "
                  "(is 2 meaningful?)",
    )
    threshold = CopyFromDecimalField(
        source_column='threshold',
        null=True,
        decimal_places=1,
        max_digits=8,
        help_text='Threshold above which the chemical is regulated???'
    )
    chemical_type = CopyFromCharField(
        source_column='ChemType',
        max_length=1,
        choices=CHEMICAL_TYPES,
        blank=True,
        help_text='"The type of chemical (T=toxic, F=Flammable).',
    )
    cbi_flag = CopyFromBooleanField(
        source_column='flgCBI',
        help_text='Indicates whether this record contained Confidential '
                  'Business Information (CBI) which has been erased by EPA '
                  'from the public version of the data.'
    )
    chemical_owner = CopyFromCharField(
        source_column='ChemOwner',
        max_length=3,
        blank=True,
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpChemicals

        return m.objects.get_default_transform_queryset()


class CountyCd(BaseRMPModel):
    state_code = CopyFromForeignKey(
        'StateCd',
        on_delete=PROTECT,
        help_text='The U.S. Postal Service abbreviation for the state in which'
                  ' the facility is located.',
        db_column='State_Code',
    )
    county_code = CopyFromCharField(
        max_length=2,
        help_text='Federal Information Processing Standard (FIPS) code for the'
                  ' county in which the facility is located.',
    )
    county_name = CopyFromCharField(
        max_length=30,
        help_text='The name of the county.',
    )
    state_county_code = CopyFromIntegerField(
        primary_key=True,
        help_text='Concatenation of state_code and county_code(?)',
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpCountyFIPSCodes

        return m.objects.get_default_transform_queryset()


class DeregCd(BaseRMPModel):
    """
    Reason for de-regulating a facility.
    """
    dereg = CopyFromIntegerField(
        source_column='LookupCode',
        primary_key=True,
        help_text='Unique identifier of the de-regulation reason.'
    )
    dereg_tr = CopyFromCharField(
        source_column='Description',
        max_length=62,
        help_text='Full description of the de-regulation reason.'
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpDeregistrationReason

        return m.objects.get_default_transform_queryset()


class DochanCd(BaseRMPModel):
    dochan = CopyFromCharField(
        source_column='LookupCode',
        primary_key=True,
        max_length=1,
    )
    dochan_tr = CopyFromCharField(
        source_column='Description',
        max_length=1,
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpDocHandle

        return m.objects.get_default_transform_queryset()


class DoctypCd(BaseRMPModel):
    """
    Type of RMP document.
    """
    doctyp = CopyFromCharField(
        source_column='LookupCode',
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the document type.'
    )
    doctyp_tr = CopyFromCharField(
        source_column='Description',
        max_length=30,
        help_text='Full description of the document type.'
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpDocType

        return m.objects.get_default_transform_queryset()


class EventsCd(BaseRMPModel):
    """
    Type of event.
    """
    events = CopyFromCharField(
        source_column='LookupCode',
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the event type.'
    )
    events_tr = CopyFromCharField(
        source_column='Description',
        max_length=40,
        help_text='Full description of the event type.'
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpS6InitiatingEvents

        return m.objects.get_default_transform_queryset()


class NAICS(BaseRMPModel):
    """
    """
    code = CopyFromCharField(
        primary_key=True,
        max_length=6,
        verbose_name='NAICS Code',
        help_text='The 5- or 6- digit NAICS code.',
    )
    description = CopyFromCharField(
        max_length=118,
        verbose_name='NAICS Description',
        help_text='Description text for the NAICS code.',
    )

    class Meta:
        verbose_name = 'Lookup: NAICS codes'

    @classmethod
    def get_transform_queryset(self):
        qs = raw_models.tlkpNAICS.objects.annotate(
            code=F("NAICS_CODE"),
            description=F("NAICS_DESCRIPTION"),
        )

        return qs


class LldescCd(BaseRMPModel):
    lldesc = CopyFromCharField(
        source_column='Feat_Code',
        primary_key=True,
        max_length=2,
    )
    lldesc_tr = CopyFromCharField(
        source_column='Feat_Desc',
        max_length=36,
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpLatLongDescriptions

        return m.objects.get_default_transform_queryset()


class LlmethCd(BaseRMPModel):
    llmeth = CopyFromCharField(
        primary_key=True,
        source_column='Method_Code',
        max_length=2,
    )
    llmeth_tr = CopyFromCharField(
        source_column='Method_Desc',
        max_length=83
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpLatLongMethods

        return m.objects.get_default_transform_queryset()


class PhysCd(BaseRMPModel):
    """
    Physical state
    """
    phys = CopyFromCharField(
        source_column='LookupCode',
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the physical state.'
    )
    phys_tr = CopyFromCharField(
        source_column='Description',
        max_length=30,
        help_text='Full description of the physical state.'
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpPhysicalStateCodes

        return m.objects.get_default_transform_queryset()


class RejectCd(BaseRMPModel):
    """
    Reason an RMP submission may be rejected.
    """
    reject = CopyFromCharField(
        source_column='LookupCode',
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the rejection reason.'
    )
    reject_tr = CopyFromCharField(
        source_column='Description',
        max_length=59,
        help_text='Full description of the rejection reason.'
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpRejectReason

        return m.objects.get_default_transform_queryset()


class ScenCd(BaseRMPModel):
    """
    Accident(?) scenario.
    """
    scen = CopyFromCharField(
        source_column='LookupCode',
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the scenario.'
    )
    scen_tr = CopyFromCharField(
        source_column='Description',
        max_length=27,
        help_text='Full description of the scenario.'
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpS2ScenarioCodes

        return m.objects.get_default_transform_queryset()


class SubmitCd(BaseRMPModel):
    """
    Reason for an RMP submission.
    """
    submit = CopyFromCharField(
        source_column='LookupCode',
        primary_key=True,
        max_length=3,
        help_text='Unique identifier of the submission reason.'
    )
    submit_tr = CopyFromCharField(
        source_column='Description',
        max_length=101,
        help_text='Full description of the submission reason.'
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpSubmissionReasonCodes

        return m.objects.get_default_transform_queryset()


class StateCd(BaseRMPModel):
    code = CopyFromCharField(
        max_length=2,
        unique=True,
        help_text='Federal Information Processing Standard (FIPS) code for the'
                  ' county in which the facility is located.'
    )
    abbr = CopyFromCharField(
        primary_key=True,
        unique=True,
        max_length=2,
        help_text='The U.S. Postal Service abbreviation for the state in which'
                  ' the facility is located.',
    )
    name = CopyFromCharField(
        max_length=30,
        help_text='The state in which the facility is located.',
    )
    region = CopyFromCharField(
        help_text='The code which represents the EPA Region in which the state'
                  ' resides.',
        max_length=2,
    )

    @classmethod
    def get_transform_queryset(self):

        qs = raw_models.tlkpStateFIPSCodes.objects.annotate(
            code=F('STATE_CODE'),
            abbr=F('STATE_ABBR'),
            name=F('STATE_NAME'),
            region=F('REGION'),
        )

        return qs


class TopoCd(BaseRMPModel):
    """
    Type of topography(?).
    """
    topo = CopyFromCharField(
        source_column='LookupCode',
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the topography type.'
    )
    topo_tr = CopyFromCharField(
        source_column='Description',
        max_length=5,
        help_text='Full description of the topography type.'
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpTopographyCode

        return m.objects.get_default_transform_queryset()


class WindCd(BaseRMPModel):
    """
    Wind speed measurement unit.
    """
    wind = CopyFromCharField(
        source_column='LookupCode',
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the wind speed measurement unit.'
    )
    wind_tr = CopyFromCharField(
        source_column='Description',
        max_length=13,
        help_text='Full description of the wind speed measurement unit.'
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tlkpWindSpeedUnitCodes

        return m.objects.get_default_transform_queryset()
