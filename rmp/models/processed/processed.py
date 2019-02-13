"""
Models for processed RMP data.
"""
import os
from django.conf import settings
from django.db import models
from django.db.models import F, Max, OuterRef, Subquery
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
)
from rmp.models import raw as raw_models
from rmp.models.base import BaseRMPModel


class AccChem(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='accchem_id',
        verbose_name='Accident Chemical Record ID',
        help_text='A unique ID for each accident chemical record.',
    )
    accident = CopyFromForeignKey(
        'Accident',
        on_delete=models.PROTECT,
        help_text='The unique ID for each accident record',
    )
    chemical = CopyFromForeignKey(
        'ChemCd',
        on_delete=models.PROTECT,
        help_text='The identifying ID for a particular chemical released in an '
                  'accident.',
    )
    quantity_lbs = CopyFromIntegerField(
        null=True,
        verbose_name='Amount Released (lbs)',
        help_text='The amount of the substance released in the accident, in '
                  'pounds, to two significant digits.',
    )
    percent_weight = CopyFromDecimalField(
        decimal_places=2,
        null=True,
        max_digits=5,
        verbose_name='Percent Weight (Within Mixture)',
        help_text='The percent weight of a chemical within a mixture released '
                  'in an accident.',
    )
    num_acc_flam = CopyFromIntegerField(
        null=True,
        verbose_name='Number of Flammable Components',
        help_text='The number of listed flammable component chemicals for this'
                  ' chemical record.',
    )
    cas = CopyFromCharField(
        max_length=9,
        verbose_name='CAS number',
        help_text='The identifying CAS number for a chemical.',
    )
    CHEMICAL_TYPE_CHOICES = (
        ('T', 'toxic'),
        ('F', 'flammable'),
    )
    chemical_type = CopyFromCharField(
        max_length=1,
        choices=CHEMICAL_TYPE_CHOICES,
        help_text='"The type of chemical.',
    )

    source_file = 'rmp_acc_chem'


class AccFlam(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        # source_column='FlamMixChemID',
        source_column='flammixchem_id',
        verbose_name='Flammable Chemical ID',
        help_text='A unique ID for each flammable chemical record.',
    )
    accchem = CopyFromForeignKey(
        'AccChem',
        on_delete=models.PROTECT,
        # source_column='AccidentChemicalID',
        verbose_name='Accident Chemical Record ID',
        help_text='A unique ID for each accident chemical record.'
    )
    chemical = CopyFromForeignKey(
        'ChemCd',
        on_delete=models.PROTECT,
        # source_column='ChemicalID',
        verbose_name='Chemical ID',
        help_text='The identifying ID for a particular flammable chemical released in an accident.',
    )

    source_file = 'rmp_acc_flam'


class Accident(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='accident_id',
    )
    rmp = CopyFromForeignKey(
        'Registration',
        on_delete=models.PROTECT,
    )
    # accident_date = CopyFromDateField(
    #     max_length=19,
    #     null=True,
    #     blank=True,
    # )
    # ^^^^^^^ This is the proper config for this field, once we
    # clean up "null" vs "NULL" values
    accident_date = CopyFromCharField(blank=True, max_length=10)
    # can we combine these two? do we know the time zone?
    # accident_date = CopyFromDateTimeField(blank=True, null=True)
    accident_time = CopyFromCharField(max_length=4)
    naics_code = CopyFromCharField(
        source_column='naics',
        max_length=6,
    )
    release_duration = CopyFromCharField(max_length=5)
    re_gas = CopyFromBooleanField()
    re_spill = CopyFromBooleanField()
    re_fire = CopyFromBooleanField()
    re_explosion = CopyFromBooleanField()
    re_reactive_incident = CopyFromBooleanField(
        source_column='re_reactiveincid',
    )
    rs_storage_vessel = CopyFromBooleanField(
        source_column='rs_storagevessel',
    )
    rs_piping = CopyFromBooleanField()
    rs_process_vessel = CopyFromBooleanField(
        source_column='rs_processvessel',
    )
    rs_transfer_hose = CopyFromBooleanField(
        source_column='rs_transferhose',
    )
    rs_valve = CopyFromBooleanField()
    rs_pump = CopyFromBooleanField()
    rs_joint = CopyFromBooleanField()
    other_release_source = CopyFromCharField(
        source_column='rs_other',
        max_length=200,
        blank=True
    )
    wind_speed = CopyFromDecimalField(
        null=True,
        max_digits=6,
        decimal_places=2,
    )
    wind_speed_unit = CopyFromCharField(max_length=1, blank=True)
    wind_direction = CopyFromCharField(max_length=3, blank=True)
    temperature = CopyFromIntegerField(
        # Data type of source column is decimal, but all distinct values
        # are whole numbers NONETHELESS, should prob convert to decimal field
        # in case the source data includes decimal values
        # means outputtin as such in processed file
        null=True,
    )
    stability_class = CopyFromCharField(max_length=1, blank=True)
    precipitation = CopyFromBooleanField(
        source_column='precipitation_yn',
    )
    unknown_weather = CopyFromBooleanField()
    deaths_workers = CopyFromIntegerField()
    deaths_responders = CopyFromIntegerField()
    deaths_public = CopyFromIntegerField()
    injuries_workers = CopyFromIntegerField()
    injuries_responders = CopyFromIntegerField(
        source_column='injuries_respond',
    )
    injuries_public = CopyFromIntegerField()
    onsite_damage = CopyFromIntegerField()
    offsite_deaths = CopyFromBooleanField()
    hospitalization = CopyFromIntegerField(
        source_column='offsite_hosp',
    )
    offsite_medical = CopyFromIntegerField()
    offsite_evacuated = CopyFromIntegerField()
    offsite_shelter = CopyFromIntegerField()
    offsite_damage = CopyFromIntegerField()
    ed_kills = CopyFromBooleanField()
    ed_defoliation = CopyFromBooleanField()
    ed_water_contamination = CopyFromBooleanField(
        source_column='ed_watercontam',
    )
    ed_soil_contamination = CopyFromBooleanField(
        source_column='ed_soilcontam',
    )
    ed_other = CopyFromCharField(
        max_length=200,
        blank=True
    )
    initiating_event = CopyFromCharField(
        max_length=1,
        blank=True
    )
    cf_equipment_failure = CopyFromBooleanField(
        source_column='cf_equipmentfail',
    )
    cf_human_error = CopyFromBooleanField(
        source_column='cf_humanerror',
    )
    cf_improper_procedure = CopyFromBooleanField(
        source_column='cf_impprocedure',
    )
    cf_overpressure = CopyFromBooleanField()
    cf_upset_condition = CopyFromBooleanField(
        source_column='cf_upsetcondition'
    )
    cf_bypass_condition = CopyFromBooleanField(
        source_column='cf_bypasscond',
    )
    cf_maintenance = CopyFromBooleanField()
    cf_process_design_failure = CopyFromBooleanField(
        source_column='cf_processdesign',
    )
    cf_unsuitable_equipment = CopyFromBooleanField(
        source_column='cf_unsuitequip',
    )
    cf_unusual_weather = CopyFromBooleanField(
        source_column='cf_unusualweather',
    )
    cf_management_error = CopyFromBooleanField(
        source_column='cf_management',
    )
    cf_other = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    offsite_responders_notify = CopyFromCharField(
        max_length=25,
        blank=True,
        source_column='offsite_notify',
    )
    ci_improved_equipment = CopyFromBooleanField(
        source_column='ci_improveequip',
    )
    ci_revised_maintenance = CopyFromBooleanField(
        source_column='ci_revisedmaint',
    )
    ci_revised_training = CopyFromBooleanField(
        source_column='ci_revisedtrain',
    )
    ci_revised_op_procedures = CopyFromBooleanField(
        source_column='ci_opprocedures',
    )
    ci_new_process_controls = CopyFromBooleanField(
        source_column='ci_processcontrol',
    )
    ci_new_mitigation_systems = CopyFromBooleanField(
        source_column='ci_mitigationsys',
    )
    ci_response_plan = CopyFromBooleanField(
        source_column='ci_responseplan',
    )
    ci_changed_process = CopyFromBooleanField(
        source_column='ci_changedprocess',
    )
    ci_reduced_inventory = CopyFromBooleanField(
        source_column='ci_reducedinv',
    )
    ci_none = CopyFromBooleanField()
    ci_other = CopyFromCharField(max_length=200, blank=True)
    cbi_flag = CopyFromBooleanField()

    #TODO TURN BELOW INTO AGGREGATE

    num_acc_chem = CopyFromIntegerField()
    flam_total = CopyFromIntegerField(
        source_column='flam_tot'
    )
    toxic_total = CopyFromIntegerField(
        source_column='toxic_tot'
    )
    quantity_total = CopyFromIntegerField(
        source_column='quantity_tot'
    )
    num_deaths = CopyFromIntegerField()
    num_injuries = CopyFromIntegerField()
    num_evacuated = CopyFromIntegerField()
    property_damage = CopyFromIntegerField()
    env_damage = CopyFromIntegerField()

    # TODO SEE IF THIS WORKS

    def save(self, *args, **kwargs):
        self.quantity_tot = self.flam_tot + self.toxic_tot
        super(Accident, self).save(*args, **kwargs)


class ExecutiveSummary(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='rmp_id',
    )
    summary_text = CopyFromTextField(
        source_column='execsum',
        blank=True,
    )

    @classmethod
    def get_transform_queryset(self):
        qs = raw_models.tblExecutiveSummaries.objects.filter(
            ESSeqNum=Subquery(
                raw_models.tblExecutiveSummaries.objects.filter(
                    FacilityID=OuterRef('FacilityID'),
                ).values('FacilityID_id').annotate(
                    max_seqnum=Max('ESSeqNum')
                ).values('max_seqnum')[:1]
            )
        ).annotate(
            rmp_id=F('FacilityID'),
            execsum=F('SummaryText')
        )
        
        return qs


class ExecutiveSummaryLength(BaseRMPModel):
    rmp_id = CopyFromIntegerField(
        primary_key=True,
    )
    byte_count = CopyFromIntegerField()
    suspect_count = CopyFromIntegerField()
    line_count = CopyFromIntegerField()
    edited_yn = CopyFromCharField(max_length=1)

    source_file = 'rmp_exec_sum_len'


class Process(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='process_id',
    )
    process_desc = CopyFromCharField(max_length=25, blank=True)
    rmp_id = CopyFromIntegerField()
    program_level = CopyFromIntegerField()
    cbi_flag = CopyFromBooleanField()

    # TODO AGGREGATE
    num_proc_chem = CopyFromIntegerField()
    num_proc_naics = CopyFromIntegerField()
    num_chem_real = CopyFromIntegerField()
    num_chem_fake = CopyFromIntegerField()
    num_worst_tox = CopyFromIntegerField()
    num_worst_flam = CopyFromIntegerField()
    num_alt_tox = CopyFromIntegerField()
    num_alt_flam = CopyFromIntegerField()
    num_prev_2 = CopyFromIntegerField()
    num_prev_3 = CopyFromIntegerField()
    toxic_tot = CopyFromBigIntegerField()
    flam_tot = CopyFromBigIntegerField()
    quantity_tot = CopyFromBigIntegerField()
    # while these fields are listed in rmp_fields.csv, they do not appear in
    # rmp_process.tsv ¯\_(ツ)_/¯
    # chem_tox_yn = CopyFromBooleanField()
    # chem_flam_yn = CopyFromBooleanField()

    source_file = 'rmp_process'


class Facility(BaseRMPModel):
    id = CopyFromBigIntegerField(
        primary_key=True,
        source_column='facility_id',
    )
    facility_name = CopyFromCharField(
        max_length=50,
    )
    # ForeignKey Candidate?
    rmp = CopyFromForeignKey(
        'Registration',
        on_delete=models.PROTECT,
    )
    street_1 = CopyFromCharField(
        # check that values going into this field match facility_str_1
        max_length=35,
    )
    street_2 = CopyFromCharField(
        # check that values going into this field match facility_str_2
        max_length=35,
    )
    city = CopyFromCharField(
        max_length=19,
    )
    state = CopyFromCharField(max_length=2)
    zip_code = CopyFromCharField(
        max_length=5,
        source_column='zip',
    )
    zip_ext = CopyFromCharField(max_length=4)
    county_fips = CopyFromIntegerField()
    num_registrations = CopyFromIntegerField()
    latitude = CopyFromDecimalField(
        source_column='latitude_dec',
        max_digits=6,
        decimal_places=3,
    )
    longitude = CopyFromDecimalField(
        source_column='longitude_dec',
        max_digits=6,
        decimal_places=3,
    )
    num_registration = CopyFromIntegerField()
    sub_type = CopyFromCharField(max_length=1, blank=True)
    sub_date = CopyFromDateTimeField()
    exec_type = CopyFromCharField(max_length=1, blank=True)
    execsum_rmp = CopyFromForeignKey(
        'ExecutiveSummary',
        on_delete=models.PROTECT,
    )
    exec_sub_type = CopyFromCharField(max_length=1, blank=True)
    exec_sub_date = CopyFromDateTimeField()
    # these fields could be converted to DateTime once we replace "0000-00-00" with NULL
    deregistration_date = CopyFromCharField(max_length=10)
    dereg_effect_date = CopyFromCharField(max_length=10)
    parent = CopyFromCharField(max_length=200, blank=True)
    parent_2 = CopyFromCharField(max_length=200, blank=True)
    operator_name = CopyFromCharField(max_length=200, blank=True)
    operator_city = CopyFromCharField(max_length=20, blank=True)
    operator_state = CopyFromCharField(max_length=2, blank=True)
    operator_zip = CopyFromCharField(max_length=5, blank=True)
    province = CopyFromCharField(max_length=20, blank=True)
    county = CopyFromCharField(max_length=200, blank=True)
    country = CopyFromCharField(max_length=25, blank=True)
    sub_reason = CopyFromCharField(max_length=3, blank=True)
    dereg_reason = CopyFromCharField(max_length=1, blank=True)
    dereg_other = CopyFromCharField(max_length=255, blank=True)
    # TODO AGGREGATE
    toxic_tot = CopyFromIntegerField()
    flam_tot = CopyFromBigIntegerField()
    quantity_tot = CopyFromBigIntegerField() # toxic_tot + flam_tot
    num_proc_23 = CopyFromBigIntegerField()
    toxic_tot_23 = CopyFromIntegerField()
    flam_tot_23 = CopyFromBigIntegerField()
    quantity_tot_23 = CopyFromBigIntegerField() # toxic_tot + flam_tot
    all_naics = CopyFromCharField(max_length=20, blank=True)
    sortid_1 = CopyFromCharField(max_length=5)
    sortid_2 = CopyFromCharField(max_length=5)
    sortid_3 = CopyFromCharField(max_length=5)
    deregistration_yn = CopyFromCharField(max_length=1, blank=True)
    num_fte = CopyFromIntegerField(null=True)
    # TODO AGGREGATE
    num_accident = CopyFromIntegerField()
    acc_flam_tot = CopyFromIntegerField()
    acc_toxic_tot = CopyFromIntegerField()
    acc_quantity_tot = CopyFromIntegerField()
    num_deaths = CopyFromIntegerField()
    num_injuries = CopyFromIntegerField()
    num_evacuated = CopyFromIntegerField()
    property_damage = CopyFromIntegerField()


class Registration(BaseRMPModel):
    rmp_id = CopyFromIntegerField(
        primary_key=True
    )
    facility_name = CopyFromCharField(max_length=255, blank=True)
    street_1 = CopyFromCharField(max_length=35, blank=True)
    street_2 = CopyFromCharField(max_length=35, blank=True)
    city = CopyFromCharField(max_length=19, blank=True)
    state = CopyFromCharField(max_length=2, blank=True)
    zip = CopyFromCharField(max_length=5, blank=True)
    zip_ext = CopyFromCharField(max_length=4, blank=True)
    county_fips = CopyFromCharField(max_length=5, blank=True)
    lepc = CopyFromCharField(max_length=30, blank=True)
    latitude_dec = CopyFromCharField(max_length=10, blank=True)
    longitude_dec = CopyFromCharField(max_length=11, blank=True)
    valid_latlong = CopyFromCharField(max_length=1, blank=True)
    latlong_meth = CopyFromCharField(max_length=2, blank=True)
    latlong_desc = CopyFromCharField(max_length=2, blank=True)
    facility_url = CopyFromCharField(max_length=100, blank=True)
    facility_phone = CopyFromCharField(max_length=10, blank=True)
    facility_email = CopyFromCharField(max_length=100, blank=True)
    facility_duns = CopyFromCharField(max_length=9, blank=True)
    facility_email = CopyFromCharField(max_length=100, blank=True)
    parent = CopyFromCharField(max_length=250, blank=True)
    parent_2 = CopyFromCharField(max_length=50, blank=True)
    parent_duns = CopyFromCharField(max_length=9, blank=True)
    parent2_duns = CopyFromCharField(max_length=9, blank=True)
    operator_name = CopyFromCharField(max_length=250, blank=True)
    operator_phone = CopyFromCharField(max_length=10, blank=True)
    op_street_1 = CopyFromCharField(max_length=35, blank=True)
    op_street_2 = CopyFromCharField(max_length=35, blank=True)
    operator_city = CopyFromCharField(max_length=19, blank=True)
    operator_state = CopyFromCharField(max_length=2, blank=True)
    operator_zip = CopyFromCharField(max_length=5, blank=True)
    operator_zip_ext = CopyFromCharField(max_length=4, blank=True)
    rmp_contact = CopyFromCharField(max_length=35, blank=True)
    rmp_contact_title = CopyFromCharField(max_length=250, blank=True)
    em_contact_name = CopyFromCharField(max_length=250, blank=True)
    em_contact_title = CopyFromCharField(max_length=35, blank=True)
    em_contact_phone = CopyFromCharField(max_length=10, blank=True)
    phone_24hour = CopyFromCharField(max_length=10, blank=True)
    phone_24hour_ext = CopyFromCharField(max_length=10, blank=True)
    num_fte = CopyFromIntegerField(null=True)
    other_facility_id = CopyFromCharField(blank=True, max_length=15)
    facility_id = CopyFromBigIntegerField(
        # 'Facility',
        # on_delete=models.CASCADE,
    )
    osha_psm_yn = CopyFromBooleanField()
    epcra_302_yn = CopyFromBooleanField()
    caa_title_v_yn = CopyFromBooleanField()
    caa_permit_id = CopyFromCharField(blank=True, max_length=15)
    # safety_inspect_dt = CopyFromDateTimeField(
    #     blank=True,
    #     null=True
    # )
    safety_inspect_dt = CopyFromCharField(blank=True, max_length=10)
    safety_inspect_by = CopyFromCharField(max_length=50, blank=True)
    osha_ranking = CopyFromBooleanField()
    predictive_file_yn = CopyFromBooleanField()
    submission_type = CopyFromCharField(max_length=1, blank=True)
    rmp_desc = CopyFromCharField(max_length=50, blank=True)
    no_accidents_yn = CopyFromBooleanField()
    foreign_province = CopyFromCharField(max_length=35, blank=True)
    foreign_zip = CopyFromCharField(max_length=14, blank=True)
    foreign_country = CopyFromCharField(max_length=2, blank=True)
    num_fte_cbi_flag = CopyFromBooleanField()
    # complete_check_dt = CopyFromDateTimeField(blank=True, null=True)
    complete_check_dt = CopyFromCharField(blank=True, max_length=10)
    # error_report_dt = CopyFromDateTimeField(blank=True, null=True)
    error_report_dt = CopyFromCharField(blank=True, max_length=10)
    receipt_date = CopyFromCharField(max_length=25, blank=True)
    graphics_ind = CopyFromBooleanField()
    attachment_ind = CopyFromBooleanField()
    cert_rec_flag = CopyFromBooleanField()
    submit_method = CopyFromCharField(max_length=50, blank=True)
    cbi_substant_flag = CopyFromBooleanField()
    elect_waiver_flag = CopyFromBooleanField()
    postmark_date = CopyFromCharField(max_length=25, blank=True)
    rmp_complete_flag = CopyFromCharField(max_length=1, blank=True)
    # deregistration_dt = CopyFromDateTimeField(blank=True, null=True)
    deregistration_dt = CopyFromCharField(blank=True, max_length=10)
    # dereg_effect_dt = CopyFromDateTimeField(blank=True, null=True)
    dereg_effect_dt = CopyFromCharField(blank=True, max_length=10)
    # anniversary_date = CopyFromDateTimeField(blank=True, null=True)
    anniversary_date = CopyFromCharField(blank=True, max_length=10)
    cbi_flag = CopyFromBooleanField()
    unsanitized_vers = CopyFromBooleanField()
    version_number = CopyFromCharField(max_length=15, blank=True)
    frs_lat_dec = CopyFromDecimalField(
        max_digits=5, decimal_places=2, null=True
    )
    frs_long_dec = CopyFromDecimalField(
        max_digits=5, decimal_places=2, null=True
    )
    frs_ll_desc = CopyFromCharField(max_length=40, blank=True)
    frs_ll_method = CopyFromCharField(max_length=60, blank=True)
    hor_measure = CopyFromCharField(max_length=6, blank=True)
    hor_ref = CopyFromCharField(max_length=3, blank=True)
    source_scale = CopyFromCharField(max_length=10, blank=True)
    em_email = CopyFromCharField(max_length=100, blank=True)
    prep_name = CopyFromCharField(max_length=70, blank=True)
    prep_street_1 = CopyFromCharField(max_length=35, blank=True)
    prep_street_2 = CopyFromCharField(max_length=35, blank=True)
    prep_city = CopyFromCharField(max_length=19, blank=True)
    prep_state = CopyFromCharField(max_length=2, blank=True)
    prep_zip = CopyFromCharField(max_length=5, blank=True)
    prep_zip_ext = CopyFromCharField(max_length=4, blank=True)
    prep_phone = CopyFromCharField(max_length=10, blank=True)
    prep_foreign_state = CopyFromCharField(max_length=35, blank=True)
    prep_country = CopyFromCharField(max_length=2, blank=True)
    prep_foreign_zip = CopyFromCharField(max_length=14, blank=True)
    sub_reason = CopyFromCharField(max_length=3, blank=True)
    rmp_email = CopyFromCharField(max_length=100, blank=True)
    dereg_reason = CopyFromCharField(max_length=2, blank=True)
    dereg_other = CopyFromCharField(max_length=80, blank=True)

    # TODO AGGREGATE
    num_accident = CopyFromIntegerField()
    num_facility = CopyFromIntegerField()
    num_process = CopyFromIntegerField()
    num_response = CopyFromIntegerField()
    num_chem_real = CopyFromIntegerField()
    num_worst_tox = CopyFromIntegerField()
    num_alt_tox = CopyFromIntegerField()
    num_worst_flam = CopyFromIntegerField()
    num_alt_flam = CopyFromIntegerField()
    num_prev_2 = CopyFromIntegerField()
    num_prev_3 = CopyFromIntegerField()
    toxic_tot = CopyFromBigIntegerField()
    flam_tot = CopyFromBigIntegerField()
    acc_flam_tot = CopyFromIntegerField()
    acc_toxic_tot = CopyFromIntegerField()
    acc_quantity_tot = CopyFromIntegerField()
    num_deaths = CopyFromIntegerField()
    num_injuries = CopyFromIntegerField()
    num_evacuated = CopyFromIntegerField()
    property_damage = CopyFromIntegerField()
    county = CopyFromCharField(max_length=60, blank=True)
    foreign_country_tr = CopyFromCharField(max_length=60, blank=True)
    num_proc_23 = CopyFromBigIntegerField()
    toxic_tot_23 = CopyFromBigIntegerField()
    flam_tot_23 = CopyFromBigIntegerField()
    quantity_tot_23 = CopyFromBigIntegerField()
    num_execsum_mod = CopyFromIntegerField()
    execsum_type = CopyFromCharField(max_length=1, blank=True)
    num_execsum = CopyFromIntegerField()
    num_exec_sum = CopyFromIntegerField()


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


class PreventionProgram2(BaseRMPModel): #rmp_prevent_2
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='prevent_2_id',
    )
    procnaics = CopyFromForeignKey(
        'ProcNaics',
        on_delete=models.CASCADE
    )
    safety_info_date = CopyFromCharField(blank=True, max_length=8)
    # safety_info_date = CopyFromDateField(blank=True)
    fr_nfpa58 = CopyFromBooleanField()
    fr_osha = CopyFromBooleanField()
    fr_astm = CopyFromBooleanField()
    fr_ansi = CopyFromBooleanField()
    fr_asme = CopyFromBooleanField()
    fr_none = CopyFromBooleanField()
    fr_other = CopyFromCharField(max_length=200, blank=True)
    fr_comments = CopyFromCharField(max_length=200, blank=True)
    haz_review_date = CopyFromCharField(blank=True, max_length=8)
    # haz_review_date = CopyFromDateField(blank=True)
    change_comp_date = CopyFromCharField(blank=True, max_length=8)
    # change_comp_date = CopyFromDateField(blank=True)
    mh_toxicrelease = CopyFromBooleanField()
    mh_fire = CopyFromBooleanField()
    mh_explosion = CopyFromBooleanField()
    mh_runawayreact = CopyFromBooleanField()
    mh_polymerization = CopyFromBooleanField()
    mh_overpressure = CopyFromBooleanField()
    mh_corrosion = CopyFromBooleanField()
    mh_overfilling = CopyFromBooleanField()
    mh_contamination = CopyFromBooleanField()
    mh_equipfailure = CopyFromBooleanField()
    mh_cooling_loss = CopyFromBooleanField()
    mh_earthquake = CopyFromBooleanField()
    mh_floods = CopyFromBooleanField()
    mh_tornado = CopyFromBooleanField()
    mh_hurricanes = CopyFromBooleanField()
    mh_othertype = CopyFromCharField(max_length=200, blank=True)
    pc_vents = CopyFromBooleanField()
    pc_reliefvalves = CopyFromBooleanField()
    pc_checkvalves = CopyFromBooleanField()
    pc_scrubbers = CopyFromBooleanField()
    pc_flares = CopyFromBooleanField()
    pc_manualshutoffs = CopyFromBooleanField()
    pc_autoshutoffs = CopyFromBooleanField()
    pc_interlocks = CopyFromBooleanField()
    pc_alarms = CopyFromBooleanField()
    pc_keyedbypass = CopyFromBooleanField()
    pc_emergencyair = CopyFromBooleanField()
    pc_emergencypower = CopyFromBooleanField()
    pc_backuppump = CopyFromBooleanField()
    pc_groundingequip = CopyFromBooleanField()
    pc_inhibitoradd = CopyFromBooleanField()
    pc_rupturedisks = CopyFromBooleanField()
    pc_excessflowdev = CopyFromBooleanField()
    pc_quenchsystem = CopyFromBooleanField()
    pc_purgesystem = CopyFromBooleanField()
    pc_none = CopyFromBooleanField()
    pc_other = CopyFromCharField(max_length=200, blank=True)
    ms_sprinklersys = CopyFromBooleanField()
    ms_dikes = CopyFromBooleanField()
    ms_firewalls = CopyFromBooleanField()
    ms_blastwalls = CopyFromBooleanField()
    ms_delugesystem = CopyFromBooleanField()
    ms_watercurtain = CopyFromBooleanField()
    ms_enclosure = CopyFromBooleanField()
    ms_neutralization = CopyFromBooleanField()
    ms_none = CopyFromBooleanField()
    ms_other = CopyFromCharField(max_length=200, blank=True)
    md_processarea = CopyFromBooleanField()
    md_perimetermon = CopyFromBooleanField()
    md_none = CopyFromBooleanField()
    md_other = CopyFromCharField(max_length=200, blank=True)
    ch_reduceinv = CopyFromBooleanField()
    ch_increaseinv = CopyFromBooleanField()
    ch_changeparam = CopyFromBooleanField()
    ch_proccontrol = CopyFromBooleanField()
    ch_procdetect= CopyFromBooleanField()
    ch_perimetermon = CopyFromBooleanField()
    ch_mitigationsys = CopyFromBooleanField()
    ch_nonerequired = CopyFromBooleanField()
    ch_none = CopyFromBooleanField()
    ch_other = CopyFromCharField(max_length=200, blank=True)
    proc_review_date = CopyFromCharField(blank=True, max_length=8)
    # proc_review_date = CopyFromDateField(blank=True)
    train_review_date = CopyFromCharField(blank=True, max_length=8)
    # train_review_date = CopyFromDateField(blank=True)
    tr_classroom = CopyFromBooleanField()
    tr_onthejob = CopyFromBooleanField()
    tr_other = CopyFromCharField(max_length=200, blank=True)
    ct_writtentest = CopyFromBooleanField()
    ct_oraltest = CopyFromBooleanField()
    ct_demonstration = CopyFromBooleanField()
    ct_observation = CopyFromBooleanField()
    ct_other = CopyFromCharField(max_length=200, blank=True)
    maint_review_date = CopyFromCharField(blank=True, max_length=8)
    # maint_review_date = CopyFromDateField(blank=True)
    maint_inspect_date = CopyFromCharField(blank=True, max_length=8)
    # maint_inspect_date = CopyFromDateField(blank=True)
    equip_tested = CopyFromCharField(max_length=200, blank=True)
    comp_audit_date = CopyFromCharField(blank=True, max_length=8)
    # comp_audit_date = CopyFromDateField(blank=True)
    audit_comp_date = CopyFromCharField(blank=True, max_length=8)
    # audit_comp_date = CopyFromDateField(blank=True)
    inc_invest_date = CopyFromCharField(blank=True, max_length=8)
    # inc_invest_date = CopyFromDateField(blank=True)
    inc_change_date = CopyFromCharField(blank=True, max_length=8)
    # inc_change_date = CopyFromDateField(blank=True)
    most_recent_date = CopyFromCharField(blank=True, max_length=8)
    # most_recent_date = CopyFromDateField(blank=True)
    cbi_flag = CopyFromBooleanField()
    num_prevent_2_chem = CopyFromIntegerField()
    num_prev2text = CopyFromIntegerField()
    num_prev2_text = CopyFromIntegerField()

    source_file = 'rmp_prevent_2'


class PreventionProgram3(BaseRMPModel):
    prevent_id = CopyFromIntegerField(
        primary_key=True,
        source_column='prevent_3_id',
    )
    procnaics = CopyFromForeignKey(
        'ProcNaics',
        on_delete=models.CASCADE
    )
    safety_info_date = CopyFromCharField(blank=True, max_length=8)
    # safety_info_date = CopyFromDateField(null=True)
    last_pha_date = CopyFromCharField(blank=True, max_length=8)
    # last_pha_date = CopyFromDateField(null=True)
    pha_whatif = CopyFromBooleanField()
    pha_checklist = CopyFromBooleanField()
    pha_whatifcheck = CopyFromBooleanField()
    pha_hazop = CopyFromBooleanField()
    pha_fmea = CopyFromBooleanField()
    pha_fta = CopyFromBooleanField()
    pha_other = CopyFromCharField(max_length=200, blank=True)
    change_comp_date = CopyFromCharField(blank=True, max_length=8)
    # change_comp_date = CopyFromDateField(null=True)
    mh_toxicrelease = CopyFromBooleanField()
    mh_fire = CopyFromBooleanField()
    mh_explosion = CopyFromBooleanField()
    mh_runawayreact = CopyFromBooleanField()
    mh_polymerization = CopyFromBooleanField()
    mh_overpressure = CopyFromBooleanField()
    mh_corrosion = CopyFromBooleanField()
    mh_overfilling = CopyFromBooleanField()
    mh_contamination = CopyFromBooleanField()
    mh_equipfailure = CopyFromBooleanField()
    mh_cooling_loss = CopyFromBooleanField()
    mh_earthquake = CopyFromBooleanField()
    mh_floods = CopyFromBooleanField()
    mh_tornado = CopyFromBooleanField()
    mh_hurricanes = CopyFromBooleanField()
    mh_othertype = CopyFromCharField(max_length=200, blank=True)
    pc_vents = CopyFromBooleanField()
    pc_reliefvalves = CopyFromBooleanField()
    pc_checkvalves = CopyFromBooleanField()
    pc_scrubbers = CopyFromBooleanField()
    pc_flares = CopyFromBooleanField()
    pc_manualshutoffs = CopyFromBooleanField()
    pc_autoshutoffs = CopyFromBooleanField()
    pc_interlocks = CopyFromBooleanField()
    pc_alarms = CopyFromBooleanField()
    pc_keyedbypass = CopyFromBooleanField()
    pc_emergencyair = CopyFromBooleanField()
    pc_emergencypower = CopyFromBooleanField()
    pc_backuppump = CopyFromBooleanField()
    pc_groundingequip = CopyFromBooleanField()
    pc_inhibitoradd = CopyFromBooleanField()
    pc_rupturedisks = CopyFromBooleanField()
    pc_excessflowdev = CopyFromBooleanField()
    pc_quenchsystem = CopyFromBooleanField()
    pc_purgesystem = CopyFromBooleanField()
    pc_none = CopyFromBooleanField()
    pc_other = CopyFromCharField(max_length=200, blank=True)
    ms_sprinklersys = CopyFromBooleanField()
    ms_dikes = CopyFromBooleanField()
    ms_firewalls = CopyFromBooleanField()
    ms_blastwalls = CopyFromBooleanField()
    ms_delugesystem = CopyFromBooleanField()
    ms_watercurtain = CopyFromBooleanField()
    ms_enclosure = CopyFromBooleanField()
    ms_neutralization = CopyFromBooleanField()
    ms_none = CopyFromBooleanField()
    ms_other = CopyFromCharField(max_length=200, blank=True)
    md_processarea = CopyFromBooleanField()
    md_perimetermon = CopyFromBooleanField()
    md_none = CopyFromBooleanField()
    md_other = CopyFromCharField(max_length=200, blank=True)
    ch_reduceinv = CopyFromBooleanField()
    ch_increaseinv = CopyFromBooleanField()
    ch_changeparam = CopyFromBooleanField()
    ch_proccontrol = CopyFromBooleanField()
    ch_procdetect = CopyFromBooleanField()
    ch_perimetermon = CopyFromBooleanField()
    ch_mitigationsys = CopyFromBooleanField()
    ch_nonerequired = CopyFromBooleanField()
    ch_none = CopyFromBooleanField()
    ch_other = CopyFromCharField(max_length=200, blank=True)
    proc_review_date = CopyFromCharField(blank=True, max_length=8)
    # proc_review_date = CopyFromDateField(null=True)
    train_review_date = CopyFromCharField(blank=True, max_length=8)
    # train_review_date = CopyFromDateField(null=True)
    tr_classroom = CopyFromBooleanField()
    tr_onthejob = CopyFromBooleanField()
    tr_other = CopyFromCharField(max_length=200, blank=True)
    ct_writtentest = CopyFromBooleanField()
    ct_oraltest  = CopyFromBooleanField()
    ct_demonstration = CopyFromBooleanField()
    ct_observation = CopyFromBooleanField()
    ct_other = CopyFromCharField(max_length=200, blank=True)
    maint_review_date = CopyFromCharField(blank=True, max_length=8)
    # maint_review_date = CopyFromDateField(null=True)
    maint_inspect_date = CopyFromCharField(blank=True, max_length=8)
    # maint_inspect_date = CopyFromDateField(null=True)
    equip_tested = CopyFromCharField(max_length=200, blank=True)
    change_manage_date = CopyFromCharField(blank=True, max_length=8)
    # change_manage_date = CopyFromDateField(null=True)
    change_review_date = CopyFromCharField(blank=True, max_length=8)
    # change_review_date = CopyFromDateField(null=True)
    prestart_rev_date = CopyFromCharField(blank=True, max_length=8)
    # prestart_rev_date = CopyFromDateField(null=True)
    comp_audit_date = CopyFromCharField(blank=True, max_length=8)
    # comp_audit_date = CopyFromDateField(null=True)
    audit_comp_date = CopyFromCharField(blank=True, max_length=8)
    # audit_comp_date = CopyFromDateField(null=True)
    inc_invest_date = CopyFromCharField(blank=True, max_length=8)
    # inc_invest_date = CopyFromDateField(null=True)
    inc_change_date = CopyFromCharField(blank=True, max_length=8)
    # inc_change_date = CopyFromDateField(null=True)
    part_review_date = CopyFromCharField(blank=True, max_length=8)
    # part_review_date = CopyFromDateField(null=True)
    hotwork_rev_date = CopyFromCharField(blank=True, max_length=8)
    # hotwork_rev_date = CopyFromDateField(null=True)
    con_safety_date = CopyFromCharField(blank=True, max_length=8)
    # con_safety_date = CopyFromDateField(null=True)
    con_eval_date = CopyFromCharField(blank=True, max_length=8)
    # con_eval_date = CopyFromDateField(null=True)
    cbi_flag = CopyFromBooleanField()

    # TODO AGGREGATE

    num_prevent_3_chem = CopyFromIntegerField()
    num_prev3text = CopyFromIntegerField()
    num_prev3_text = CopyFromIntegerField()

    source_file = 'rmp_prevent_3'


class EmergencyResponse(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='rmp_id',
    )
    community_erp_yn = CopyFromBooleanField()
    facility_erp_yn = CopyFromBooleanField()
    erp_specific_yn = CopyFromBooleanField()
    erp_inform_yn = CopyFromBooleanField()
    erp_inform_hth_yn = CopyFromBooleanField()
    # erp_review_date = CopyFromDateTimeField(blank=True)
    # erp_training_date = CopyFromDateTimeField(blank=True)
    erp_review_date = CopyFromCharField(max_length=10, blank=True)
    erp_training_date = CopyFromCharField(max_length=10, blank=True)
    coord_agency= CopyFromCharField(max_length=250, blank=True)
    coord_phone = CopyFromCharField(max_length=10, blank=True)
    subto_osha191038 = CopyFromBooleanField()
    subto_osha191020 = CopyFromBooleanField()
    subto_cwa112 = CopyFromBooleanField()
    subto_rcra264= CopyFromBooleanField()
    subto_opa90 = CopyFromBooleanField()
    subto_state_epcra = CopyFromBooleanField()
    subto_other = CopyFromCharField(max_length=200, blank=True)

    source_file = 'rmp_response'

#problems with big integer field
class ProcChem(BaseRMPModel):
    procchem_id = CopyFromBigIntegerField(
        primary_key=True,
        source_column='procchem_id',
    )
    process = CopyFromForeignKey(
        'Process',
        on_delete=models.CASCADE
    )
    chemical = CopyFromForeignKey(
        'ChemCd',
        on_delete=models.CASCADE
    )
    quantity_lbs = CopyFromBigIntegerField()
    cbi_flag = CopyFromBooleanField()
    num_alt_flam = CopyFromBigIntegerField()
    num_alt_tox = CopyFromBigIntegerField()
    num_prevent_2_chem = CopyFromBigIntegerField()
    num_prevent_3_chem = CopyFromBigIntegerField()
    num_proc_flam = CopyFromBigIntegerField()
    num_worst_flam = CopyFromBigIntegerField()
    num_worst_tox = CopyFromBigIntegerField()
    cas = CopyFromBigIntegerField()
    chemical_type = CopyFromCharField(max_length=1)

    source_file = 'rmp_proc_chem'


class ProcFlam(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='flammixchem_id',
    )
    procchem = CopyFromForeignKey(
        ProcChem,
        on_delete=models.CASCADE
    )
    chemical = CopyFromForeignKey(
        'ChemCd',
        on_delete=models.CASCADE
    )

    source_file = 'rmp_proc_flam'


class ProcNaics(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='procnaics_id',
    )
    process = CopyFromForeignKey(
        'Process',
        on_delete=models.CASCADE
    )
    naics = CopyFromIntegerField()
    num_prevent_2 = CopyFromIntegerField()
    num_prevent_3 = CopyFromIntegerField()

    source_file = 'rmp_proc_naics'


class Prev2Text(BaseRMPModel):
    prevent_2 = CopyFromOneToOneField(
        'PreventionProgram2',
        primary_key=True,
        on_delete=models.CASCADE,
        source_column='prevent_2_id',
    )
    desctext = CopyFromTextField()

    source_file = 'rmp_prev2text'


class Prev3Text(BaseRMPModel):
    prevent_3 = CopyFromOneToOneField(
        'PreventionProgram3',
        primary_key=True,
        on_delete=models.CASCADE,
        source_column='prevent_3_id',
    )
    desctext = CopyFromTextField()

    source_file = 'rmp_prev3text'


class Prevent2Chem(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='primary_key',
    )
    prevent_2 = CopyFromForeignKey(
        'PreventionProgram2',
        on_delete=models.CASCADE,
        source_column='prevent_2_id',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.CASCADE
    )

    source_file = 'rmp_prevent_2_chem'


class Prevent3Chem(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='primary_key',
    )
    prevent_3 = CopyFromForeignKey(
        'PreventionProgram3',
        on_delete=models.CASCADE,
        source_column='prevent_3_id',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.CASCADE
    )

    source_file = 'rmp_prevent_3_chem'


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
