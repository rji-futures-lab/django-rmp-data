"""
Models for processed RMP data.
"""
from django.db import models
from postgres_copy import CopyManager
from django.db.models import Count, Sum


class AccChem(models.Model):
    accchem_id = models.IntegerField(
        primary_key=True,
        verbose_name='Accident Chemical Record ID',
        help_text='A unique ID for each accident chemical record.',
    )
    accident_id = models.ForeignKey(
        tbls6Accidenthistory,
        on_delete=models.CASCADE,
        help_text='The unique ID for each accident record',
    )
    chemical_id = models.ForeignKey(
        ChemCd,
        on_delete=models.CASCADE,
        help_text='The identifying ID for a particular chemical released in an '
                  'accident.',
    )
    quantity_lbs = models.IntegerField(
        null=True,
        verbose_name='Amount Released (lbs)',
        help_text='The amount of the substance released in the accident, in '
                  'pounds, to two significant digits.',
    )
    percent_weight = models.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=5,
        verbose_name='Percent Weight (Within Mixture)',
        help_text='The percent weight of a chemical within a mixture released '
                  'in an accident.',
    )
    num_acc_flam = models.IntegerField(
        null=True,
        verbose_name='Number of Flammable Components',
        help_text='The number of listed flammable component chemicals for this'
                  ' chemical record.',
    )
    cas = models.CharField(
        max_length=9,
        verbose_name='CAS number',
        help_text='The identifying CAS number for a chemical.',
    )
    CHEMICAL_TYPE_CHOICES = (
        ('T', 'toxic'),
        ('F', 'flammable'),
    )
    chemical_type = models.CharField(
        max_length=1,
        choices=CHEMICAL_TYPE_CHOICES,
        help_text='"The type of chemical.',
    )

    objects = CopyManager()

    class Meta:
        db_table = 'rmp_acc_chem'

# TODO: does this table have a primary key, or is it a linking table?
# if the latter, how might we make the model more in line with Django's
# conventions?
class AccFlam(models.Model):
    # TODO: ForeignKeyField candidate
    flammixchem_id = models.IntegerField(
        primary_key=True,
        verbose_name='Flammable Chemical ID',
        help_text='A unique ID for each flammable chemical record.',
        primary_key=True,
    )
    # TODO: ForeignKeyField candidate
    accchem_id = models.ForeignKey(
        AccChem,
        on_delete=models.CASCADE,
        verbose_name='Accident Chemical Record ID',
        help_text='A unique ID for each accident chemical record.'
    )
    # TODO: ForeignKeyField candidate
    chemical_id = models.ForeignKey(
        ChemCd,
        on_delete=models.CASCADE,
        verbose_name='Chemical ID',
        help_text='The identifying ID for a particular flammable chemical released in an accident.',
    )

    objects = CopyManager()

    class Meta:
        db_table = 'rmp_acc_flam'

class Tbls6Accidenthistory(models.Model): #rmp_accident
    accident_id = models.IntegerField(primary_key=True)
    rmp_id = models.ForeignKey(
        rmp_registration,
        on_delete=models.CASCADE,
    )
    accidentdate = models.DateTimeField(blank=True, null=True)
    accidenttime = models.CharField(max_length=4)
    naicscode = models.CharField(max_length=6)
    accidentreleaseduration = models.CharField(max_length=5)
    re_gas = models.BooleanField()
    re_spill = models.BooleanField()
    re_fire = models.BooleanField()
    re_explosion = models.BooleanField()
    re_reactiveincident = models.BooleanField()
    rs_storagevessel = models.BooleanField()
    rs_piping = models.BooleanField()
    rs_processvessel = models.BooleanField()
    rs_transferhose = models.BooleanField()
    rs_valve = models.BooleanField()
    rs_pump = models.BooleanField()
    rs_joint = models.BooleanField()
    otherreleasesource = models.CharField(max_length=200, blank=True, null=True)
    windspeed = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    windspeedunitcode = models.CharField(max_length=1, blank=True, null=True)
    winddirection = models.CharField(max_length=3, blank=True, null=True)
    temperature = models.DecimalField(max_digits=6, decimal_places=2)
    stabilityclass = models.CharField(max_length=1, blank=True, null=True)
    precipitation = models.BooleanField()
    weatherunknown = models.BooleanField()
    deathsworkers = models.IntegerField()
    deathspublicresponders = models.IntegerField()
    deathspublic = models.IntegerField()
    injuriesworkers = models.IntegerField()
    injuriespublicresponders = models.IntegerField()
    injuriespublic = models.IntegerField()
    onsitepropertydamage = models.IntegerField()
    offsitedeaths = models.BooleanField(blank=True, null=True)
    hospitalization = models.IntegerField()
    medicaltreatment = models.IntegerField()
    evacuated = models.IntegerField()
    shelteredinplace = models.IntegerField()
    offsitepropertydamage = models.IntegerField()
    ed_kills = models.BooleanField()
    ed_minordefoliation = models.BooleanField()
    ed_watercontamination = models.BooleanField()
    ed_soilcontamination = models.BooleanField()
    ed_other = models.CharField(max_length=200, blank=True, null=True)
    initiatingevent = models.CharField(max_length=1, blank=True, null=True)
    cf_equipmentfailure = models.BooleanField()
    cf_humanerror = models.BooleanField()
    cf_improperprocedure = models.BooleanField()
    cf_overpressurization = models.BooleanField()
    cf_upsetcondition = models.BooleanField()
    cf_bypasscondition = models.BooleanField()
    cf_maintenance = models.BooleanField()
    cf_processdesignfailure = models.BooleanField()
    cf_unsuitableequipment = models.BooleanField()
    cf_unusualweather = models.BooleanField()
    cf_managementerror = models.BooleanField()
    cf_other = models.CharField(max_length=200, blank=True, null=True)
    offsiterespondersnotify = models.CharField(max_length=25, blank=True, null=True)
    ci_improvedequipment = models.BooleanField()
    ci_revisedmaintenance = models.BooleanField()
    ci_revisedtraining = models.BooleanField()
    ci_revisedopprocedures = models.BooleanField()
    ci_newprocesscontrols = models.BooleanField()
    ci_newmitigationsystems = models.BooleanField()
    ci_revisederplan = models.BooleanField()
    ci_changedprocess = models.BooleanField()
    ci_reducedinventory = models.BooleanField()
    ci_none = models.BooleanField()
    ci_othertype = models.CharField(max_length=200, blank=True, null=True)
    cbi_flag = models.BooleanField()

    #TODO TURN BELOW INTO AGGREGATE

    num_acc_chem = models.IntegerField()
    flam_tot = models.DecimalField(max_digits=6, decimal_places=2)
    toxic_tot = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_tot = models.DecimalField(max_digits=6, decimal_places=2)
    num_deaths = models.IntegerField()
    num_injuries = models.IntegerField()
    num_evacuated = models.IntegerField()
    property_damage = models.IntegerField()
    env_damage = models.IntegerField()

    # TODO SEE IF THIS WORKS

    def save(self, *args, **kwargs):
        self.quantity_tot = self.flam_tot + self.toxic_tot
        super(Tbls6Accidenthistory, self).save(*args, **kwargs)

    class Meta:
        db_table = 'tblS6AccidentHistory'

class Tblexecutivesummaries(models.Model): #rmp_execsum
    rmp_id = models.ForeignKey(
        rmp_registration,
        on_delete=models.CASCADE,
    )
    summarytext = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tblExecutiveSummaries'

class ExecSumLen(models.Model):
    rmp_id = models.ForeignKey(
        rmp_registration,
        on_delete=models.CASCADE,
    )
    byte_count = models.IntegerField()
    suspect_count = models.IntegerField()
    line_count = models.IntegerField()
    edited_yn = models.CharField(max_length=1)

    class Meta:
        db_table = 'rmp_exec_sum_len'

class Rmp_process(models.Model):
    process_id = models.IntegerField(primary_key=True)
    process_desc = models.CharField(max_length=25, blank=True, null=True)
    rmp_id = models.ForeignKey(
        rmp_registration,
        on_delete=models.CASCADE,
    )
    program_level = models.IntegerField()
    cbi_flag = models.BooleanField()

    # TODO AGGREGATE
    num_proc_chem =
    num_proc_naics =
    num_chem_real =
    num_chem_fake =
    num_worst_tox =
    num_worst_flam =
    num_alt_tox =
    num_alt_flam =
    num_prev_2 =
    num_prev_3 =
    toxic_tot =
    flam_tot =
    quantity_tot =
    chem_tox_yn = models.BooleanField()
    chem_flam_yn = models.BooleanField()

    class Meta:
        db_table = 'rmp_process'

class rmp_facility(models.Model):
    epa_facility_id = models.IntegerField(primary_key=True)
    facility_name = models.CharField()
    rmp_id = models.ForeignKey(
        rmp_registration,
        on_delete=models.CASCADE,
    )
    facility_str_1 = models.CharField()
    facility_str_2 = models.CharField()
    facility_city = models.CharField()
    facility_state = models.CharField(max_length=2)
    facility_zip_code = models.CharField(max_length=5)
    facility_exten = models.CharField(max_length=4)
    facility_fips = models.IntegerField()
    # TODO AGGREGATE
    num_registrations =
    count_id = models.IntegerField()
    facility_latitude = models.IntegerField()
    facility_longitude = models.IntegerField()
    sub_type = models.CharField(max_length=1, blank=True, null=True)
    sub_date = models.DateTimeField()
    exec_type = models.CharField(max_length=1, blank=True, null=True)
    execsum_rmp_id = models.ForeignKey()
    exec_sub_type = models.CharField(max_length=1, blank=True, null=True)
    exec_sub_date = models.DateTimeField()
    deregistration_date = models.DateTimeField()
    dereg_effect_date = models.DateTimeField()
    parent = models.CharField(max_length=200, blank=True, null=True)
    parent_2 = models.CharField(max_length=200, blank=True, null=True)
    operator_name = models.CharField(max_length=200, blank=True, null=True)
    operator_state = models.CharField(max_length=2)
    operator_zip = models.CharField(max_length=5)
    province = models.CharField(max_length=20, blank=True, null=True)
    county = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    sub_reason = models.CharField(max_length=3, blank=True, null=True)
    dereg_reason = models.CharField(max_length=1, blank=True, null=True)
    dereg_other = models.CharField(max_length=255, blank=True, null=True)
    # TODO AGGREGATE
    toxic_tot = models.IntegerField()
    flam_tot = models.IntegerField()
    quantity_tot = # toxic_tot + flam_tot
    toxic_tot_23 = models.IntegerField()
    flam_tot_23 = models.IntegerField()
    quantity_tot_23 = # toxic_tot + flam_tot
    all_naics = models.CharField(max_length=20)
    sortid_1 = models.CharField(max_length=5)
    sortid_2 = models.CharField(max_length=5)
    sortid_3 = models.CharField(max_length=5)
    dereg_yn = models.CharField(max_length=1, blank=True, null=True)
    num_fte = models.IntegerField()
    # TODO AGGREGATE
    num_accident =
    acc_flam_tot =
    acc_toxic_tot =
    acc_quantity_tot =
    num_deaths =
    num_injuries =
    num_evacuated =
    property_damage = models.IntegerField()

    class Meta:
        db_table = 'rmp_facility'

class rmp_registration(models.Model):
    rmp_id = models.IntegerField(
        primary_key=True
    )
    facility_name = models.CharField(max_length=255, blank=True, null=True)
    street_1 = models.CharField(max_length=35, blank=True, null=True)
    street_2 = models.CharField(max_length=35, blank=True, null=True)
    city = models.CharField(max_length=19, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    zip_ext = models.CharField(max_length=4, blank=True, null=True)
    county_fips = models.CharField(max_length=5, blank=True, null=True)
    lepc = models.CharField(max_length=30, blank=True, null=True)
    latitude_dec = models.CharField(max_length=10, blank=True, null=True)
    longitude_dec = models.CharField(max_length=11, blank=True, null=True)
    valid_latlong = models.CharField(max_length=1, blank=True, null=True)
    latlong_meth = models.CharField(max_length=2, blank=True, null=True)
    latlong_desc = models.CharField(max_length=2, blank=True, null=True)
    facility_url = models.CharField(max_length=100, blank=True, null=True)
    facility_phone = models.CharField(max_length=10, blank=True, null=True)
    facility_email = models.CharField(max_length=100, blank=True, null=True)
    facility_duns = models.CharField(max_length=9, blank=True, null=True)
    facility_email = models.CharField(max_length=100, blank=True, null=True)
    parent = models.CharField(max_length=250, blank=True, null=True)
    parent_2 = models.CharField(max_length=50, blank=True, null=True)
    parent_duns = models.CharField(max_length=9, blank=True, null=True)
    parent2_duns = models.CharField(max_length=9, blank=True, null=True)
    operator_name = models.CharField(max_length=250, blank=True, null=True)
    operator_phone = models.CharField(max_length=10, blank=True, null=True)
    op_street_1 = models.CharField(max_length=35, blank=True, null=True)
    op_street_2 = models.CharField(max_length=35, blank=True, null=True)
    operator_city = models.CharField(max_length=19, blank=True, null=True)
    operator_state = models.CharField(max_length=2, blank=True, null=True)
    operator_zip = models.CharField(max_length=5, blank=True, null=True)
    operator_zip_ext = models.CharField(max_length=4, blank=True, null=True)
    rmp_contact = models.CharField(max_length=35, blank=True, null=True)
    rmp_contact_title = models.CharField(max_length=250, blank=True, null=True)
    em_contact_name = models.CharField(max_length=250, blank=True, null=True)
    em_contact_title = models.CharField(max_length=35, blank=True, null=True)
    em_contact_phone = models.CharField(max_length=10, blank=True, null=True)
    phone_24hour = models.CharField(max_length=10, blank=True, null=True)
    phone_24hour_ext = models.CharField(max_length=10, blank=True, null=True)
    num_fte = models.IntegerField()
    other_facility_id = models.IntegerField()
    facility_id = models.ForeignKey(
        rmp_facility,
        on_delete=models.CASCADE,
    )
    osha_psm_yn = models.BooleanField()
    epcra_302_yn = models.BooleanField()
    caa_title_v_yn = models.BooleanField()
    caa_permit_id = models.IntegerField()
    safety_inspect_dt = models.DateTimeField(blank=True, null=True)
    safety_inspect_by = models.CharField(max_length=50, blank=True, null=True)
    osha_ranking = models.BooleanField()
    predictive_file_yn = models.BooleanField()
    submission_type = models.CharField(max_length=1, blank=True, null=True)
    rmp_desc = models.CharField(max_length=50, blank=True, null=True)
    no_accidents_yn = models.BooleanField()
    foreign_province = models.CharField(max_length=35, blank=True, null=True)
    foreign_zip = models.CharField(max_length=14, blank=True, null=True)
    foreign_country = models.CharField(max_length=2, blank=True, null=True)
    num_fte_cbi_flag = models.BooleanField()
    complete_check_dt = models.DateTimeField(blank=True, null=True)
    error_report_dt = models.DateTimeField(blank=True, null=True)
    receipt_date = models.CharField(max_length=25, blank=True, null=True)
    graphics_ind = models.BooleanField()
    attachment_ind = models.BooleanField()
    cert_rec_flag = models.BooleanField()
    submit_method = models.CharField(max_length=50, blank=True, null=True)
    cbi_substant_flag = models.BooleanField()
    elect_waiver_flag = models.BooleanField()
    postmark_date = models.CharField(max_length=25, blank=True, null=True)
    rmp_complete_flag = models.CharField(max_length=1, blank=True, null=True)
    deregistration_dt = models.DateTimeField(blank=True, null=True)
    dereg_effect_dt = models.DateTimeField(blank=True, null=True)
    anniversary_date = models.DateTimeField(blank=True, null=True)
    cbi_flag = models.BooleanField()
    unsanitized_vers = models.BooleanField()
    version_number = models.CharField(max_length=15, blank=True, null=True)
    frs_lat_dec = models.DecimalField(max_digits=5, decimal_places=2)
    frs_long_dec = models.DecimalField(max_digits=5, decimal_places=2)
    frs_ll_desc = models.CharField(max_length=40, blank=True, null=True)
    frs_ll_method = models.CharField(max_length=60, blank=True, null=True)
    hor_measure = models.CharField(max_length=6, blank=True, null=True)
    hor_ref = models.CharField(max_length=3, blank=True, null=True)
    source_scale = models.CharField(max_length=10, blank=True, null=True)
    em_email = models.CharField(max_length=100, blank=True, null=True)
    prep_name = models.CharField(max_length=70, blank=True, null=True)
    prep_street_1 = models.CharField(max_length=35, blank=True, null=True)
    prep_street_2 = models.CharField(max_length=35, blank=True, null=True)
    prep_city = models.CharField(max_length=19, blank=True, null=True)
    prep_state = models.CharField(max_length=2, blank=True, null=True)
    prep_zip = models.CharField(max_length=5, blank=True, null=True)
    prep_zip_ext = models.CharField(max_length=4, blank=True, null=True)
    prep_phone = models.CharField(max_length=10, blank=True, null=True)
    prep_foreign_state = models.CharField(max_length=35, blank=True, null=True)
    prep_country = models.CharField(max_length=2, blank=True, null=True)
    prep_foreign_zip = models.CharField(max_length=14, blank=True, null=True)
    sub_reason = models.CharField(max_length=3, blank=True, null=True)
    rmp_email = models.CharField(max_length=100, blank=True, null=True)
    dereg_reason = models.CharField(max_length=2, blank=True, null=True)
    dereg_other = models.CharField(max_length=80, blank=True, null=True)

    # TODO AGGREGATE
    num_accident =
    num_facility =
    num_process =
    num_response =
    num_chem_real =
    num_worst_tox =
    num_alt_tox =
    num_worst_flam =
    num_alt_flam =
    num_prev_2 =
    num_prev_3 =
    toxic_tot =
    flam_tot =
    acc_flam_tot =
    acc_toxic_tot =
    acc_quantity_tot =
    num_deaths =
    num_injuries =
    num_evacuated =
    property_damage =
    county = models.CharField(max_length=60, blank=True, null=True)
    foreign_country_tr = models.CharField(max_length=60, blank=True, null=True)
    num_proc_23 =
    toxic_tot_23 =
    flam_tot_23 =
    quantity_tot_23 =
    num_execsum_mod =
    execsum_type = models.CharField(max_length=1, blank=True, null=True)
    num_execsum =
    num_exec_sum =

    class Meta:
        db_table = 'rmp_registration'



class Tbls5Flammablesaltreleases(models.Model): #rmp_alt_flam
    flammableid = models.IntegerField(primary_key=True)
    processchemicalid = models.ForeignKey(
        ProcChem,
        on_delete=models.CASCADE,
    )
    analyticalbasis = models.CharField(max_length=255, blank=True, null=True)
    scenario = models.CharField(max_length=200)
    quantityreleased = models.DecimalField(max_digits=5, decimal_places=2)
    endpointused = models.CharField(max_length=30, blank=True, null=True)
    lfl_value = models.DecimalField(max_digits=5, decimal_places=1)
    endpoint_distance = models.DecimalField(max_digits=5, decimal_places=1)
    residentialpopulation = models.CharField(max_length=9, blank=True, null=True)
    pr_schools = models.BooleanField()
    pr_residences = models.BooleanField()
    pr_hospitals = models.BooleanField()
    pr_prisons = models.BooleanField()
    pr_publicrecreation = models.BooleanField()
    pr_comm_ind = models.BooleanField()
    pr_othertype = models.CharField(max_digits=200, blank=True, null=True)
    er_natlstateparks = models.BooleanField()
    er_wildlifesactuary = models.BooleanField()
    er_fedwilderness = models.BooleanField()
    er_othertype = models.CharField(max_digits=200, blank=True, null=True)
    pm_dikes = models.BooleanField()
    pm_firewalls = models.BooleanField()
    pm_blastwalls = models.BooleanField()
    pm_enclosures = models.BooleanField()
    pm_othertype = models.CharField(max_length=200, blank=True, null=True)
    am_sprinklersystems = models.BooleanField()
    am_delugesystems = models.BooleanField()
    am_watercurtain = models.BooleanField()
    am_excessflowvalve = models.BooleanField()
    am_othertype = models.CharField(max_length=200, blank=True, null=True)
    ptrgraphic = models.CharField(max_length=12, blank=True, null=True)
    cbi_flag = models.BooleanField()

    class Meta:
        db_table = 'tblS5FlammablesAltReleases'

class Tbls3Toxicsaltreleases(models.Model): #rmp_alt_tox
    toxicid = models.IntegerField(primary_key=True)
    processchemicalid = models.ForeignKey(
        ProcChem,
        on_delete=models.CASCADE,
    )
    percentweight = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    physicalstate = models.CharField(max_length=1, blank=True, null=True)
    analyticalbasis = models.CharField(max_length=255, blank=True, null=True)
    scenario = models.CharField(max_length=200)
    quantityreleased = models.DecimalField(max_digits=5, decimal_places=2)
    releaseduration = models.BDecimalField(max_digits=5, decimal_places=2)
    releaserate = models.BooleanField(blank=True, null=True)
    windspeed = models.DecimalField(max_digits=6, decimal_places=2)
    stabilityclass = models.CharField(max_length=1, blank=True, null=True)
    topography = models.CharField(max_length=1, blank=True, null=True)
    endpoint_distance = models.DecimalField(max_digits=5, decimal_places=1)
    residentialpopulation = models.CharField(max_length=9, blank=True, null=True)
    pr_schools = models.BooleanField()
    pr_residences = models.BooleanField()
    pr_hospitals = models.BooleanField()
    pr_prisons = models.BooleanField()
    pr_publicrecreation = models.BooleanField()
    pr_comm_ind = models.BooleanField()
    pr_othertype = models.CharField(max_length=200, blank=True, null=True)
    er_natlstateparks = models.BooleanField()
    er_wildlifesactuary = models.BooleanField()
    er_fedwilderness = models.BooleanField()
    er_othertype = models.CharField(max_length=200, blank=True, null=True)
    pm_dikes = models.BooleanField()
    pm_enclosures = models.BooleanField()
    pm_berms = models.BooleanField()
    pm_drains = models.BooleanField()
    pm_sumps = models.BooleanField()
    pm_othertype = models.CharField(max_length=200, blank=True, null=True)
    am_sprinklersystems = models.BooleanField()
    am_delugesystems = models.BooleanField()
    am_watercurtain = models.BooleanField()
    am_neutralization = models.BooleanField()
    am_excessflowvalve = models.BooleanField()
    am_flares = models.BooleanField()
    am_scrubbers = models.BooleanField()
    am_emergencyshutdown = models.BooleanField()
    am_othertype = models.CharField(max_length=200, blank=True, null=True)
    ptrgraphic = models.CharField(max_length=12, blank=True, null=True)
    cbi_flag = models.BooleanField()

    class Meta:
        db_table = 'tblS3ToxicsAltReleases'

class Tbls8Preventionprogram2(models.Model): #rmp_prevent_2
    preventionprogram2id = models.IntegerField(primary_key=True)
    process_naics_id = models.ForeignKey(
        ProcNaics,
        on_delete=models.CASCADE
    )
    safetyreviewdate = models.DateTimeField(blank=True, null=True)
    fr_nfpa58 = models.BooleanField()
    fr_osha = models.BooleanField()
    fr_astm = models.BooleanField()
    fr_ansi = models.BooleanField()
    fr_asme = models.BooleanField()
    fr_none = models.BooleanField()
    fr_othertype = models.CharField(max_length=200, blank=True, null=True)
    fr_comments = models.CharField(max_length=200, blank=True, null=True)
    hazardreviewdate = models.DateTimeField(blank=True, null=True)
    changecompletiondate = models.DateTimeField(blank=True, null=True)
    mh_toxicrelease = models.BooleanField()
    mh_fire = models.BooleanField()
    mh_explosion = models.BooleanField()
    mh_runawayreaction = models.BooleanField()
    mh_polymerization = models.BooleanField()
    mh_overpressurization = models.BooleanField()
    mh_corrosion = models.BooleanField()
    mh_overfilling = models.BooleanField()
    mh_contamination = models.BooleanField()
    mh_equipmentfailure = models.BooleanField()
    mh_coolingloss = models.BooleanField()
    mh_earthquake = models.BooleanField()
    mh_floods = models.BooleanField()
    mh_tornado = models.BooleanField()
    mh_hurricanes = models.BooleanField()
    mh_othertype = models.CharField(max_length=200, blank=True, null=True)
    pc_vents = models.BooleanField()
    pc_reliefvalves = models.BooleanField()
    pc_checkvalves = models.BooleanField()
    pc_scrubbers = models.BooleanField()
    pc_flares = models.BooleanField()
    pc_manualshutoffs = models.BooleanField()
    pc_automaticshutoffs = models.BooleanField()
    pc_interlocks = models.BooleanField()
    pc_alarms = models.BooleanField()
    pc_keyedbypass = models.BooleanField()
    pc_emergencyairsupply = models.BooleanField()
    pc_emergencypower = models.BooleanField()
    pc_backuppump = models.BooleanField()
    pc_groundingequipment = models.BooleanField()
    pc_inhibitoraddition = models.BooleanField()
    pc_rupturedisks = models.BooleanField()
    pc_excessflowdevice = models.BooleanField()
    pc_quenchsystem = models.BooleanField()
    pc_purgesystem = models.BooleanField()
    pc_none = models.BooleanField()
    pc_othertype = models.CharField(max_length=200, blank=True, null=True)
    ms_sprinklersystem = models.BooleanField()
    ms_dikes = models.BooleanField()
    ms_firewalls = models.BooleanField()
    ms_blastwalls = models.BooleanField()
    ms_delugesystem = models.BooleanField()
    ms_watercurtain = models.BooleanField()
    ms_enclosure = models.BooleanField()
    ms_neutralization = models.BooleanField()
    ms_none = models.BooleanField()
    ms_othertype = models.CharField(max_length=200, blank=True, null=True)
    md_processareadetectors = models.BooleanField()
    md_perimetermonitors = models.BooleanField()
    md_none = models.BooleanField()
    md_othertype = models.CharField(max_length=200, blank=True, null=True)
    ch_chemicalreduction = models.BooleanField()
    ch_chemicalincrease = models.BooleanField()
    ch_changeprocessparameters = models.BooleanField()
    ch_installprocesscontrols = models.BooleanField()
    ch_installprocessdetection = models.BooleanField()
    ch_installperimetermonitoring = models.BooleanField()
    ch_installmitigationsystems = models.BooleanField()
    ch_nonerequired = models.BooleanField()
    ch_none = models.BooleanField()
    ch_otherchanges = models.CharField(max_length=-1, blank=True, null=True)
    opproceduresreviewdate = models.DateTimeField(blank=True, null=True)
    trainingreviewdate = models.DateTimeField(blank=True, null=True)
    tr_classroom = models.BooleanField()
    tr_onthejob = models.BooleanField()
    tr_othertype = models.CharField(max_length=-1, blank=True, null=True)
    ct_writtentest = models.BooleanField()
    ct_oraltest = models.BooleanField()
    ct_demonstration = models.BooleanField()
    ct_observation = models.BooleanField()
    ct_othertype = models.CharField(max_length=-1, blank=True, null=True)
    maintenancereviewdate = models.DateTimeField(blank=True, null=True)
    equipmentinspectiondate = models.DateTimeField(blank=True, null=True)
    equipmenttested = models.CharField(max_length=-1, blank=True, null=True)
    complianceauditdate = models.DateTimeField(blank=True, null=True)
    auditcompletiondate = models.DateTimeField(blank=True, null=True)
    incidentinvestigationdate = models.DateTimeField(blank=True, null=True)
    investigationchangedate = models.DateTimeField(blank=True, null=True)
    mostrecentchangedate = models.DateTimeField(blank=True, null=True)
    cbi_flag = models.BooleanField()
    description = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        db_table = 'tblS8PreventionProgram2'

class rmp_prevent_3(models.Model):
    prevent_3_id = models.IntegerField(primary_key=True)
    procnaics_id = models.ForeignKey(
        ProcNaics,
        on_delete=models.CASCADE
    )
    safety_info_date = models.DateTimeField()
    last_pha_date = models.DateTimeField()
    pha_whatif = models.BooleanField()
    pha_checklist = models.BooleanField()
    pha_whatifcheck = models.BooleanField()
    pha_hazop = models.BooleanField()
    pha_fmea = models.BooleanField()
    pha_fta = models.BooleanField()
    pha_other = models.CharField(max_length=200, blank=True, null=True)
    change_comp_date = models.DateTimeField()
    mh_toxicrelease = models.BooleanField()
    mh_fire = models.BooleanField()
    mh_explosion = models.BooleanField()
    mh_runawayreact = models.BooleanField()
    mh_polymerization = models.BooleanField()
    mh_overpressure = models.BooleanField()
    mh_corrosion = models.BooleanField()
    mh_overfilling = models.BooleanField()
    mh_contamination = models.BooleanField()
    mh_equipfailure = models.BooleanField()
    mh_cooling_loss = models.BooleanField()
    mh_earthquake = models.BooleanField()
    mh_floods = models.BooleanField()
    mh_tornado = models.BooleanField()
    mh_hurricanes = models.BooleanField()
    mh_othertype = models.CharField(max_length=200, blank=True, null=True)
    pc_vents = models.BooleanField()
    pc_reliefvalves = models.BooleanField()
    pc_checkvalves = models.BooleanField()
    pc_scrubbers = models.BooleanField()
    pc_flares = models.BooleanField()
    pc_manualshutoffs = models.BooleanField()
    pc_autoshutoffs = models.BooleanField()
    pc_interlocks = models.BooleanField()
    pc_alarms = models.BooleanField()
    pc_keyedbypass = models.BooleanField()
    pc_emergencyair = models.BooleanField()
    pc_emergencypower = models.BooleanField()
    pc_backuppump = models.BooleanField()
    pc_groundingequip = models.BooleanField()
    pc_inhibitoradd = models.BooleanField()
    pc_rupturedisks = models.BooleanField()
    pc_excessflowdev = models.BooleanField()
    pc_quenchsystem = models.BooleanField()
    pc_purgesystem = models.BooleanField()
    pc_none = models.BooleanField()
    pc_other = models.CharField(max_length=200, blank=True, null=True)
    mx_sprinklersys = models.BooleanField()
    ms_dikes = models.BooleanField()
    ms_firewalls = models.BooleanField()
    ms_blastwalls = models.BooleanField()
    ms_delugesystem = models.BooleanField()
    ms_watercurtain = models.BooleanField()
    ms_enclosure = models.BooleanField()
    ms_neutralization = models.BooleanField()
    ms_none = models.BooleanField()
    ms_other = models.CharField(max_length=200, blank=True, null=True)
    md_processare = models.BooleanField()
    md_perimetermon = models.BooleanField()
    md_none = models.BooleanField()
    md_other = models.CharField(max_length=200, blank=True, null=True)
    ch_reduceinv = models.BooleanField()
    ch_increaseinv = models.BooleanField()
    ch_changeparam = models.BooleanField()
    ch_proccontrol = models.BooleanField()
    ch_procdetect = models.BooleanField()
    ch_perimetermon = models.BooleanField()
    ch_mitigationsys = models.BooleanField()
    ch_nonerequired = models.BooleanField()
    ch_none = models.BooleanField()
    ch_other = models.CharField(max_length=200, blank=True, null=True)
    proc_review_date = models.DateTimeField()
    train_review_date = models.DateTimeField()
    tr_classroom = models.BooleanField()
    tr_onthejob = models.BooleanField()
    tr_other = models.CharField(max_length=200, blank=True, null=True)
    ct_writtentest = models.BooleanField()
    ct_oraltest  = models.BooleanField()
    ct_demonstration = models.BooleanField()
    ct_observation = models.BooleanField()
    ct_other = models.CharField(max_length=200, blank=True, null=True)
    maint_review_date = models.DateTimeField()
    maint_inspect_date = models.DateTimeField()
    equip_tested = models.CharField(max_length=200, blank=True, null=True)
    change_manage_date = models.DateTimeField()
    change_review_date = models.DateTimeField()
    prestart_rev_date = models.DateTimeField()
    comp_audit_date = models.DateTimeField()
    audit_comp_date = models.DateTimeField()
    inc_invest_date = models.DateTimeField()
    inc_change_date = models.DateTimeField()
    part_review_date = models.DateTimeField()
    hotwork_rev_date = models.DateTimeField()
    con_safety_date = models.DateTimeField()
    con_eval_date = models.DateTimeField()
    cbi_flag = models.BooleanField()

    # TODO AGGREGATE

    num_prevent_3_chem =
    num_prev3text =
    num_prev3_text =

class Tbls9Emergencyresponses(models.Model): #rmp_response
    facilityid = models.ForeignKey(
        rmp_registration,
        on_delete=models.CASCADE,
    )
    er_communityplan = models.BooleanField()
    er_facilityplan = models.BooleanField()
    er_responseactions = models.BooleanField()
    er_publicinfoprocedures = models.BooleanField()
    er_emergencyhealthcare = models.BooleanField()
    er_reviewdate = models.DateTimeField(blank=True, null=True)
    ertrainingdate = models.DateTimeField(blank=True, null=True)
    coordinatingagencyname = models.CharField(max_length=250, blank=True, null=True)
    coordinatingagencyphone = models.CharField(max_length=10, blank=True, null=True)
    fr_osha1910_38 = models.BooleanField()
    fr_osha1910_120 = models.BooleanField()
    fr_spcc = models.BooleanField()
    fr_rcra = models.BooleanField()
    fr_opa90 = models.BooleanField()
    fr_epcra = models.BooleanField()
    fr_otherregulation = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'tblS9EmergencyResponses'

class ProcChem(models.Model):
    procchem_id = models.IntegerField(primary_key=True)
    process_id = models.ForeignKey(
        Rmp_process,
        on_delete=models.CASCADE
    )
    chemical_id = models.ForeignKey(
        ChemCd,
        on_delete=models.CASCADE
    )
    quantity_lbs = models.IntegerField()
    cbi_flag = models.BooleanField()
    num_alt_flam = models.IntegerField()
    num_alt_tox = models.IntegerField()
    num_prevent_2_chem = models.IntegerField()
    num_prevent_3_chem = models.IntegerField()
    num_proc_flam = models.IntegerField()
    num_worst_flam = models.IntegerField()
    num_worst_tox =models.IntegerField()
    cas = models.IntegerField()
    chemical_type = models.CharField(max_length=1)

    class Meta:
        db_table = 'rmp_proc_chem'


class ProcFlam(models.Model):
    flammixchem_id = models.IntegerField(primary_key=True)
    procchem_id = models.ForeignKey(
        ProcChem,
        on_delete=models.CASCADE
    )
    chemical_id = models.ForeignKey(
        ChemCd,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'rmp_proc_flam'

class ProcNaics(models.Model):
    procnaics_id = models.IntegerField(primary_key=True)
    process_id = models.ForeignKey(
        Rmp_process,
        on_delete=models.CASCADE
    )
    naics = models.IntegerField()
    num_prevent_2 = models.IntegerField()
    num_prevent_3 = models.IntegerField()

    class Meta:
        db_table = 'rmp_proc_naics'

class Rmp_prev2text(models.Model):
    prevent_2_id = models.ForeignKey(
        Tbls8Preventionprogram2,
        on_delete=models.CASCADE
    )
    desctext = models.TextField()

    class Meta:
        db_table = 'rmp_prev2text'

class Rmp_prev3text(models.Model):
    prevent_3_id = models.ForeignKey(
        rmp_prevent_3,
        on_delete=models.CASCADE
    )
    desctext = models.TextField()

    class Meta:
        db_table = 'rmp_prev3text'

class Prevent2Chem(models.Model):
    primary_key = models.IntegerField(primary_key=True)

    # TODO foreign key ?
    prevent_2_id = models.ForeignKey(
        Tbls8Preventionprogram2,
        on_delete=models.CASCADE
    )

    # TODO foreign key ?
    procchem_id = models.ForeignKey(
        ProcChem,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'rmp_prevent_2_chem'


class Prevent3Chem(models.Model):
    primary_key = models.IntegerField(primary_key=True)

    #TODO Foreign key ?
    prevent_3_id = models.ForeignKey(
        rmp_prevent_3,
        on_delete=models.CASCADE
    )

    # TODO Foreign key ?
    procchem_id = models.ForiegnKey(
        ProcChem,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'rmp_prevent_3_chem'

class Tbls2Toxicsworstcase(models.Model):
    toxicid = models.IntegerField(primary_key=True)
    processchemicalid = models.ForeignKey(
        ProcChem,
        on_delete=models.CASCADE
    )
    percentweight = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    physicalstate = models.CharField(max_length=1, blank=True, null=True)
    analyticalbasis = models.CharField(max_length=255, blank=True, null=True)
    scenario = models.BooleanField(blank=True, null=True)
    quantityreleased = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    releaseduration = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    releaserate = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    windspeed = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    stabilityclass = models.CharField(max_length=1, blank=True, null=True)
    topography = models.CharField(max_length=1, blank=True, null=True)
    endpoint_distance = models.DecimalField(max_digits=5, decimal_places=1)
    residentialpopulation = models.BooleanField(blank=True, null=True)
    pr_schools = models.BooleanField()
    pr_residences = models.BooleanField()
    pr_hospitals = models.BooleanField()
    pr_prisons = models.BooleanField()
    pr_publicrecreation = models.BooleanField()
    pr_comm_ind = models.BooleanField()
    pr_othertype = models.CharField(max_length=200, blank=True, null=True)
    er_natlstateparks = models.BooleanField()
    er_wildlifesactuary = models.BooleanField()
    er_fedwilderness = models.BooleanField()
    er_othertype = models.CharField(max_length=200, blank=True, null=True)
    pm_dikes = models.BooleanField()
    pm_enclosures = models.BooleanField()
    pm_berms = models.BooleanField()
    pm_drains = models.BooleanField()
    pm_sumps = models.BooleanField()
    pm_othertype = models.CharField(max_length=200, blank=True, null=True)
    ptrgraphic = models.BooleanField(max_length=12, blank=True, null=True)
    cbi_flag = models.BooleanField()

    class Meta:
        db_table = 'tblS2ToxicsWorstCase'

class Tbls4Flammablesworstcase(models.Model):
    flammableid = models.IntegerField(primary_key=True)
    processchemicalid = models.ForeignKey(
        ProcChem,
        on_delete=models.CASCADE
    )
    analyticalbasis = models.CharField(max_length=255, blank=True, null=True)
    quantityreleased = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    endpoint_distance = models.DecimalField(max_digits=5, decimal_places=1)
    residentialpopulation = models.CharField(max_length=9, blank=True, null=True)
    pr_schools = models.BooleanField()
    pr_residences = models.BooleanField()
    pr_hospitals = models.BooleanField()
    pr_prisons = models.BooleanField()
    pr_publicrecreation = models.BooleanField()
    pr_comm_ind = models.BooleanField()
    pr_othertype = models.CharField(max_length=200, blank=True, null=True)
    er_natlstateparks = models.BooleanField()
    er_wildlifesactuary = models.BooleanField()
    er_fedwilderness = models.BooleanField()
    er_othertype = models.CharField(max_length=200, blank=True, null=True)
    pm_blastwalls = models.BooleanField()
    pm_othertype = models.CharField(max_length=200, blank=True, null=True)
    ptrgraphic = models.BooleanField(max_length=12, blank=True, null=True)
    cbi_flag = models.BooleanField()

    class Meta:
        db_table = 'tblS4FlammablesWorstCase'
