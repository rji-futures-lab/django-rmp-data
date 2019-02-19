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
from rmp.models.base import BaseRMPModel

class Facility(BaseRMPModel):
    id = CopyFromBigIntegerField(
        primary_key=True,
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


class Registration(BaseRMPModel):
    rmp = CopyFromIntegerField(
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
    facility_id = CopyFromForeignKey(
        'Facility',
        db_column='facility_id',
        on_delete=models.PROTECT,
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
