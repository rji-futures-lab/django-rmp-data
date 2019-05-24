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
    )
    safety_review_date = CopyFromDateField(null=True)
    fr_nfpa58 = CopyFromBooleanField()
    fr_osha = CopyFromBooleanField()
    fr_astm = CopyFromBooleanField()
    fr_ansi = CopyFromBooleanField()
    fr_asme = CopyFromBooleanField()
    fr_none = CopyFromBooleanField()
    fr_other_type = CopyFromCharField(max_length=200, blank=True)
    fr_comments = CopyFromCharField(max_length=200, blank=True)
    hazard_review_date = CopyFromDateField(null=True)
    change_completion_date = CopyFromDateField(null=True)
    mh_toxic_release = CopyFromBooleanField()
    mh_fire = CopyFromBooleanField()
    mh_explosion = CopyFromBooleanField()
    mh_runaway_reaction = CopyFromBooleanField()
    mh_polymerization = CopyFromBooleanField()
    mh_overpressurization = CopyFromBooleanField()
    mh_corrosion = CopyFromBooleanField()
    mh_overfilling = CopyFromBooleanField()
    mh_contamination = CopyFromBooleanField()
    mh_equipment_failure = CopyFromBooleanField()
    mh_cooling_loss = CopyFromBooleanField()
    mh_earthquake = CopyFromBooleanField()
    mh_floods = CopyFromBooleanField()
    mh_tornado = CopyFromBooleanField()
    mh_hurricanes = CopyFromBooleanField()
    mh_other_type = CopyFromCharField(max_length=200, blank=True)
    pc_vents = CopyFromBooleanField()
    pc_relief_valves = CopyFromBooleanField()
    pc_check_valves = CopyFromBooleanField()
    pc_scrubbers = CopyFromBooleanField()
    pc_flares = CopyFromBooleanField()
    pc_manual_shutoffs = CopyFromBooleanField()
    pc_automatic_shutoffs = CopyFromBooleanField()
    pc_interlocks = CopyFromBooleanField()
    pc_alarms = CopyFromBooleanField()
    pc_keyed_bypass = CopyFromBooleanField()
    pc_emergency_air_supply = CopyFromBooleanField()
    pc_emergency_power = CopyFromBooleanField()
    pc_backup_pump = CopyFromBooleanField()
    pc_grounding_equipment = CopyFromBooleanField()
    pc_inhibitor_addition = CopyFromBooleanField()
    pc_rupture_disks = CopyFromBooleanField()
    pc_excess_flow_device = CopyFromBooleanField()
    pc_quench_system = CopyFromBooleanField()
    pc_purge_system = CopyFromBooleanField()
    pc_none = CopyFromBooleanField()
    pc_other_type = CopyFromCharField(max_length=200, blank=True)
    ms_sprinkler_system = CopyFromBooleanField()
    ms_dikes = CopyFromBooleanField()
    ms_fire_walls = CopyFromBooleanField()
    ms_blast_walls = CopyFromBooleanField()
    ms_deluge_system = CopyFromBooleanField()
    ms_water_curtain = CopyFromBooleanField()
    ms_enclosure = CopyFromBooleanField()
    ms_neutralization = CopyFromBooleanField()
    ms_none = CopyFromBooleanField()
    ms_other_type = CopyFromCharField(max_length=200, blank=True)
    md_process_area_detectors = CopyFromBooleanField()
    md_perimeter_monitors = CopyFromBooleanField()
    md_none = CopyFromBooleanField()
    md_other_type = CopyFromCharField(max_length=200, blank=True)
    ch_chemical_reduction = CopyFromBooleanField()
    ch_chemical_increase = CopyFromBooleanField()
    ch_change_process_parameters = CopyFromBooleanField()
    ch_install_process_controls = CopyFromBooleanField()
    ch_install_process_detection = CopyFromBooleanField()
    ch_install_perimeter_monitoring = CopyFromBooleanField()
    ch_install_mitigation_systems = CopyFromBooleanField()
    ch_none_required = CopyFromBooleanField()
    ch_none = CopyFromBooleanField()
    ch_other_changes = CopyFromCharField(max_length=200, blank=True)
    op_procedures_review_date = CopyFromDateField(null=True)
    training_review_date = CopyFromDateField(null=True)
    tr_classroom = CopyFromBooleanField()
    tr_on_the_job = CopyFromBooleanField()
    tr_other_type = CopyFromCharField(max_length=200, blank=True)
    ct_written_test = CopyFromBooleanField()
    ct_oral_test = CopyFromBooleanField()
    ct_demonstration = CopyFromBooleanField()
    ct_observation = CopyFromBooleanField()
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
        annotations['num_prevent_2_chemicals'] = Count('tbls8_prevention_program_chemicals')

        qs = m.objects.annotate(**annotations)

        return qs


class PreventionProgram3(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
    )
    process_naics = CopyFromForeignKey(
        'ProcNaics',
        on_delete=models.PROTECT,
    )
    safety_review_date = CopyFromDateField(null=True)
    pha_date = CopyFromDateField(null=True)
    pha_what_if = CopyFromBooleanField()
    pha_checklist = CopyFromBooleanField()
    pha_what_if_checklist = CopyFromBooleanField()
    pha_hazop = CopyFromBooleanField()
    pha_fmea = CopyFromBooleanField()
    pha_fta = CopyFromBooleanField()
    pha_other_technique = CopyFromCharField(max_length=200, blank=True)
    pha_completion_date = CopyFromDateField(null=True)
    mh_toxic_release = CopyFromBooleanField()
    mh_fire = CopyFromBooleanField()
    mh_explosion = CopyFromBooleanField()
    mh_runaway_reaction = CopyFromBooleanField()
    mh_polymerization = CopyFromBooleanField()
    mh_overpressurization = CopyFromBooleanField()
    mh_corrosion = CopyFromBooleanField()
    mh_overfilling = CopyFromBooleanField()
    mh_contamination = CopyFromBooleanField()
    mh_equipment_failure = CopyFromBooleanField()
    mh_cooling_loss = CopyFromBooleanField()
    mh_earthquake = CopyFromBooleanField()
    mh_floods = CopyFromBooleanField()
    mh_tornado = CopyFromBooleanField()
    mh_hurricanes = CopyFromBooleanField()
    mh_other_type = CopyFromCharField(max_length=200, blank=True)
    pc_vents = CopyFromBooleanField()
    pc_relief_valves = CopyFromBooleanField()
    pc_check_valves = CopyFromBooleanField()
    pc_scrubbers = CopyFromBooleanField()
    pc_flares = CopyFromBooleanField()
    pc_manual_shutoffs = CopyFromBooleanField()
    pc_automatic_shutoffs = CopyFromBooleanField()
    pc_interlocks = CopyFromBooleanField()
    pc_alarms = CopyFromBooleanField()
    pc_keyed_bypass = CopyFromBooleanField()
    pc_emergency_air_supply = CopyFromBooleanField()
    pc_emergency_power = CopyFromBooleanField()
    pc_backup_pump = CopyFromBooleanField()
    pc_grounding_equipment = CopyFromBooleanField()
    pc_inhibitor_addition = CopyFromBooleanField()
    pc_rupture_disks = CopyFromBooleanField()
    pc_excess_flow_device = CopyFromBooleanField()
    pc_quench_system = CopyFromBooleanField()
    pc_purge_system = CopyFromBooleanField()
    pc_none = CopyFromBooleanField()
    pc_other_type = CopyFromCharField(max_length=200, blank=True)
    ms_sprinkler_system = CopyFromBooleanField()
    ms_dikes = CopyFromBooleanField()
    ms_fire_walls = CopyFromBooleanField()
    ms_blast_walls = CopyFromBooleanField()
    ms_deluge_system = CopyFromBooleanField()
    ms_water_curtain = CopyFromBooleanField()
    ms_enclosure = CopyFromBooleanField()
    ms_neutralization = CopyFromBooleanField()
    ms_none = CopyFromBooleanField()
    ms_other_type = CopyFromCharField(max_length=200, blank=True)
    md_process_area_detectors = CopyFromBooleanField()
    md_perimeter_monitors = CopyFromBooleanField()
    md_none = CopyFromBooleanField()
    md_other_type = CopyFromCharField(max_length=200, blank=True)
    ch_chemical_reduction = CopyFromBooleanField()
    ch_chemical_increase = CopyFromBooleanField()
    ch_change_process_parameters = CopyFromBooleanField()
    ch_install_process_controls = CopyFromBooleanField()
    ch_install_process_detection = CopyFromBooleanField()
    ch_install_perimeter_monitoring = CopyFromBooleanField()
    ch_install_mitigation_systems = CopyFromBooleanField()
    ch_none_required = CopyFromBooleanField()
    ch_none = CopyFromBooleanField()
    ch_other_changes = CopyFromCharField(max_length=200, blank=True)
    op_procedures_review_date = CopyFromDateField(null=True)
    training_review_date = CopyFromDateField(null=True)
    tr_classroom = CopyFromBooleanField()
    tr_on_the_job = CopyFromBooleanField()
    tr_other_type = CopyFromCharField(max_length=200, blank=True)
    ct_written_test = CopyFromBooleanField()
    ct_oral_test  = CopyFromBooleanField()
    ct_demonstration = CopyFromBooleanField()
    ct_observation = CopyFromBooleanField()
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
        annotations['num_prevent_3_chemicals'] = Count('tbls7_prevention_program_chemicals')

        qs = m.objects.annotate(**annotations)

        return qs


class EmergencyResponse(BaseRMPModel):
    facility = CopyFromOneToOneField(
        'Facility',
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
