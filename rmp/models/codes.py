"""
Code-related RMP data models.
"""
from django.db import models
from .choices import (
    CHEMICAL_TYPE_CHOICES,
)


class ChemCd(models.Model):
    chemical_id = models.IntegerField(
        primary_key=True,
        help_text="RMP's unique identifier of a chemical substance.",
    )
    chemical_name = models.CharField(
        max_length=92,
        help_text="Chemical substance name.",
    )
    cas2 = models.CharField(
        max_length=10,
        blank=True,
        help_text="Chemical Abstracts Service (CAS) registry number "
                  "(is 2 meaningful?)",
    )
    threshold = models.IntegerField(
        help_text='Threshold above which the chemical is regulated???'
    )
    chemical_type = models.CharField(
        max_length=1,
        choices=CHEMICAL_TYPE_CHOICES,
        blank=True,
        help_text='"The type of chemical (T=toxic, F=Flammable).',
    )
    cbi_flag = models.BooleanField(
        help_text='Indicates whether this record contained Confidential '
                  'Business Information (CBI) which has been erased by EPA '
                  'from the public version of the data.'
    )
    chemical_owner = models.CharField(
        max_length=3,
        blank=True,
    )

    class Meta:
        db_table = 'rmp_chem_cd'


class DeregCd(models.Model):
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

    class Meta:
        db_table = 'rmp_dereg_cd'


class DochanCd(models.Model):
    dochan = models.CharField(
        primary_key=True,
        max_length=1,
    )
    dochan_tr = models.CharField(
        max_length=1,
    )

    class Meta:
        db_table = 'rmp_dochan_cd'


class DoctypCd(models.Model):
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

    class Meta:
        db_table = 'rmp_doctyp_cd'


class EventsCd(models.Model):
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

    class Meta:
        db_table = 'rmp_events_cd'


class LldescCd(models.Model):
    lldesc = models.CharField(
        primary_key=True,
        max_length=2,
    )
    lldesc_tr = models.CharField(
        max_length=36,
    )

    class Meta:
        db_table = 'rmp_lldesc_cd'


class LlmethCd(models.Model):
    primary_key = models.IntegerField(
        primary_key=True
    )
    llmeth = models.CharField(
        max_length=2
    )
    llmeth_tr = models.CharField(
        max_length=83
    )

    class Meta:
        db_table = 'rmp_llmeth_cd'


class PhysCd(models.Model):
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

    class Meta:
        db_table = 'rmp_phys_cd'


class RejectCd(models.Model):
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

    class Meta:
        db_table = 'rmp_reject_cd'


class ScenCd(models.Model):
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

    class Meta:
        db_table = 'rmp_scen_cd'


class SubmitCd(models.Model):
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

    class Meta:
        db_table = 'rmp_submit_cd'


class TopoCd(models.Model):
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

    class Meta:
        db_table = 'rmp_topo_cd'


class WindCd(models.Model):
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

    class Meta:
        db_table = 'rmp_wind_cd'
