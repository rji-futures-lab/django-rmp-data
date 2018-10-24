"""
Code-related RMP data models.
"""
from django.db import models
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDecimalField,
    CopyFromIntegerField,
)
from rmp.models import BaseRMPModel
from rmp.models.choices import (
    CHEMICAL_TYPE_CHOICES,
)


class ChemCd(BaseRMPModel):
    chemical_id = CopyFromIntegerField(
        source_column='ChemicalID',
        primary_key=True,
        help_text="RMP's unique identifier of a chemical substance.",
    )
    chemical_name = CopyFromCharField(
        source_column='ChemicalName',
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
        source_column='Threshold',
        null=True,
        decimal_places=1,
        max_digits=8,
        help_text='Threshold above which the chemical is regulated???'
    )
    chemical_type = CopyFromCharField(
        source_column='ChemType',
        max_length=1,
        choices=CHEMICAL_TYPE_CHOICES,
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

    source_file = 'tlkpChemicals'


class DeregCd(BaseRMPModel):
    """
    Reason for de-regulating a facility.
    """
    dereg = models.IntegerField(
        primary_key=True,
        help_text='Unique identifier of the de-regulation reason.'
    )
    dereg_tr = models.CharField(
        max_length=62,
        help_text='Full description of the de-regulation reason.'
    )

    source_file = 'rmp_dereg_cd'


class DochanCd(BaseRMPModel):
    dochan = models.CharField(
        primary_key=True,
        max_length=1,
    )
    dochan_tr = models.CharField(
        max_length=1,
    )

    source_file = 'rmp_dochan_cd'


class DoctypCd(BaseRMPModel):
    """
    Type of RMP document.
    """
    doctyp = models.CharField(
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the document type.'
    )
    doctyp_tr = models.CharField(
        max_length=30,
        help_text='Full description of the document type.'
    )

    source_file = 'rmp_doctyp_cd'


class EventsCd(BaseRMPModel):
    """
    Type of event.
    """
    events = models.CharField(
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the event type.'
    )
    events_tr = models.CharField(
        max_length=40,
        help_text='Full description of the event type.'
    )

    source_file = 'rmp_events_cd'


class LldescCd(BaseRMPModel):
    lldesc = models.CharField(
        primary_key=True,
        max_length=2,
    )
    lldesc_tr = models.CharField(
        max_length=36,
    )

    source_file = 'rmp_lldesc_cd'


class LlmethCd(BaseRMPModel):
    primary_key = models.IntegerField(
        primary_key=True
    )
    llmeth = models.CharField(
        max_length=2
    )
    llmeth_tr = models.CharField(
        max_length=83
    )

    source_file = 'rmp_llmeth_cd'


class PhysCd(BaseRMPModel):
    """
    Physical state?
    """
    phys = models.CharField(
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the physical state.'
    )
    phys_tr = models.CharField(
        max_length=30,
        help_text='Full description of the physical state.'
    )

    source_file = 'rmp_phys_cd'


class RejectCd(BaseRMPModel):
    """
    Reason an RMP submission may be rejected.
    """
    reject = models.CharField(
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the rejection reason.'
    )
    reject_tr = models.CharField(
        max_length=59,
        help_text='Full description of the rejection reason.'
    )

    source_file = 'rmp_reject_cd'


class ScenCd(BaseRMPModel):
    """
    Accident(?) scenario.
    """
    scen = models.CharField(
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the scenario.'
    )
    scen_tr = models.CharField(
        max_length=27,
        help_text='Full description of the scenario.'
    )

    source_file = 'rmp_scen_cd'


class SubmitCd(BaseRMPModel):
    """
    Reason for an RMP submission.
    """
    submit = models.CharField(
        primary_key=True,
        max_length=3,
        help_text='Unique identifier of the submission reason.'
    )
    submit_tr = models.CharField(
        max_length=101,
        help_text='Full description of the submission reason.'
    )

    source_file = 'rmp_submit_cd'


class TopoCd(BaseRMPModel):
    """
    Type of topography(?).
    """ 
    topo = models.CharField(
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the topography type.'
    )
    topo_tr = models.CharField(
        max_length=5,
        help_text='Full description of the topography type.'
    )

    source_file = 'rmp_topo_cd'


class City(BaseRMPModel):
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=2, blank=True)
    num_fac = models.IntegerField()

    source_file = 'rmp_cities_cd'


class WindCd(BaseRMPModel):
    """
    Wind speed measurement unit.
    """
    wind = models.CharField(
        primary_key=True,
        max_length=1,
        help_text='Unique identifier of the wind speed measurement unit.'
    )
    wind_tr = models.CharField(
        max_length=13,
        help_text='Full description of the wind speed measurement unit.'
    )

    source_file = 'rmp_wind_cd'
