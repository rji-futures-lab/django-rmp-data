"""
Models for processed RMP data.
"""
import os
from django.conf import settings
from django.db import models
from django.db.models import F, Max, OuterRef, Subquery, Sum, Count, Case, When, Value, Q
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
    )
    zip_ext = CopyFromCharField(max_length=4)
    county_fips = CopyFromIntegerField()
    num_registrations = CopyFromIntegerField()
    latitude = CopyFromDecimalField(
        max_digits=6,
        decimal_places=3,
    )
    longitude = CopyFromDecimalField(
        max_digits=6,
        decimal_places=3,
    )
    sub_type = CopyFromCharField(max_length=1, blank=True)
    sub_date = CopyFromDateTimeField()
    # exec_type = CopyFromCharField(max_length=1, blank=True) **** This field is nowhere to be found in codes or in tblS1Facilities
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
    # num_proc_23 = CopyFromBigIntegerField()
    # toxic_tot_23 = CopyFromIntegerField()
    # flam_tot_23 = CopyFromBigIntegerField()
    # quantity_tot_23 = CopyFromBigIntegerField() # toxic_tot + flam_tot
    # all_naics = CopyFromCharField(max_length=20, blank=True)
    # sortid_1 = CopyFromCharField(max_length=5)
    # sortid_2 = CopyFromCharField(max_length=5)
    # sortid_3 = CopyFromCharField(max_length=5)
    registered = CopyFromBooleanField(default=True)
    num_fte = CopyFromIntegerField(null=True)
    num_accident_actual = CopyFromIntegerField(null=True)
    num_accident_records = CopyFromIntegerField(null=True)
    num_accident_divider = CopyFromIntegerField(null=True)
    acc_flam_tot = CopyFromIntegerField(null=True)
    acc_toxic_tot = CopyFromIntegerField(null=True)
    acc_quantity_tot = CopyFromIntegerField(null=True)
    num_deaths = CopyFromIntegerField(null=True)
    num_injuries = CopyFromIntegerField(null=True)
    num_evacuated = CopyFromIntegerField(null=True)
    property_damage = CopyFromIntegerField(null=True)

    @classmethod
    def get_transform_queryset(self):
        qs = raw_models.tblFacility.objects.filter(
            tbls1facilities__ReceiptDate=Subquery(
                raw_models.tblS1Facilities.objects.filter(
                    EPAFacilityID=OuterRef('EPAFacilityID'),
                ).values('ReceiptDate').annotate(
                    max_sub_date=Max('ReceiptDate')
                ).values('max_sub_date').order_by('-max_sub_date')[:1]
            )
        ).values(
            'EPAFacilityID',
            # 'FacilityName',
            'FacilityID',
            # 'FacilityStr1',
            # 'FacilityStr2',
            # 'FacilityCity',
            # 'FacilityState',
            # 'FacilityZipCode',
            # 'Facility4DigitZipExt',
            # 'FacilityCountyFIPS',
            # 'CountOfFacilityID',
        ).distinct().annotate(
            id=F('EPAFacilityID'),
            facility_name=F('FacilityName'),
            rmp_id=F('FacilityID'),
            street_1=F('FacilityStr1'),
            street_2=F('FacilityStr2'),
            city=F('FacilityCity'),
            state=F('FacilityState'),
            zip_code=F('FacilityZipCode'),
            zip_ext=F('Facility4DigitZipExt'),
            county_fips=F('FacilityCountyFIPS'),
            num_registrations=F('CountOfFacilityID'),
            latitude=F('tbls1facilities__FacilityLatDecDegs'),
            longitude=F('tbls1facilities__FacilityLongDecDegs'),
            sub_type=F('tbls1facilities__SubmissionType'),
            sub_date=F('tbls1facilities__ReceiptDate'),
            # exec_type=F('exec_type'),
            execsum_rmp_id=F('FacilityID'),
            exec_sub_type=F('tbls1facilities__SubmissionType'),
            exec_sub_date=F('tbls1facilities__ReceiptDate'),
            deregistration_date=F('tbls1facilities__DeRegistrationDate'),
            dereg_effect_date=F('tbls1facilities__DeRegistrationEffectiveDate'),
            parent=F('tbls1facilities__ParentCompanyName'),
            parent_2=F('tbls1facilities__Company2Name'),
            operator_name=F('tbls1facilities__OperatorName'),
            operator_city=F('tbls1facilities__OperatorCity'),
            operator_state=F('tbls1facilities__OperatorStateFIPS'),
            operator_zip=F('tbls1facilities__OperatorZipCode'),
            province=F('tbls1facilities__ForeignStateProv'),
            county=F('tbls1facilities__FacilityCountyFIPS'),
            country=F('tbls1facilities__ForeignCountry'),
            sub_reason=F('tbls1facilities__RMPSubmissionReasonCode'),
            dereg_reason=F('tbls1facilities__DeregistrationReasonCode'),
            dereg_other=F('tbls1facilities__DeregistrationReasonOtherText'),
            toxic_tot=Sum(Case(When(tbls1facilities__tbls1processes__tbls1processchemicals__ChemicalID__ChemType='T', then=F('tbls1facilities__tbls1processes__tbls1processchemicals__Quantity')), default=Value(0), output_field=CopyFromIntegerField())),
            flam_tot=Sum(Case(When(tbls1facilities__tbls1processes__tbls1processchemicals__ChemicalID__ChemType='F', then=F('tbls1facilities__tbls1processes__tbls1processchemicals__Quantity')), default=Value(0), output_field=CopyFromIntegerField())),
            quantity_tot=F('toxic_tot') + F('flam_tot'),
            registered=Case(When(dereg_reason__gt=0, then=0), default=Value(1), output_field=CopyFromBooleanField()),
            num_fte=F('tbls1facilities__FTE'),
            # num_proc_23=F('num_proc_23'),
            # toxic_tot_23=F('toxic_tot_23'),
            # flam_tot_23=F('flam_tot_23'),
            # quantity_tot_23=F('quantity_tot_23'),
            all_naics=F('tbls1facilities__tbls1processes__tbls1process_naics__NAICSCode'),
            num_accident_records=Count('tbls1facilities__tbls6accidenthistory',),
            num_accident_actual=Count('tbls1facilities__tbls6accidenthistory', distinct=True,),
            num_accident_divider=Case(When(num_accident_actual=0, then=1), default=F('num_accident_records') / F('num_accident_actual')),
            acc_flam_tot=Sum(Case(When(tbls1facilities__tbls6accidenthistory__tbls6accidentchemicals__ChemicalID__ChemType='F', then=('tbls1facilities__tbls6accidenthistory__tbls6accidentchemicals__QuantityReleased')), default=Value(0), output_field=CopyFromIntegerField())) / F('num_accident_divider'),
            acc_toxic_tot=Sum(Case(When(tbls1facilities__tbls6accidenthistory__tbls6accidentchemicals__ChemicalID__ChemType='T', then=('tbls1facilities__tbls6accidenthistory__tbls6accidentchemicals__QuantityReleased')), default=Value(0), output_field=CopyFromIntegerField())) / F('num_accident_divider'),
            acc_quantity_tot=F('acc_flam_tot') + F('acc_toxic_tot'),
            num_deaths=Sum(F('tbls1facilities__tbls6accidenthistory__DeathsWorkers') + F('tbls1facilities__tbls6accidenthistory__DeathsPublicResponders') + F('tbls1facilities__tbls6accidenthistory__DeathsPublic'), default=Value(0), output_field=CopyFromIntegerField()) / F('num_accident_divider'),
            num_injuries=Sum(F('tbls1facilities__tbls6accidenthistory__InjuriesPublic') + F('tbls1facilities__tbls6accidenthistory__InjuriesWorkers') + F('tbls1facilities__tbls6accidenthistory__InjuriesPublicResponders'), default=Value(0), output_field=CopyFromIntegerField()) / F('num_accident_divider'),
            num_evacuated=Sum(F('tbls1facilities__tbls6accidenthistory__Evacuated'), output_field=CopyFromIntegerField()) / F('num_accident_divider'),
            property_damage=Sum(F('tbls1facilities__tbls6accidenthistory__OnsitePropertyDamage') + F('tbls1facilities__tbls6accidenthistory__OffsitePropertyDamage'), output_field=CopyFromIntegerField()) / F('num_accident_divider'),
        )
        print(qs.query)
        return qs

    class Meta:
        indexes = [
            models.Index(fields=['registered', '-num_deaths']),
            models.Index(fields=['registered', '-num_evacuated']),
            models.Index(fields=['registered', '-property_damage']),
        ]


class Registration(BaseRMPModel):
    rmp_id = CopyFromIntegerField(
        primary_key=True,
        db_column='rmp_id',
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
    num_accident_records = CopyFromIntegerField(null=True)
    num_accident_actual = CopyFromIntegerField(null=True)
    num_accident_divider = CopyFromIntegerField(null=True)
    num_facility = CopyFromIntegerField(null=True)
    num_process = CopyFromIntegerField(null=True)
    num_proc_chem = CopyFromIntegerField(null=True)
    num_acc_chem = CopyFromIntegerField(null=True)
    num_proc_chem_tox = CopyFromIntegerField(null=True)
    num_proc_chem_flam = CopyFromIntegerField(null=True)
    num_response = CopyFromIntegerField(null=True)
    num_chem_real = CopyFromIntegerField(null=True)
    num_worst_tox = CopyFromIntegerField(null=True)
    num_alt_tox = CopyFromIntegerField(null=True)
    num_worst_flam = CopyFromIntegerField(null=True)
    num_alt_flam = CopyFromIntegerField(null=True)
    num_prev_2 = CopyFromIntegerField(null=True)
    num_prev_3 = CopyFromIntegerField(null=True)
    toxic_tot = CopyFromBigIntegerField(null=True)
    flam_tot = CopyFromBigIntegerField(null=True)
    quantity_tot=CopyFromBigIntegerField(null=True)
    acc_flam_tot = CopyFromIntegerField(null=True)
    acc_toxic_tot = CopyFromIntegerField(null=True)
    acc_quantity_tot = CopyFromIntegerField(null=True)
    num_deaths = CopyFromIntegerField(null=True)
    num_injuries = CopyFromIntegerField(null=True)
    num_evacuated = CopyFromIntegerField(null=True)
    property_damage = CopyFromIntegerField(null=True)
    county = CopyFromCharField(max_length=60, blank=True, null=True)
    foreign_country_tr = CopyFromCharField(max_length=60, blank=True, null=True)
    # num_proc_23 = CopyFromBigIntegerField(null=True)
    # toxic_tot_23 = CopyFromBigIntegerField(null=True)
    # flam_tot_23 = CopyFromBigIntegerField(null=True)
    # quantity_tot_23 = CopyFromBigIntegerField(null=True)
    num_execsum = CopyFromIntegerField(null=True)

    @classmethod
    def get_transform_queryset(self):
        qs = raw_models.tblS1Facilities.objects.select_related('FacilityCountyFIPS_id').values(
            'FacilityID',
            # 'FacilityName',
            # 'FacilityStr1',
            # 'FacilityStr2',
            # 'FacilityCity',
            # 'FacilityState',
            # 'FacilityZipCode',
            # 'Facility4DigitZipExt',
            # 'FacilityCountyFIPS',
            # 'LEPC',
            # 'FacilityLatDecDegs',
            # 'FacilityLongDecDegs',
            # 'ValidLatLongFlag',
            # 'LatLongMethod',
            # 'LatLongDescription',
            # 'FacilityURL',
            # 'FacilityPhoneNumber',
            # 'FacilityEmailAddress',
            # 'FacilityDUNS',
            # 'ParentCompanyName',
            # 'Company2Name',
            # 'CompanyDUNS',
            # 'Company2DUNS',
            # 'OperatorName',
            # 'OperatorPhone',
            # 'OperatorStr1',
            # 'OperatorStr2',
            # 'OperatorCity',
            # 'OperatorStateFIPS',
            # 'OperatorZipCode',
            # 'OperatorZipCodeExt',
            # 'RMPContact',
            # 'RMPTitle',
            # 'EmergencyContactName',
            # 'EmergencyContactTitle',
            # 'EmergencyContactPhone',
            # 'Phone24',
            # 'EmergencyContactExt_PIN',
            # 'FTE',
            # 'OtherEPAFacilityID',
            # 'EPAFacilityID',
            # 'OSHA_PSM',
            # 'EPCRA_302',
            # 'CAA_TitleV',
            # 'ClearAirOpPermitID',
            # 'SafetyInspectionDate',
            # 'SafetyInspectionBy',
            # 'OSHARanking',
            # 'PredictiveFilingFlag',
            # 'SubmissionType',
            # 'RMPDescription',
            # 'NoAccidents',
            # 'ForeignStateProv',
            # 'ForeignZipCode',
            # 'ForeignCountry',
            # 'CBI_Flag',
            # 'CompletionCheckDate',
            # 'ErrorReportDate',
            # 'ReceiptDate',
            # 'GraphicsIndicator',
            # 'AttachmentsIndicator',
            # 'CertificationReceivedFlag',
            # 'SubmissionMethod',
            # 'CBISubstantiationFlag',
            # 'ElectronicWaiverReceivedFlag',
            # 'PostmarkDate',
            # 'RMPCompleteFlag',
            # 'DeRegistrationDate',
            # 'DeRegistrationEffectiveDate',
            # 'AnniversaryDate',
            # 'CBIFlag',
            # 'CBIUnsanitizedVersionFlag',
            # 'VersionNumber',
            # 'FRS_Lat',
            # 'FRS_Long',
            # 'FRS_Description',
            # 'FRS_Method',
            # 'HorizontalAccMeasure',
            # 'HorizontalRefDatumCode',
            # 'SourceMapScaleNumber',
            # 'EmergencyContactEmail',
            # 'RMPPreparerName',
            # 'RMPPreparerStreet1',
            # 'RMPPreparerStreet2',
            # 'RMPPreparerCity',
            # 'RMPPreparerState',
            # 'RMPPreparerZIP',
            # 'RMPPreparerZIP4Ext',
            # 'RMPPreparerTelephone',
            # 'RMPPreparerForeignStateOrProvince',
            # 'RMPPreparerForeignCountry',
            # 'RMPPreparerForeignPostalCode',
            # 'RMPSubmissionReasonCode',
            # 'RMPEmail',
            # 'DeregistrationReasonCode',
            # 'DeregistrationReasonOtherText',
        ).annotate(
            rmp_id=F('FacilityID'),
            facility_name=F('FacilityName'),
            street_1=F('FacilityStr1'),
            street_2=F('FacilityStr2'),
            city=F('FacilityCity'),
            state=F('FacilityState'),
            zip=F('FacilityZipCode'),
            zip_ext=F('Facility4DigitZipExt'),
            county_fips=F('FacilityCountyFIPS'),
            lepc=F('LEPC'),
            latitude_dec=F('FacilityLatDecDegs'),
            longitude_dec=F('FacilityLongDecDegs'),
            valid_latlong=F('ValidLatLongFlag'),
            latlong_meth=F('LatLongMethod'),
            latlong_desc=F('LatLongDescription'),
            facility_url=F('FacilityURL'),
            facility_phone=F('FacilityPhoneNumber'),
            facility_email=F('FacilityEmailAddress'),
            facility_duns=F('FacilityDUNS'),
            parent=F('ParentCompanyName'),
            parent_2=F('Company2Name'),
            parent_duns=F('CompanyDUNS'),
            parent2_duns=F('Company2DUNS'),
            operator_name=F('OperatorName'),
            operator_phone=F('OperatorPhone'),
            op_street_1=F('OperatorStr1'),
            op_street_2=F('OperatorStr2'),
            operator_city=F('OperatorCity'),
            operator_state=F('OperatorStateFIPS'),
            operator_zip=F('OperatorZipCode'),
            operator_zip_ext=F('OperatorZipCodeExt'),
            rmp_contact=F('RMPContact'),
            rmp_contact_title=F('RMPTitle'),
            em_contact_name=F('EmergencyContactName'),
            em_contact_title=F('EmergencyContactTitle'),
            em_contact_phone=F('EmergencyContactPhone'),
            phone_24hour=F('Phone24'),
            phone_24hour_ext=F('EmergencyContactExt_PIN'),
            num_fte=F('FTE'),
            other_facility_id=F('OtherEPAFacilityID'),
            facility_id=F('EPAFacilityID'),
            osha_psm_yn=F('OSHA_PSM'),
            epcra_302_yn=F('EPCRA_302'),
            caa_title_v_yn=F('CAA_TitleV'),
            caa_permit_id=F('ClearAirOpPermitID'),
            safety_inspect_dt=F('SafetyInspectionDate'),
            safety_inspect_by=F('SafetyInspectionBy'),
            osha_ranking=F('OSHARanking'),
            predictive_file_yn=F('PredictiveFilingFlag'),
            submission_type=F('SubmissionType'),
            rmp_desc=F('RMPDescription'),
            no_accidents_yn=F('NoAccidents'),
            foreign_province=F('ForeignStateProv'),
            foreign_zip=F('ForeignZipCode'),
            foreign_country=F('ForeignCountry'),
            num_fte_cbi_flag=F('CBI_Flag'),
            complete_check_dt=F('CompletionCheckDate'),
            error_report_dt=F('ErrorReportDate'),
            receipt_date=F('ReceiptDate'),
            graphics_ind=F('GraphicsIndicator'),
            attachment_ind=F('AttachmentsIndicator'),
            cert_rec_flag=F('CertificationReceivedFlag'),
            submit_method=F('SubmissionMethod'),
            cbi_substant_flag=F('CBISubstantiationFlag'),
            elect_waiver_flag=F('ElectronicWaiverReceivedFlag'),
            postmark_date=F('PostmarkDate'),
            rmp_complete_flag=F('RMPCompleteFlag'),
            deregistration_dt=F('DeRegistrationDate'),
            dereg_effect_dt=F('DeRegistrationEffectiveDate'),
            anniversary_date=F('AnniversaryDate'),
            cbi_flag=F('CBIFlag'),
            unsanitized_vers=F('CBIUnsanitizedVersionFlag'),
            version_number=F('VersionNumber'),
            frs_lat_dec=F('FRS_Lat'),
            frs_long_dec=F('FRS_Long'),
            frs_ll_desc=F('FRS_Description'),
            frs_ll_method=F('FRS_Method'),
            hor_measure=F('HorizontalAccMeasure'),
            hor_ref=F('HorizontalRefDatumCode'),
            source_scale=F('SourceMapScaleNumber'),
            em_email=F('EmergencyContactEmail'),
            prep_name=F('RMPPreparerName'),
            prep_street_1=F('RMPPreparerStreet1'),
            prep_street_2=F('RMPPreparerStreet2'),
            prep_city=F('RMPPreparerCity'),
            prep_state=F('RMPPreparerState'),
            prep_zip=F('RMPPreparerZIP'),
            prep_zip_ext=F('RMPPreparerZIP4Ext'),
            prep_phone=F('RMPPreparerTelephone'),
            prep_foreign_state=F('RMPPreparerForeignStateOrProvince'),
            prep_country=F('RMPPreparerForeignCountry'),
            prep_foreign_zip=F('RMPPreparerForeignPostalCode'),
            sub_reason=F('RMPSubmissionReasonCode'),
            rmp_email=F('RMPEmail'),
            dereg_reason=F('DeregistrationReasonCode'),
            dereg_other=F('DeregistrationReasonOtherText'),
            num_accident_records=Count('tbls6accidenthistory',),
            num_accident_actual=Count('tbls6accidenthistory', distinct=True,),
            num_accident_divider=Case(When(num_accident_actual=0, then=1), default=F('num_accident_records') / F('num_accident_actual')),
            num_facility=Count('tblfacility', distinct=True,),
            num_process=Count('tbls1processes', distinct=True,),
            num_proc_chem=Count('tbls1processes__tbls1processchemicals'),
            num_acc_chem=Count('tbls6accidenthistory__tbls6accidentchemicals'),
            num_response=Count('tbls9emergencyresponses', distinct=True),
            num_chem_real=Count(Case(When(tbls1processes__tbls1processchemicals__ChemicalID__gt=Value(0), then=('tbls1processes__tbls1processchemicals'))), distinct=True),
            num_proc_chem_tox=(F('num_proc_chem') / F('num_chem_real'))/2,
            num_proc_chem_flam=(F('num_proc_chem') / F('num_chem_real'))/2,
            num_worst_tox=Count('tbls1processes__tbls1processchemicals__tbls2toxicsworstcase__ProcessChemicalID', distinct=True),
            num_alt_tox=Count('tbls1processes__tbls1processchemicals__tbls3toxicsaltreleases__ProcessChemicalID', distinct=True),
            num_worst_flam=Count('tbls1processes__tbls1processchemicals__tbls4flammablesworstcase', distinct=True),
            num_alt_flam=Count('tbls1processes__tbls1processchemicals__tbls5flammablesaltreleases', distinct=True),
            num_prev_2=Count('tbls1processes__tbls1process_naics__tbls8preventionprogram2', distinct=True),
            num_prev_3=Count('tbls1processes__tbls1process_naics__tbls7preventionprogram3', distinct=True),
            toxic_tot=Sum(Case(When(tbls1processes__tbls1processchemicals__ChemicalID__ChemType='T', then=F('tbls1processes__tbls1processchemicals__Quantity')), default=Value(0), output_field=CopyFromIntegerField())) / F('num_proc_chem_tox'),
            flam_tot=Sum(Case(When(tbls1processes__tbls1processchemicals__ChemicalID__ChemType='F', then=F('tbls1processes__tbls1processchemicals__Quantity')), default=Value(0), output_field=CopyFromIntegerField())) / F('num_proc_chem_flam'),
            quantity_tot=F('toxic_tot') + F('flam_tot'),
            acc_flam_tot=Sum(Case(When(tbls6accidenthistory__tbls6accidentchemicals__ChemicalID__ChemType='F', then=('tbls6accidenthistory__tbls6accidentchemicals__QuantityReleased')), default=Value(0), output_field=CopyFromIntegerField())) / F('num_accident_divider'),
            acc_toxic_tot=Sum(Case(When(tbls6accidenthistory__tbls6accidentchemicals__ChemicalID__ChemType='T', then=('tbls6accidenthistory__tbls6accidentchemicals__QuantityReleased')), default=Value(0), output_field=CopyFromIntegerField())) / F('num_accident_divider'),
            acc_quantity_tot=F('acc_flam_tot') + F('acc_toxic_tot'),
            num_deaths=Sum(F('tbls6accidenthistory__DeathsWorkers') + F('tbls6accidenthistory__DeathsPublicResponders') + F('tbls6accidenthistory__DeathsPublic'), default=Value(0), output_field=CopyFromIntegerField()) / F('num_accident_divider'),
            num_injuries=Sum(F('tbls6accidenthistory__InjuriesPublic') + F('tbls6accidenthistory__InjuriesWorkers') + F('tbls6accidenthistory__InjuriesPublicResponders'), default=Value(0), output_field=CopyFromIntegerField()) / F('num_accident_divider'),
            num_evacuated=Sum(F('tbls6accidenthistory__Evacuated'), output_field=CopyFromIntegerField()) / F('num_accident_divider'),
            property_damage=Sum(F('tbls6accidenthistory__OnsitePropertyDamage') + F('tbls6accidenthistory__OffsitePropertyDamage'), output_field=CopyFromIntegerField()) / F('num_accident_divider'),
            county=F('FacilityCountyFIPS'),
            foreign_country_tr=F('ForeignCountry'),
            # num_proc_23=Count(Case(When(Q(tbls1processes__ProgramLevel='2') | Q(tbls1processes__ProgramLevel='3'), then=('tbls1processes__tbls1processchemicals')))),
            # toxic_tot_23=Sum(Case(When((Q(tbls1processes__ProgramLevel='2') | Q(tbls1processes__ProgramLevel='3')) & Q(tbls1processes__tbls1processchemicals__ChemicalID__ChemType='T'), then=('tbls1processes__tbls1processchemicals__Quantity')))),
            # flam_tot_23=Sum(Case(When((Q(tbls1processes__ProgramLevel='2') | Q(tbls1processes__ProgramLevel='3')) & Q(tbls1processes__tbls1processchemicals__ChemicalID__ChemType='F'), then=('tbls1processes__tbls1processchemicals__Quantity')))),
            # quantity_tot_23=F('toxic_tot_23') + F('flam_tot_23'),
            num_execsum=Count('tblexecutivesummaries'),

            # annotate(
            #     county=Subquery(
            #         raw_models.tlkpCountyFIPSCodes.objects.filter(
            #             StateCounty_Code=OuterRef('FacilityCountyFIPS')
            #         ).values('StateCounty_Code').annotate(
            #             county=F('County_Name'),
            #         ).values('county')
            #     )
            # )

        )
        return qs

class State(BaseRMPModel):
    code = CopyFromCharField(
        max_length=2,
        unique=True,
    )
    total_facilities = CopyFromIntegerField()
    total_accidents = CopyFromIntegerField()
    total_deaths = CopyFromIntegerField()
    total_injuries = CopyFromIntegerField()
    total_evacuated = CopyFromIntegerField()
    total_property_damage = CopyFromIntegerField()

    @classmethod
    def get_transform_queryset(self):
        qs = Facility.objects.filter(registered=True).values(
                'state'
            ).annotate(
            code=F('state'),
            total_facilities=Count('id'),
            total_accidents=Sum('num_accident'),
            total_deaths=Sum('num_deaths'),
            total_injuries=Sum('num_injuries'),
            total_evacuated=Sum('num_evacuated'),
            total_property_damage=Sum('property_damage'),
        ).order_by('state')
        return qs
