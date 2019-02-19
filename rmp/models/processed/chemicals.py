"""
Models for processed RMP data.
"""
import os
from django.conf import settings
from django.db import models
from django.db.models import F, Max, OuterRef, Subquery, Sum, Count, Case, When, Value
from rmp.fields import (
    CopyFromBigIntegerField,
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDateField,
    CopyFromDateTimeField,
    CopyFromDecimalField,
    CopyFromForeignKey,
    CopyFromIntegerField,
    CopyFromOneToOneField,
    CopyFromTextField,
    CopyFromFloatField,
)
from rmp.models import raw as raw_models
from rmp.models import processed as processed_models
from rmp.models.base import BaseRMPModel


class FlammablesAltRelease(BaseRMPModel):
    flammable_id = CopyFromIntegerField(
        primary_key=True,
        source_column='flammable_id'
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.CASCADE,
        source_column='process_chemical_id'
    )
    analytical_basis = CopyFromCharField(max_length=255, blank=True)
    scenario = CopyFromCharField(max_length=200)
    quantity_released = CopyFromDecimalField(
        max_digits=5,
        decimal_places=2,
        # source_column='quantity_lbs',
        null=True,
    )
    endpoint_used = CopyFromCharField(max_length=30, blank=True)
    lfl_value = CopyFromDecimalField(
        max_digits=5, decimal_places=1, null=True,
    )
    endpoint_distance = CopyFromDecimalField(
        source_column="distance2_endpoint",
        max_digits=5,
        decimal_places=1,
        null=True,
    )
    population = CopyFromCharField(
        source_column="residential_population",
        max_length=9,
        blank=True,
        verbose_name='Residential population',
    )
    pr_schools = CopyFromBooleanField()
    pr_residences = CopyFromBooleanField()
    pr_hospitals = CopyFromBooleanField()
    pr_prisons = CopyFromBooleanField()
    pr_public_recreation = CopyFromBooleanField()
    pr_comm_ind = CopyFromBooleanField()
    pr_other_type = CopyFromCharField(
        max_length=200, blank=True
    )
    er_natl_state_parks = CopyFromBooleanField()
    er_wildlife_sactuary = CopyFromBooleanField()
    er_fed_wilderness = CopyFromBooleanField()
    er_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    pm_dikes = CopyFromBooleanField()
    pm_firewalls = CopyFromBooleanField(source_column='pm_fire_walls')
    pm_blastwalls = CopyFromBooleanField(source_column='pm_blast_walls')
    pm_enclosures = CopyFromBooleanField()
    pm_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    am_sprinklers = CopyFromBooleanField(source_column='am_sprinkler_systems')
    am_deluge_systems = CopyFromBooleanField()
    am_watercurtain = CopyFromBooleanField(source_column='am_water_curtain')
    am_excess_flowvalve = CopyFromBooleanField(source_column='am_excess_flow_valve')
    am_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    ptrgraphic = CopyFromCharField(
        source_column='ptr_graphic',
        max_length=12,
        blank=True,
    )
    cbi_flag = CopyFromBooleanField()

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tblS5FlammablesAltReleases

        return m.objects.get_default_transform_queryset()


class ToxicsAltRelease(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='toxic_id',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.CASCADE,
    )
    percent_weight = CopyFromDecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
    )
    physical_state = CopyFromCharField(max_length=1, blank=True)
    analytical_basis = CopyFromCharField(max_length=255, blank=True)
    scenario = CopyFromCharField(max_length=200)
    quantity_released = CopyFromDecimalField(
        max_digits=5,
        decimal_places=2,
        source_column='quantity_lbs',
        null=True,
    )
    release_duration = CopyFromDecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    release_rate = CopyFromBooleanField(null=True)
    wind_speed = CopyFromDecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
    )
    stability_class = CopyFromCharField(max_length=1, blank=True)
    topography = CopyFromCharField(max_length=1, blank=True)
    endpoint_distance = CopyFromDecimalField(
        max_digits=5, decimal_places=1, null=True,
    )
    population = CopyFromCharField(
        max_length=9, blank=True, verbose_name='Residential population'
    )
    pr_schools = CopyFromBooleanField()
    pr_residences = CopyFromBooleanField()
    pr_hospitals = CopyFromBooleanField()
    pr_prisons = CopyFromBooleanField()
    pr_public_recreation = CopyFromBooleanField(
        source_column='pr_public_rec'
    )
    pr_comm_ind = CopyFromBooleanField()
    pr_other_type = CopyFromCharField(
        max_length=200, blank=True, source_column='pr_othertype',
    )
    er_natl_state_parks = CopyFromBooleanField(
        source_column='er_natlstateparks'
    )
    er_wildlife_sactuary = CopyFromBooleanField(
        source_column='er_wildlifesanct'
    )
    er_fed_wilderness = CopyFromBooleanField(
        source_column='er_fedwilderness'
    )
    er_other_type = CopyFromCharField(
        max_length=200, blank=True, source_column='er_othertype'
    )
    pm_dikes = CopyFromBooleanField()
    pm_enclosures = CopyFromBooleanField()
    pm_berms = CopyFromBooleanField()
    pm_drains = CopyFromBooleanField()
    pm_sumps = CopyFromBooleanField()
    pm_other_type = CopyFromCharField(
        max_length=200, blank=True, source_column='pm_othertype'
    )
    am_sprinklers = CopyFromBooleanField()
    am_deluge_systems = CopyFromBooleanField(
        source_column='am_delugesystems'
    )
    am_watercurtain = CopyFromBooleanField()
    am_neutralization = CopyFromBooleanField()
    am_excess_flowvalve = CopyFromBooleanField(
        source_column='am_excessflowvalve'
    )
    am_flares = CopyFromBooleanField()
    am_scrubbers = CopyFromBooleanField()
    am_emergency_shutdown = CopyFromBooleanField(
        source_column='am_emerg_shutdown'
    )
    am_other_type = CopyFromCharField(
        max_length=200, blank=True, source_column='am_othertype'
    )
    ptrgraphic = CopyFromCharField(max_length=12, blank=True)
    cbi_flag = CopyFromBooleanField()

    source_file = 'rmp_alt_tox'

class ToxicsWorstCase(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='toxic_id',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.CASCADE
    )
    percent_weight = CopyFromDecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
    )
    # percent_weight = CopyFromCharField(max_length=7)
    physical_state = CopyFromCharField(max_length=1, blank=True)
    analytical_basis = CopyFromCharField(max_length=255, blank=True)
    scenario = CopyFromCharField(max_length=1, blank=True)
    # quantity_lbs = CopyFromDecimalField(max_digits=6, decimal_places=2, blank=True)
    quantity_lbs = CopyFromCharField(max_length=4, blank=True)
    # release_duration = CopyFromDecimalField(max_digits=7, decimal_places=2, blank=True)
    release_duration = CopyFromCharField(max_length=7, blank=True)
    # release_rate = CopyFromDecimalField(max_digits=4, decimal_places=1, blank=True)
    release_rate = CopyFromCharField(max_length=7, blank=True)
    wind_speed = CopyFromDecimalField(max_digits=4, decimal_places=1, blank=True)
    stability_class = CopyFromCharField(max_length=1, blank=True)
    topography = CopyFromCharField(max_length=1, blank=True)
    # endpoint_distance = CopyFromDecimalField(max_digits=5, decimal_places=1)
    endpoint_distance = CopyFromCharField(max_length=4, blank=True)
    population = CopyFromCharField(max_length=9, blank=True)
    pr_schools = CopyFromBooleanField()
    pr_residences = CopyFromBooleanField()
    pr_hospitals = CopyFromBooleanField()
    pr_prisons = CopyFromBooleanField()
    pr_public_rec= CopyFromBooleanField()
    pr_comm_ind = CopyFromBooleanField()
    pr_othertype = CopyFromCharField(max_length=200, blank=True)
    er_natlstateparks = CopyFromBooleanField()
    er_wildlifesanct = CopyFromBooleanField()
    er_fedwilderness = CopyFromBooleanField()
    er_othertype = CopyFromCharField(max_length=200, blank=True)
    pm_dikes = CopyFromBooleanField()
    pm_enclosures = CopyFromBooleanField()
    pm_berms = CopyFromBooleanField()
    pm_drains = CopyFromBooleanField()
    pm_sumps = CopyFromBooleanField()
    pm_othertype = CopyFromCharField(max_length=200, blank=True)
    ptrgraphic = CopyFromCharField(max_length=12, blank=True)
    cbi_flag = CopyFromBooleanField()

    source_file = 'rmp_worst_tox'

#NULLs in two numberical fields and also blank
class FlammablesWorstCase(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='flammable_id',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.CASCADE
    )
    analytical_basis = CopyFromCharField(max_length=255, blank=True)
    # quantity_lbs = CopyFromDecimalField(max_digits=6, decimal_places=2, blank=True)
    # endpoint_distance = CopyFromDecimalField(max_digits=5, decimal_places=1)
    quantity_lbs = CopyFromCharField(max_length=20, blank=True)
    endpoint_distance = CopyFromCharField(max_length=20, blank=True)
    population = CopyFromCharField(max_length=9, blank=True)
    pr_schools = CopyFromBooleanField()
    pr_residences = CopyFromBooleanField()
    pr_hospitals = CopyFromBooleanField()
    pr_prisons = CopyFromBooleanField()
    pr_public_rec = CopyFromBooleanField()
    pr_comm_ind = CopyFromBooleanField()
    pr_othertype = CopyFromCharField(max_length=200, blank=True)
    er_natlstateparks = CopyFromBooleanField()
    er_wildlife_sanct = CopyFromBooleanField()
    er_fedwilderness = CopyFromBooleanField()
    er_othertype = CopyFromCharField(max_length=200, blank=True)
    pm_blastwalls = CopyFromBooleanField()
    pm_othertype = CopyFromCharField(max_length=200, blank=True)
    ptrgraphic = CopyFromCharField(max_length=12, blank=True)
    cbi_flag = CopyFromBooleanField()

    source_file = 'rmp_worst_flam'
