"""
Models for processed RMP data.
"""
import os
from django.conf import settings
from django.db import models
from django.db.models import (
    F, Max, OuterRef, Subquery, Sum, Count, Case, When, Value
)
from django.db.models.functions import Cast
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


class PreventionProgram2(BaseRMPModel): #rmp_prevent_2
    id = CopyFromIntegerField(
        primary_key=True,
    )
    process_naics = CopyFromForeignKey(
        'ProcNaics',
        on_delete=models.PROTECT,
        # db_column='process_naics_2',
    )
    safety_review_date = CopyFromDateField(null=True)
    fr_nfpa58 = CopyFromBooleanField(
        verbose_name='NFPA 58',
    )
    fr_osha = CopyFromBooleanField(
        verbose_name='OSHA (Ammonia)',
    )
    fr_astm = CopyFromBooleanField(
        verbose_name='ASTM Standards',
    )
    fr_ansi = CopyFromBooleanField(
        verbose_name='ANSI Standards',
    )
    fr_asme = CopyFromBooleanField(
        verbose_name='ASME Standards',
    )
    fr_none = CopyFromBooleanField(
        verbose_name='None'
    )
    fr_other_type = CopyFromCharField(max_length=200, blank=True)
    fr_comments = CopyFromCharField(max_length=200, blank=True)
    hazard_review_date = CopyFromDateField(null=True)
    change_completion_date = CopyFromDateField(null=True)
    mh_toxic_release = CopyFromBooleanField(
        verbose_name='Toxic Release',
    )
    mh_fire = CopyFromBooleanField(
        verbose_name='Fire',
    )
    mh_explosion = CopyFromBooleanField(
        verbose_name='Explosion',
    )
    mh_runaway_reaction = CopyFromBooleanField(
        verbose_name='Runaway reaction',
    )
    mh_polymerization = CopyFromBooleanField(
        verbose_name='Polymerization',
    )
    mh_overpressurization = CopyFromBooleanField(
        verbose_name='Overpressurization',
    )
    mh_corrosion = CopyFromBooleanField(
        verbose_name='Corrosion'
    )
    mh_overfilling = CopyFromBooleanField(
        verbose_name='Overfilling',
    )
    mh_contamination = CopyFromBooleanField(
        verbose_name='Contamination',
    )
    mh_equipment_failure = CopyFromBooleanField(
        verbose_name='Equipment failure'
    )
    mh_cooling_loss = CopyFromBooleanField(
        verbose_name='Cooling loss',
    )
    mh_earthquake = CopyFromBooleanField(
        verbose_name = 'Earthquake'
    )
    mh_floods = CopyFromBooleanField(
        verbose_name = 'Floods',
    )
    mh_tornado = CopyFromBooleanField(
        verbose_name = 'Tornado',
    )
    mh_hurricanes = CopyFromBooleanField(
        verbose_name = 'Hurricanes',
    )
    mh_other_type = CopyFromCharField(max_length=200, blank=True)
    pc_vents = CopyFromBooleanField(
        verbose_name='Vents',
    )
    pc_relief_valves = CopyFromBooleanField(
        verbose_name='Relief Valves',
    )
    pc_check_valves = CopyFromBooleanField(
        verbose_name='Check Valves',
    )
    pc_scrubbers = CopyFromBooleanField(
        verbose_name='Scrubbers',
    )
    pc_flares = CopyFromBooleanField(
        verbose_name='Flares',
    )
    pc_manual_shutoffs = CopyFromBooleanField(
        verbose_name='Manual Shutoffs',
    )
    pc_automatic_shutoffs = CopyFromBooleanField(
        verbose_name='Automatic Shutoffs',
    )
    pc_interlocks = CopyFromBooleanField(
        verbose_name='Interlocks',
    )
    pc_alarms = CopyFromBooleanField(
        verbose_name='Alarms',
    )
    pc_keyed_bypass = CopyFromBooleanField(
        verbose_name='Keyed Bypass',
    )
    pc_emergency_air_supply = CopyFromBooleanField(
        verbose_name='Emergency Air Supply',
    )
    pc_emergency_power = CopyFromBooleanField(
        verbose_name='Emergency Power',
    )
    pc_backup_pump = CopyFromBooleanField(
        verbose_name='Backup Pump',
    )
    pc_grounding_equipment = CopyFromBooleanField(
        verbose_name='Grounding Equipment',
    )
    pc_inhibitor_addition = CopyFromBooleanField(
        verbose_name='Inhibitor Addition',
    )
    pc_rupture_disks = CopyFromBooleanField(
        verbose_name='Rupture Disks',
    )
    pc_excess_flow_device = CopyFromBooleanField(
        verbose_name='Excess Flow Device',
    )
    pc_quench_system = CopyFromBooleanField(
        verbose_name='Quench System',
    )
    pc_purge_system = CopyFromBooleanField(
        verbose_name='Purge System',
    )
    pc_none = CopyFromBooleanField(
        verbose_name='None',
    )
    pc_other_type = CopyFromCharField(max_length=200, blank=True)
    ms_sprinkler_system = CopyFromBooleanField(
        verbose_name='Sprinkler System',
    )
    ms_dikes = CopyFromBooleanField(
        verbose_name='Dikes',
    )
    ms_fire_walls = CopyFromBooleanField(
        verbose_name='Fire Walls',
    )
    ms_blast_walls = CopyFromBooleanField(
        verbose_name='Blast Walls',
    )
    ms_deluge_system = CopyFromBooleanField(
        verbose_name='Deluge System',
    )
    ms_water_curtain = CopyFromBooleanField(
        verbose_name='Water Curtain',
    )
    ms_enclosure = CopyFromBooleanField(
        verbose_name='Enclosure',
    )
    ms_neutralization = CopyFromBooleanField(
        verbose_name='Neutralization',
    )
    ms_none = CopyFromBooleanField(
        verbose_name='None',
    )
    ms_other_type = CopyFromCharField(max_length=200, blank=True)
    md_process_area_detectors = CopyFromBooleanField(
        verbose_name='Process Area',
    )
    md_perimeter_monitors = CopyFromBooleanField(
        verbose_name='Perimeter Monitors',
    )
    md_none = CopyFromBooleanField(
        verbose_name='None',
    )
    md_other_type = CopyFromCharField(max_length=200, blank=True)
    ch_chemical_reduction = CopyFromBooleanField(
        verbose_name='Reduced Inventory',
    )
    ch_chemical_increase = CopyFromBooleanField(
        verbose_name='Increased Inventory',
    )
    ch_change_process_parameters = CopyFromBooleanField(
        verbose_name='Process Parameters',
    )
    ch_install_process_controls = CopyFromBooleanField(
        verbose_name='Process Controls',
    )
    ch_install_process_detection = CopyFromBooleanField(
        verbose_name='Process Detection',
    )
    ch_install_perimeter_monitoring = CopyFromBooleanField(
        verbose_name='Perimeter Monitoring',
    )
    ch_install_mitigation_systems = CopyFromBooleanField(
        verbose_name='Mitigation Systems',
    )
    ch_none_required = CopyFromBooleanField(
        verbose_name='None Recommended',
    )
    ch_none = CopyFromBooleanField(
        verbose_name='None',
    )
    ch_other_changes = CopyFromCharField(max_length=200, blank=True)
    op_procedures_review_date = CopyFromDateField(null=True)
    training_review_date = CopyFromDateField(null=True)
    tr_classroom = CopyFromBooleanField(
        verbose_name='Classroom',
    )
    tr_on_the_job = CopyFromBooleanField(
        verbose_name='On the Job',
    )
    tr_other_type = CopyFromCharField(max_length=200, blank=True)
    ct_written_test = CopyFromBooleanField(
        verbose_name='Written Test',
    )
    ct_oral_test = CopyFromBooleanField(
        verbose_name='Oral Test',
    )
    ct_demonstration = CopyFromBooleanField(
        verbose_name='Demonstration',
    )
    ct_observation = CopyFromBooleanField(
        verbose_name='Observation',
    )
    ct_other_type = CopyFromCharField(max_length=200, blank=True)
    maintenance_review_date = CopyFromDateField(null=True)
    equipment_inspection_date = CopyFromDateField(null=True)
    equipment_tested = CopyFromCharField(max_length=200, blank=True)
    compliance_audit_date = CopyFromDateField(null=True)
    audit_completion_date = CopyFromDateField(null=True)
    incident_investigation_date = CopyFromDateField(null=True)
    investigation_change_date = CopyFromDateField(null=True)
    most_recent_change_date = CopyFromDateField(null=True)
    cbi_flag = CopyFromBooleanField()
    description = CopyFromTextField()
    num_prevent_2_chemicals = CopyFromIntegerField(
        help_text='The number of chemicals associated with this prevention '
                  'program record.'
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tblS8PreventionProgram2

        annotations = m.get_renamed_fields()

        annotations['id'] = F('PreventionProgram2ID')
        annotations['process_naics_2'] = F('Process_NAICS_ID')
        annotations['num_prevent_2_chemicals'] = Count('tbls8_prevention_program_chemicals')

        qs = m.objects.annotate(**annotations)

        return qs

    @classmethod
    def get_prefixed_boolean_fields(cls, prefix):

        fields = [
            f for f in cls._meta.get_fields()
            if f.name[0:len(prefix)] == prefix and
            f.name != prefix + 'other_type'
        ]

        return fields

    @property
    def safety_regs(self):

        self._safety_regs = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('fr_')
            if self.__dict__[f.name]
        ]

        if self.fr_other_type != '':
            self._public_receptors_within_distance.append(
                self.fr_other_type
            )

        return self._safety_regs

    @property
    def hazard_identified(self):

        self._hazard_identified = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('mh_')
            if self.__dict__[f.name]
        ]

        if self.mh_other_type != '':
            self._public_receptors_within_distance.append(
                self.mh_other_type
            )

        return self._hazard_identified

    @property
    def process_controls(self):

        self._process_controls = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pc_')
            if self.__dict__[f.name]
        ]

        if self.pc_other_type != '':
            self._public_receptors_within_distance.append(
                self.pc_other_type
            )

        return self._process_controls

    @property
    def mitigation_systems(self):

        self._mitigation_systems = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('ms_')
            if self.__dict__[f.name]
        ]

        if self.ms_other_type != '':
            self._public_receptors_within_distance.append(
                self.ms_other_type
            )

        return self._mitigation_systems

    @property
    def monitoring_systems(self):

        self._monitoring_systems = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('md_')
            if self.__dict__[f.name]
        ]

        if self.md_other_type != '':
            self._public_receptors_within_distance.append(
                self.md_other_type
            )

        return self._monitoring_systems

    @property
    def pha_changes(self):

        self._pha_changes = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('ch_')
            if self.__dict__[f.name]
        ]

        if self.md_other_type != '':
            self._public_receptors_within_distance.append(
                self.md_other_type
            )

        return self._pha_changes

    @property
    def training_type(self):

        self._training_type = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('tr_')
            if self.__dict__[f.name]
        ]

        if self.tr_other_type != '':
            self._public_receptors_within_distance.append(
                self.tr_other_type
            )

        return self._training_type

    @property
    def competency_testing(self):

        self._competency_testing = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('ct_')
            if self.__dict__[f.name]
        ]

        if self.ct_other_type != '':
            self._public_receptors_within_distance.append(
                self.ct_other_type
            )

        return self._competency_testing


class PreventionProgram3(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
    )
    process_naics = CopyFromForeignKey(
        'ProcNaics',
        on_delete=models.PROTECT,
        # db_column='process_naics_3',
    )
    safety_review_date = CopyFromDateField(null=True)
    pha_date = CopyFromDateField(null=True)
    pha_what_if = CopyFromBooleanField(
        verbose_name='What if',
    )
    pha_checklist = CopyFromBooleanField(
        verbose_name='Checklist',
    )
    pha_what_if_checklist = CopyFromBooleanField(
        verbose_name='What if/Checklist',
    )
    pha_hazop = CopyFromBooleanField(
        verbose_name='HAZOP',
    )
    pha_fmea = CopyFromBooleanField(
        verbose_name='FMEA',
    )
    pha_fta = CopyFromBooleanField(
        verbose_name='FTA',
    )
    pha_other_technique = CopyFromCharField(max_length=200, blank=True)
    pha_completion_date = CopyFromDateField(null=True)
    mh_toxic_release = CopyFromBooleanField(
        verbose_name='Toxic release',
    )
    mh_fire = CopyFromBooleanField(
        verbose_name='Fire',
    )
    mh_explosion = CopyFromBooleanField(
        verbose_name='Explosion',
    )
    mh_runaway_reaction = CopyFromBooleanField(
        verbose_name='Runaway reaction',
    )
    mh_polymerization = CopyFromBooleanField(
        verbose_name='Polymerization'
    )
    mh_overpressurization = CopyFromBooleanField(
        verbose_name='Overpressurization'
    )
    mh_corrosion = CopyFromBooleanField(
        verbose_name='Corrosion',
    )
    mh_overfilling = CopyFromBooleanField(
        verbose_name='Overfilling',
    )
    mh_contamination = CopyFromBooleanField(
        verbose_name='Contamination',
    )
    mh_equipment_failure = CopyFromBooleanField(
        verbose_name='Equipment failure'
    )
    mh_cooling_loss = CopyFromBooleanField(
        verbose_name='Cooling loss',
    )
    mh_earthquake = CopyFromBooleanField(
        verbose_name = 'Earthquake'
    )
    mh_floods = CopyFromBooleanField(
        verbose_name = 'Floods',
    )
    mh_tornado = CopyFromBooleanField(
        verbose_name = 'Tornado',
    )
    mh_hurricanes = CopyFromBooleanField(
        verbose_name = 'Hurricanes',
    )
    mh_other_type = CopyFromCharField(max_length=200, blank=True)
    pc_vents = CopyFromBooleanField(
        verbose_name='Vents',
    )
    pc_relief_valves = CopyFromBooleanField(
        verbose_name='Relief Valves',
    )
    pc_check_valves = CopyFromBooleanField(
        verbose_name='Check Valves',
    )
    pc_scrubbers = CopyFromBooleanField(
        verbose_name='Scrubbers',
    )
    pc_flares = CopyFromBooleanField(
        verbose_name='Flares',
    )
    pc_manual_shutoffs = CopyFromBooleanField(
        verbose_name='Manual Shutoffs',
    )
    pc_automatic_shutoffs = CopyFromBooleanField(
        verbose_name='Automatic Shutoffs',
    )
    pc_interlocks = CopyFromBooleanField(
        verbose_name='Interlocks',
    )
    pc_alarms = CopyFromBooleanField(
        verbose_name='Alarms',
    )
    pc_keyed_bypass = CopyFromBooleanField(
        verbose_name='Keyed Bypass',
    )
    pc_emergency_air_supply = CopyFromBooleanField(
        verbose_name='Emergency Air Supply',
    )
    pc_emergency_power = CopyFromBooleanField(
        verbose_name='Emergency Power',
    )
    pc_backup_pump = CopyFromBooleanField(
        verbose_name='Backup Pump',
    )
    pc_grounding_equipment = CopyFromBooleanField(
        verbose_name='Grounding Equipment',
    )
    pc_inhibitor_addition = CopyFromBooleanField(
        verbose_name='Inhibitor Addition',
    )
    pc_rupture_disks = CopyFromBooleanField(
        verbose_name='Rupture Disks',
    )
    pc_excess_flow_device = CopyFromBooleanField(
        verbose_name='Excess Flow Device',
    )
    pc_quench_system = CopyFromBooleanField(
        verbose_name='Quench System',
    )
    pc_purge_system = CopyFromBooleanField(
        verbose_name='Purge System',
    )
    pc_none = CopyFromBooleanField(
        verbose_name='None',
    )
    pc_other_type = CopyFromCharField(max_length=200, blank=True)
    ms_sprinkler_system = CopyFromBooleanField(
        verbose_name='Sprinkler System',
    )
    ms_dikes = CopyFromBooleanField(
        verbose_name='Dikes',
    )
    ms_fire_walls = CopyFromBooleanField(
        verbose_name='Fire Walls',
    )
    ms_blast_walls = CopyFromBooleanField(
        verbose_name='Blast Walls',
    )
    ms_deluge_system = CopyFromBooleanField(
        verbose_name='Deluge System',
    )
    ms_water_curtain = CopyFromBooleanField(
        verbose_name='Water Curtain',
    )
    ms_enclosure = CopyFromBooleanField(
        verbose_name='Enclosure',
    )
    ms_neutralization = CopyFromBooleanField(
        verbose_name='Neutralization',
    )
    ms_none = CopyFromBooleanField(
        verbose_name='None',
    )
    ms_other_type = CopyFromCharField(max_length=200, blank=True)
    md_process_area_detectors = CopyFromBooleanField(
        verbose_name='Process Area',
    )
    md_perimeter_monitors = CopyFromBooleanField(
        verbose_name='Perimeter Monitors',
    )
    md_none = CopyFromBooleanField(
        verbose_name='None',
    )
    md_other_type = CopyFromCharField(max_length=200, blank=True)
    ch_chemical_reduction = CopyFromBooleanField(
        verbose_name='Reduced Inventory',
    )
    ch_chemical_increase = CopyFromBooleanField(
        verbose_name='Increased Inventory',
    )
    ch_change_process_parameters = CopyFromBooleanField(
        verbose_name='Process Parameters',
    )
    ch_install_process_controls = CopyFromBooleanField(
        verbose_name='Process Controls',
    )
    ch_install_process_detection = CopyFromBooleanField(
        verbose_name='Process Detection',
    )
    ch_install_perimeter_monitoring = CopyFromBooleanField(
        verbose_name='Perimeter Monitoring',
    )
    ch_install_mitigation_systems = CopyFromBooleanField(
        verbose_name='Mitigation Systems',
    )
    ch_none_required = CopyFromBooleanField(
        verbose_name='None Recommended',
    )
    ch_none = CopyFromBooleanField(
        verbose_name='None',
    )
    ch_other_changes = CopyFromCharField(max_length=200, blank=True)
    op_procedures_review_date = CopyFromDateField(null=True)
    training_review_date = CopyFromDateField(null=True)
    tr_classroom = CopyFromBooleanField(
        verbose_name='Classrom',
    )
    tr_on_the_job = CopyFromBooleanField(
        verbose_name='On the Job',
    )
    tr_other_type = CopyFromCharField(max_length=200, blank=True)
    ct_written_test = CopyFromBooleanField(
        verbose_name='Written Test',
    )
    ct_oral_test  = CopyFromBooleanField(
        verbose_name='Oral Test',
    )
    ct_demonstration = CopyFromBooleanField(
        verbose_name='Demonstration',
    )
    ct_observation = CopyFromBooleanField(
        verbose_name='Observation',
    )
    ct_other_type = CopyFromCharField(max_length=200, blank=True)
    maintenance_review_date = CopyFromDateField(null=True)
    equipment_inspection_date = CopyFromDateField(null=True)
    equipment_tested = CopyFromCharField(max_length=200, blank=True)
    change_mgmt_date = CopyFromDateField(null=True)
    change_mgmt_review_date = CopyFromDateField(null=True)
    pre_startup_review_date = CopyFromDateField(null=True)
    compliance_audit_date = CopyFromDateField(null=True)
    audit_completion_date = CopyFromDateField(null=True)
    incident_investigation_date = CopyFromDateField(null=True)
    investigation_change_date = CopyFromDateField(null=True)
    participation_plans_review_date = CopyFromDateField(null=True)
    hot_work_permit_review_date = CopyFromDateField(null=True)
    contractor_safety_review_date = CopyFromDateField(null=True)
    contractor_safety_eval_date = CopyFromDateField(null=True)
    cbi_flag = CopyFromBooleanField()
    description = CopyFromTextField()
    num_prevent_3_chemicals = CopyFromIntegerField()

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tblS7PreventionProgram3

        annotations = m.get_renamed_fields()

        annotations['id'] = F('PreventionProgram3ID')
        annotations['process_naics_3'] = F('Process_NAICS_ID')
        annotations['num_prevent_3_chemicals'] = Count('tbls7_prevention_program_chemicals')

        qs = m.objects.annotate(**annotations)

        return qs

    @classmethod
    def get_prefixed_boolean_fields(cls, prefix):

        fields = [
            f for f in cls._meta.get_fields()
            if f.name[0:len(prefix)] == prefix and
            f.name != prefix + 'other_type' and
            f.name != prefix + 'completion_date' and
            f.name != prefix + 'date'
        ]

        return fields

    @property
    def pha_technique(self):

        self._pha_technique = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pha_')
            if self.__dict__[f.name]
        ]

        if self.pha_other_technique != '':
            self._public_receptors_within_distance.append(
                self.pha_other_technique
            )

        return self._pha_technique

    @property
    def hazard_identified(self):

        self._hazard_identified = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('mh_')
            if self.__dict__[f.name]
        ]

        if self.mh_other_type != '':
            self._public_receptors_within_distance.append(
                self.mh_other_type
            )

        return self._hazard_identified

    @property
    def process_controls(self):

        self._process_controls = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('pc_')
            if self.__dict__[f.name]
        ]

        if self.pc_other_type != '':
            self._public_receptors_within_distance.append(
                self.pc_other_type
            )

        return self._process_controls

    @property
    def mitigation_systems(self):

        self._mitigation_systems = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('ms_')
            if self.__dict__[f.name]
        ]

        if self.ms_other_type != '':
            self._public_receptors_within_distance.append(
                self.ms_other_type
            )

        return self._mitigation_systems

    @property
    def monitoring_systems(self):

        self._monitoring_systems = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('md_')
            if self.__dict__[f.name]
        ]

        if self.md_other_type != '':
            self._public_receptors_within_distance.append(
                self.md_other_type
            )

        return self._monitoring_systems

    @property
    def pha_changes(self):

        self._pha_changes = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('ch_')
            if self.__dict__[f.name]
        ]

        if self.md_other_type != '':
            self._public_receptors_within_distance.append(
                self.md_other_type
            )

        return self._pha_changes

    @property
    def training_type(self):

        self._training_type = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('tr_')
            if self.__dict__[f.name]
        ]

        if self.tr_other_type != '':
            self._public_receptors_within_distance.append(
                self.tr_other_type
            )

        return self._training_type

    @property
    def competency_testing(self):

        self._competency_testing = [
            f.verbose_name for f
            in self._meta.model.get_prefixed_boolean_fields('ct_')
            if self.__dict__[f.name]
        ]

        if self.ct_other_type != '':
            self._public_receptors_within_distance.append(
                self.ct_other_type
            )

        return self._competency_testing


class EmergencyResponse(BaseRMPModel):
    facility = CopyFromOneToOneField(
        'Registration',
        primary_key=True,
        on_delete=models.PROTECT,
    )
    community_erp_yn = CopyFromBooleanField(
        source_column='ER_CommunityPlan',
    )
    facility_erp_yn = CopyFromBooleanField(
        source_column='ER_FacilityPlan',
    )
    erp_specific_yn = CopyFromBooleanField(
        source_column='ER_ResponseActions',
    )
    erp_inform_yn = CopyFromBooleanField(
        source_column='ER_PublicInfoProcedures',
    )
    erp_inform_hth_yn = CopyFromBooleanField(
        source_column='ER_EmergencyHealthCare',
    )
    erp_review_date = CopyFromDateField(
        source_column='ER_ReviewDate',
        blank=True,
        null=True,
    )
    erp_training_date = CopyFromDateField(
        source_column='ERTrainingDate',
        blank=True,
        null=True,
    )
    coord_agency= CopyFromCharField(
        source_column='CoordinatingAgencyName',
        max_length=250,
        blank=True,
    )
    coord_phone = CopyFromCharField(
        source_column='CoordinatingAgencyPhone',
        max_length=10,
        blank=True,
    )
    subto_osha191038 = CopyFromBooleanField(
        source_column='FR_OSHA1910_38',
    )
    subto_osha191020 = CopyFromBooleanField(
        source_column='FR_OSHA1910_120',
    )
    subto_cwa112 = CopyFromBooleanField(
        source_column='FR_SPCC',
    )
    subto_rcra264= CopyFromBooleanField(
        source_column='FR_RCRA',
    )
    subto_opa90 = CopyFromBooleanField(
        source_column='FR_OPA90',
    )
    subto_state_epcra = CopyFromBooleanField(
        source_column='FR_EPCRA',
    )
    subto_other = CopyFromCharField(
        source_column='FR_OtherRegulation',
        max_length=200,
        blank=True,
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tblS9EmergencyResponses

        annotations = m.get_renamed_fields()
        annotations['erp_review_date'] = Cast(
            'ER_ReviewDate', CopyFromDateField()
        )
        annotations['erp_training_date'] = Cast(
            'ERTrainingDate', CopyFromDateField()
        )

        return m.objects.annotate(**annotations)


class ProcNaics(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
    )
    process = CopyFromForeignKey(
        'Process',
        on_delete=models.PROTECT,
    )
    naics_code = CopyFromForeignKey(
        'NAICS',
        db_column='naics_code',
        on_delete=models.PROTECT,
    )
    num_prevent_2 = CopyFromIntegerField()
    num_prevent_3 = CopyFromIntegerField()

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tblS1Process_NAICS

        annotations = m.get_renamed_fields()

        annotations['id'] = F('Process_NAICS_ID')
        annotations['num_prevent_2'] = Count('tbls8preventionprogram2')
        annotations['num_prevent_3'] = Count('tbls7preventionprogram3')

        qs = m.objects.annotate(**annotations)

        return qs


class Prevent2Chem(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='PrimaryKey',
    )
    prevent_2 = CopyFromForeignKey(
        'PreventionProgram2',
        on_delete=models.PROTECT,
        source_column='PreventionProgram2ID',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.PROTECT,
        source_column='ProcessChemicalID',
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tblS8_Prevention_Program_Chemicals

        return m.objects.get_default_transform_queryset()


class Prevent3Chem(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='PrimaryKey',
    )
    prevent_3 = CopyFromForeignKey(
        'PreventionProgram3',
        on_delete=models.PROTECT,
        source_column='PreventionProgram3ID',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.PROTECT,
        source_column='ProcessChemicalID',
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tblS7_Prevention_Program_Chemicals

        return m.objects.get_default_transform_queryset()
