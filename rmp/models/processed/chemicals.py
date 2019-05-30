"""
Models for processed RMP data.
"""
import os
from django.conf import settings
from django.db import models
from django.db.models import (
    F, Max, OuterRef, Subquery, Sum, Count, Case, When, Value
)
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
    analytical_basis = CopyFromCharField(
        max_length=255,
        blank=True,
    )
    scenario = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    quantity_released = CopyFromDecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    endpoint_used = CopyFromCharField(
        max_length=30,
        blank=True,
    )
    lfl_value = CopyFromDecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
    )
    endpoint_distance = CopyFromDecimalField(
        source_column="distance2_endpoint",
        max_digits=5,
        decimal_places=1,
        null=True,
    )
    population = CopyFromIntegerField(
        source_column="residential_population",
        null=True,
        verbose_name='Residential population',
    )
    pr_schools = CopyFromBooleanField(
        verbose_name='Schools'
    )
    pr_residences = CopyFromBooleanField(
        verbose_name='Residences'
    )
    pr_hospitals = CopyFromBooleanField(
        verbose_name='Hospitals'
    )
    pr_prisons = CopyFromBooleanField(
        verbose_name='Prisons/Correctional Facilities'
    )
    pr_public_recreation= CopyFromBooleanField(
        verbose_name='Recreation Areas'
    )
    pr_comm_ind = CopyFromBooleanField(
        verbose_name='Major Commercial, office, industrial areas'
    )
    pr_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    er_natl_state_parks = CopyFromBooleanField(
        verbose_name='National or state parks, forests, or monuments',
    )
    er_wildlife_sactuary = CopyFromBooleanField(
        verbose_name='Officially designated wildlife sanctuaries, preserves, or refuges',
    )
    er_fed_wilderness = CopyFromBooleanField(
        verbose_name='Federal wilderness area',
    )
    er_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    pm_dikes = CopyFromBooleanField(
        verbose_name='Dikes',
    )
    pm_firewalls = CopyFromBooleanField(
        source_column='pm_fire_walls',
        verbose_name='Fire wall',
    )
    pm_blastwalls = CopyFromBooleanField(
        source_column='pm_blast_walls',
        verbose_name='Blast walls',
    )
    pm_enclosures = CopyFromBooleanField(
        verbose_name='Enclosures',
    )
    pm_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    am_sprinklers = CopyFromBooleanField(
        source_column='am_sprinkler_systems',
    )
    am_deluge_systems = CopyFromBooleanField(
        verbose_name='Deluge systems',
    )
    am_watercurtain = CopyFromBooleanField(
        source_column='am_water_curtain',
        verbose_name='Water curtain',
    )
    am_excess_flowvalve = CopyFromBooleanField(
        source_column='am_excess_flow_valve',
        verbose_name='Excess flow valve',
    )
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

    @property
    def public_receptors_within_distance(self):

        self._public_receptors_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pr_')
            if self.__dict__[f.name]
        ]

        if self.pr_other_type != '':
            self._public_receptors_within_distance.append(
                self.pr_other_type
            )

        return self._public_receptors_within_distance
    
    @property
    def public_receptors_not_within_distance(self):

        self._public_receptors_not_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pr_')
            if not self.__dict__[f.name]
        ]

        return self._public_receptors_not_within_distance

    @property
    def environmental_receptors_within_distance(self):

        self._environmental_receptors_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('er_')
            if self.__dict__[f.name]
        ]

        if self.er_other_type != '':
            self._environmental_receptors_within_distance.append(
                self.er_other_type
            )

        return self._environmental_receptors_within_distance
    
    @property
    def environmental_receptors_not_within_distance(self):

        self._environmental_receptors_not_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('er_')
            if not self.__dict__[f.name]
        ]

        return self._environmental_receptors_not_within_distance

    @property
    def passive_mitigation_considered(self):

        self._passive_mitigation_considered = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pm_')
            if self.__dict__[f.name]
        ]

        if self.er_other_type != '':
            self._passive_mitigation_considered.append(
                self.pm_other_type
            )

        return self._passive_mitigation_considered
    
    @property
    def passive_mitigation_not_considered(self):

        self._passive_mitigation_not_considered = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pm_')
            if not self.__dict__[f.name]
        ]

        return self._passive_mitigation_not_considered

    @property
    def active_mitigation_considered(self):

        self._active_mitigation_considered = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('am_')
            if self.__dict__[f.name]
        ]

        if self.er_other_type != '':
            self._active_mitigation_considered.append(
                self.pm_other_type
            )

        return self._active_mitigation_considered
    
    @property
    def active_mitigation_not_considered(self):

        self._active_mitigation_not_considered = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('am_')
            if not self.__dict__[f.name]
        ]

        return self._active_mitigation_not_considered    


class ToxicsAltRelease(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='toxic_id',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.CASCADE,
        source_column='ProcessChemicalID',
    )
    percent_weight = CopyFromDecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
    )
    physical_state = CopyFromForeignKey(
        "PhysCd",
        on_delete=models.PROTECT,
        db_column='physical_state',
        null=True,
    )
    analytical_basis = CopyFromCharField(
        max_length=255,
        blank=True,
    )
    scenario = CopyFromForeignKey(
        "ScenCd",
        on_delete=models.PROTECT,
        db_column='scenario',
        null=True,
    )
    quantity_released = CopyFromDecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    release_duration = CopyFromDecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    release_rate = CopyFromBooleanField(
        null=True,
    )
    wind_speed = CopyFromDecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
    )
    stability_class = CopyFromCharField(
        max_length=1,
        blank=True,
    )
    topography = CopyFromForeignKey(
        "TopoCd",
        on_delete=models.PROTECT,
        db_column='topography',
        null=True,
    )
    endpoint_distance = CopyFromDecimalField(
        source_column='distance2_endpoint',
        max_digits=5,
        decimal_places=1,
        null=True,
    )
    residential_population = CopyFromIntegerField(
        null=True,
        verbose_name='Residential population',
    )
    pr_schools = CopyFromBooleanField(
        verbose_name='Schools'
    )
    pr_residences = CopyFromBooleanField(
        verbose_name='Residences'
    )
    pr_hospitals = CopyFromBooleanField(
        verbose_name='Hospitals'
    )
    pr_prisons = CopyFromBooleanField(
        verbose_name='Prisons/Correctional Facilities'
    )
    pr_public_recreation= CopyFromBooleanField(
        verbose_name='Recreation Areas'
    )
    pr_comm_ind = CopyFromBooleanField(
        verbose_name='Major Commercial, office, industrial areas'
    )
    pr_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    er_natl_state_parks = CopyFromBooleanField(
        verbose_name='National or state parks, forests, or monuments',
    )
    er_wildlife_sactuary = CopyFromBooleanField(
        verbose_name='Officially designated wildlife sanctuaries, preserves, or refuges',
    )
    er_fed_wilderness = CopyFromBooleanField(
        verbose_name='Federal wilderness area',
    )
    er_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    pm_dikes = CopyFromBooleanField(
        verbose_name='Dikes',
    )
    pm_enclosures = CopyFromBooleanField(
        verbose_name='Enclosures',
    )
    pm_berms = CopyFromBooleanField(
        verbose_name='Berms',
    )
    pm_drains = CopyFromBooleanField(
        verbose_name='Drains',
    )
    pm_sumps = CopyFromBooleanField(
        verbose_name='Sumps',
    )
    pm_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    am_sprinkler_systems = CopyFromBooleanField(
        verbose_name='Sprinkler systems'
    )
    am_deluge_systems = CopyFromBooleanField(
        verbose_name='Deluge systems'
    )
    am_water_curtain = CopyFromBooleanField(
        verbose_name='Water curtain'
    )
    am_neutralization = CopyFromBooleanField(
        verbose_name='Neutralization'
    )
    am_excess_flow_valve = CopyFromBooleanField(
        verbose_name='Excess flow valve'
    )
    am_flares = CopyFromBooleanField(
        verbose_name='Flares'
    )
    am_scrubbers = CopyFromBooleanField(
        verbose_name='Scrubbers'
    )
    am_emergency_shutdown = CopyFromBooleanField(
        verbose_name='Emergency shutdown'
    )
    am_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    ptr_graphic = CopyFromCharField(
        max_length=12,
        blank=True,
    )
    cbi_flag = CopyFromBooleanField()

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tblS3ToxicsAltReleases

        return m.objects.get_default_transform_queryset()

    @property
    def public_receptors_within_distance(self):

        self._public_receptors_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pr_')
            if self.__dict__[f.name]
        ]

        if self.pr_other_type != '':
            self._public_receptors_within_distance.append(
                self.pr_other_type
            )

        return self._public_receptors_within_distance
    
    @property
    def public_receptors_not_within_distance(self):

        self._public_receptors_not_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pr_')
            if not self.__dict__[f.name]
        ]

        return self._public_receptors_not_within_distance

    @property
    def environmental_receptors_within_distance(self):

        self._environmental_receptors_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('er_')
            if self.__dict__[f.name]
        ]

        if self.er_other_type != '':
            self._environmental_receptors_within_distance.append(
                self.er_other_type
            )

        return self._environmental_receptors_within_distance
    
    @property
    def environmental_receptors_not_within_distance(self):

        self._environmental_receptors_not_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('er_')
            if not self.__dict__[f.name]
        ]

        return self._environmental_receptors_not_within_distance

    @property
    def passive_mitigation_considered(self):

        self._passive_mitigation_considered = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pm_')
            if self.__dict__[f.name]
        ]

        if self.er_other_type != '':
            self._passive_mitigation_considered.append(
                self.pm_other_type
            )

        return self._passive_mitigation_considered
    
    @property
    def passive_mitigation_not_considered(self):

        self._passive_mitigation_not_considered = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pm_')
            if not self.__dict__[f.name]
        ]

        return self._passive_mitigation_not_considered

    @property
    def active_mitigation_considered(self):

        self._active_mitigation_considered = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('am_')
            if self.__dict__[f.name]
        ]

        if self.er_other_type != '':
            self._active_mitigation_considered.append(
                self.pm_other_type
            )

        return self._active_mitigation_considered
    
    @property
    def active_mitigation_not_considered(self):

        self._active_mitigation_not_considered = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('am_')
            if not self.__dict__[f.name]
        ]

        return self._active_mitigation_not_considered


class ToxicsWorstCase(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='toxic_id',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.CASCADE,
        source_column="ProcessChemicalID",
    )
    percent_weight = CopyFromDecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
    )
    physical_state = CopyFromForeignKey(
        "PhysCd",
        on_delete=models.PROTECT,
        db_column='physical_state',
        null=True,
    )
    analytical_basis = CopyFromCharField(
        max_length=255,
        blank=True,
    )
    scenario = CopyFromForeignKey(
        "ScenCd",
        on_delete=models.PROTECT,
        db_column='scenario',
        null=True,
    )
    quantity_released = CopyFromDecimalField(
        max_digits=6, 
        decimal_places=2,
        null=True,
    )
    release_duration = CopyFromDecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
    )
    release_rate = CopyFromDecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
    )
    wind_speed = CopyFromDecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
    )
    stability_class = CopyFromCharField(
        max_length=1,
        blank=True,
    )
    topography = CopyFromForeignKey(
        "TopoCd",
        on_delete=models.PROTECT,
        db_column='topography',
        null=True,
    )
    distance2_endpoint = CopyFromDecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
    )
    residential_population = CopyFromIntegerField(
        null=True,
    )
    pr_schools = CopyFromBooleanField(
        verbose_name='Schools'
    )
    pr_residences = CopyFromBooleanField(
        verbose_name='Residences'
    )
    pr_hospitals = CopyFromBooleanField(
        verbose_name='Hospitals'
    )
    pr_prisons = CopyFromBooleanField(
        verbose_name='Prisons/Correctional Facilities'
    )
    pr_public_recreation= CopyFromBooleanField(
        verbose_name='Recreation Areas'
    )
    pr_comm_ind = CopyFromBooleanField(
        verbose_name='Major Commercial, office, industrial areas'
    )
    pr_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    er_natl_state_parks = CopyFromBooleanField(
        verbose_name='National or state parks, forests, or monuments',
    )
    er_wildlife_sactuary = CopyFromBooleanField(
        verbose_name='Officially designated wildlife sanctuaries, preserves, or refuges',
    )
    er_fed_wilderness = CopyFromBooleanField(
        verbose_name='Federal wilderness area',
    )
    er_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    pm_dikes = CopyFromBooleanField(
        verbose_name='Dikes',
    )
    pm_enclosures = CopyFromBooleanField(
        verbose_name='Enclosures',
    )
    pm_berms = CopyFromBooleanField(
        verbose_name='Berms',
    )
    pm_drains = CopyFromBooleanField(
        verbose_name='Drains',
    )
    pm_sumps = CopyFromBooleanField(
        verbose_name='Sumps',
    )
    pm_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    ptr_graphic = CopyFromCharField(
        max_length=12,
        blank=True,
    )
    cbi_flag = CopyFromBooleanField()

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tblS2ToxicsWorstCase

        return m.objects.get_default_transform_queryset()

    @property
    def public_receptors_within_distance(self):

        self._public_receptors_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pr_')
            if self.__dict__[f.name]
        ]

        if self.pr_other_type != '':
            self._public_receptors_within_distance.append(
                self.pr_other_type
            )

        return self._public_receptors_within_distance
    
    @property
    def public_receptors_not_within_distance(self):

        self._public_receptors_not_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pr_')
            if not self.__dict__[f.name]
        ]

        return self._public_receptors_not_within_distance

    @property
    def environmental_receptors_within_distance(self):

        self._environmental_receptors_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('er_')
            if self.__dict__[f.name]
        ]

        if self.er_other_type != '':
            self._environmental_receptors_within_distance.append(
                self.er_other_type
            )

        return self._environmental_receptors_within_distance
    
    @property
    def environmental_receptors_not_within_distance(self):

        self._environmental_receptors_not_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('er_')
            if not self.__dict__[f.name]
        ]

        return self._environmental_receptors_not_within_distance

    @property
    def passive_mitigation_considered(self):

        self._passive_mitigation_considered = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pm_')
            if self.__dict__[f.name]
        ]

        if self.er_other_type != '':
            self._passive_mitigation_considered.append(
                self.pm_other_type
            )

        return self._passive_mitigation_considered
    
    @property
    def passive_mitigation_not_considered(self):

        self._passive_mitigation_not_considered = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pm_')
            if not self.__dict__[f.name]
        ]

        return self._passive_mitigation_not_considered


class FlammablesWorstCase(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='flammable_id',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.CASCADE,
        source_column='ProcessChemicalID',
    )
    analytical_basis = CopyFromCharField(
        max_length=255,
        blank=True,
    )
    distance2_endpoint = CopyFromDecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
    )
    quantity_released = CopyFromIntegerField(
        null=True,
    )
    residential_population = CopyFromIntegerField(
        null=True,
    )
    pr_schools = CopyFromBooleanField(
        verbose_name='Schools'
    )
    pr_residences = CopyFromBooleanField(
        verbose_name='Residences'
    )
    pr_hospitals = CopyFromBooleanField(
        verbose_name='Hospitals'
    )
    pr_prisons = CopyFromBooleanField(
        verbose_name='Prisons/Correctional Facilities'
    )
    pr_public_recreation= CopyFromBooleanField(
        verbose_name='Recreation Areas'
    )
    pr_comm_ind = CopyFromBooleanField(
        verbose_name='Major Commercial, office, industrial areas'
    )
    pr_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    er_natl_state_parks = CopyFromBooleanField(
        verbose_name='National or state parks, forests, or monuments',
    )
    er_wildlife_sactuary = CopyFromBooleanField(
        verbose_name='Officially designated wildlife sanctuaries, preserves, or refuges',
    )
    er_fed_wilderness = CopyFromBooleanField(
        verbose_name='Federal wilderness area',
    )
    er_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    pm_blast_walls = CopyFromBooleanField(
        verbose_name='Blast walls'
    )
    pm_other_type = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    ptr_graphic = CopyFromCharField(
        max_length=12,
        blank=True,
    )
    cbi_flag = CopyFromBooleanField()

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tblS4FlammablesWorstCase

        return m.objects.get_default_transform_queryset()

    @property
    def public_receptors_within_distance(self):

        self._public_receptors_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pr_')
            if self.__dict__[f.name]
        ]

        if self.pr_other_type != '':
            self._public_receptors_within_distance.append(
                self.pr_other_type
            )

        return self._public_receptors_within_distance
    
    @property
    def public_receptors_not_within_distance(self):

        self._public_receptors_not_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pr_')
            if not self.__dict__[f.name]
        ]

        return self._public_receptors_not_within_distance

    @property
    def environmental_receptors_within_distance(self):

        self._environmental_receptors_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('er_')
            if self.__dict__[f.name]
        ]

        if self.er_other_type != '':
            self._environmental_receptors_within_distance.append(
                self.er_other_type
            )

        return self._environmental_receptors_within_distance
    
    @property
    def environmental_receptors_not_within_distance(self):

        self._environmental_receptors_not_within_distance = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('er_')
            if not self.__dict__[f.name]
        ]

        return self._environmental_receptors_not_within_distance

    @property
    def passive_mitigation_considered(self):

        self._passive_mitigation_considered = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pm_')
            if self.__dict__[f.name]
        ]

        if self.er_other_type != '':
            self._passive_mitigation_considered.append(
                self.pm_other_type
            )

        return self._passive_mitigation_considered
    
    @property
    def passive_mitigation_not_considered(self):

        self._passive_mitigation_not_considered = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pm_')
            if not self.__dict__[f.name]
        ]

        return self._passive_mitigation_not_considered
