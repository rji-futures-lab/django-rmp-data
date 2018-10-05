# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from postgres_copy import CopyManager

# class Tblexecutivesummaries(models.Model):
#     esseqnum = models.DecimalField(db_column='ESSeqNum', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     facilityid = models.DecimalField(db_column='FacilityID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     summarytext = models.CharField(db_column='SummaryText', max_length=-1, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tblExecutiveSummaries'


# class Tbls1Flammablemixturechemicals(models.Model):
#     flammixchemid = models.DecimalField(db_column='FlamMixChemID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     processchemicalid = models.DecimalField(db_column='ProcessChemicalID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     chemicalid = models.DecimalField(db_column='ChemicalID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tblS1FlammableMixtureChemicals'


# class Tbls2Toxicsworstcase(models.Model):
#     toxicid = models.DecimalField(db_column='ToxicID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     processchemicalid = models.DecimalField(db_column='ProcessChemicalID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     percentweight = models.DecimalField(db_column='PercentWeight', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     physicalstate = models.CharField(db_column='PhysicalState', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     analyticalbasis = models.CharField(db_column='AnalyticalBasis', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     scenario = models.BooleanField(db_column='Scenario', blank=True, null=True)  # Field name made lowercase.
#     quantityreleased = models.BooleanField(db_column='QuantityReleased', blank=True, null=True)  # Field name made lowercase.
#     releaseduration = models.DecimalField(db_column='ReleaseDuration', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     releaserate = models.BooleanField(db_column='ReleaseRate', blank=True, null=True)  # Field name made lowercase.
#     windspeed = models.DecimalField(db_column='WindSpeed', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     stabilityclass = models.CharField(db_column='StabilityClass', max_length=-1)  # Field name made lowercase.
#     topography = models.CharField(db_column='Topography', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     distance2endpoint = models.BooleanField(db_column='Distance2Endpoint', blank=True, null=True)  # Field name made lowercase.
#     residentialpopulation = models.BooleanField(db_column='ResidentialPopulation', blank=True, null=True)  # Field name made lowercase.
#     pr_schools = models.BooleanField(db_column='PR_Schools')  # Field name made lowercase.
#     pr_residences = models.BooleanField(db_column='PR_Residences')  # Field name made lowercase.
#     pr_hospitals = models.BooleanField(db_column='PR_Hospitals')  # Field name made lowercase.
#     pr_prisons = models.BooleanField(db_column='PR_Prisons')  # Field name made lowercase.
#     pr_publicrecreation = models.BooleanField(db_column='PR_PublicRecreation')  # Field name made lowercase.
#     pr_comm_ind = models.BooleanField(db_column='PR_Comm_Ind')  # Field name made lowercase.
#     pr_othertype = models.BooleanField(db_column='PR_OtherType', blank=True, null=True)  # Field name made lowercase.
#     er_natlstateparks = models.BooleanField(db_column='ER_NatlStateParks')  # Field name made lowercase.
#     er_wildlifesactuary = models.BooleanField(db_column='ER_WildlifeSactuary')  # Field name made lowercase.
#     er_fedwilderness = models.BooleanField(db_column='ER_FedWilderness')  # Field name made lowercase.
#     er_othertype = models.BooleanField(db_column='ER_OtherType', blank=True, null=True)  # Field name made lowercase.
#     pm_dikes = models.BooleanField(db_column='PM_Dikes')  # Field name made lowercase.
#     pm_enclosures = models.BooleanField(db_column='PM_Enclosures')  # Field name made lowercase.
#     pm_berms = models.BooleanField(db_column='PM_Berms')  # Field name made lowercase.
#     pm_drains = models.BooleanField(db_column='PM_Drains')  # Field name made lowercase.
#     pm_sumps = models.BooleanField(db_column='PM_Sumps')  # Field name made lowercase.
#     pm_othertype = models.CharField(db_column='PM_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     ptrgraphic = models.BooleanField(db_column='ptrGraphic', blank=True, null=True)  # Field name made lowercase.
#     cbi_flag = models.BooleanField(db_column='CBI_Flag')  # Field name made lowercase.

#     class Meta:
#         db_table = 'tblS2ToxicsWorstCase'


# class Tbls3Toxicsaltreleases(models.Model):
#     toxicid = models.DecimalField(db_column='ToxicID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     processchemicalid = models.DecimalField(db_column='ProcessChemicalID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     percentweight = models.DecimalField(db_column='PercentWeight', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     physicalstate = models.CharField(db_column='PhysicalState', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     analyticalbasis = models.CharField(db_column='AnalyticalBasis', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     scenario = models.BooleanField(db_column='Scenario', blank=True, null=True)  # Field name made lowercase.
#     quantityreleased = models.BooleanField(db_column='QuantityReleased', blank=True, null=True)  # Field name made lowercase.
#     releaseduration = models.BooleanField(db_column='ReleaseDuration', blank=True, null=True)  # Field name made lowercase.
#     releaserate = models.BooleanField(db_column='ReleaseRate', blank=True, null=True)  # Field name made lowercase.
#     windspeed = models.DecimalField(db_column='WindSpeed', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     stabilityclass = models.CharField(db_column='StabilityClass', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     topography = models.CharField(db_column='Topography', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     distance2endpoint = models.BooleanField(db_column='Distance2Endpoint', blank=True, null=True)  # Field name made lowercase.
#     residentialpopulation = models.BooleanField(db_column='ResidentialPopulation', blank=True, null=True)  # Field name made lowercase.
#     pr_schools = models.BooleanField(db_column='PR_Schools')  # Field name made lowercase.
#     pr_residences = models.BooleanField(db_column='PR_Residences')  # Field name made lowercase.
#     pr_hospitals = models.BooleanField(db_column='PR_Hospitals')  # Field name made lowercase.
#     pr_prisons = models.BooleanField(db_column='PR_Prisons')  # Field name made lowercase.
#     pr_publicrecreation = models.BooleanField(db_column='PR_PublicRecreation')  # Field name made lowercase.
#     pr_comm_ind = models.BooleanField(db_column='PR_Comm_Ind')  # Field name made lowercase.
#     pr_othertype = models.BooleanField(db_column='PR_OtherType', blank=True, null=True)  # Field name made lowercase.
#     er_natlstateparks = models.BooleanField(db_column='ER_NatlStateParks')  # Field name made lowercase.
#     er_wildlifesactuary = models.BooleanField(db_column='ER_WildlifeSactuary')  # Field name made lowercase.
#     er_fedwilderness = models.BooleanField(db_column='ER_FedWilderness')  # Field name made lowercase.
#     er_othertype = models.BooleanField(db_column='ER_OtherType', blank=True, null=True)  # Field name made lowercase.
#     pm_dikes = models.BooleanField(db_column='PM_Dikes')  # Field name made lowercase.
#     pm_enclosures = models.BooleanField(db_column='PM_Enclosures')  # Field name made lowercase.
#     pm_berms = models.BooleanField(db_column='PM_Berms')  # Field name made lowercase.
#     pm_drains = models.BooleanField(db_column='PM_Drains')  # Field name made lowercase.
#     pm_sumps = models.BooleanField(db_column='PM_Sumps')  # Field name made lowercase.
#     pm_othertype = models.CharField(db_column='PM_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     am_sprinklersystems = models.BooleanField(db_column='AM_SprinklerSystems')  # Field name made lowercase.
#     am_delugesystems = models.BooleanField(db_column='AM_DelugeSystems')  # Field name made lowercase.
#     am_watercurtain = models.BooleanField(db_column='AM_WaterCurtain')  # Field name made lowercase.
#     am_neutralization = models.BooleanField(db_column='AM_Neutralization')  # Field name made lowercase.
#     am_excessflowvalve = models.BooleanField(db_column='AM_ExcessFlowValve')  # Field name made lowercase.
#     am_flares = models.BooleanField(db_column='AM_Flares')  # Field name made lowercase.
#     am_scrubbers = models.BooleanField(db_column='AM_Scrubbers')  # Field name made lowercase.
#     am_emergencyshutdown = models.BooleanField(db_column='AM_EmergencyShutdown')  # Field name made lowercase.
#     am_othertype = models.CharField(db_column='AM_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     ptrgraphic = models.BooleanField(db_column='ptrGraphic', blank=True, null=True)  # Field name made lowercase.
#     cbi_flag = models.BooleanField(db_column='CBI_Flag')  # Field name made lowercase.

#     class Meta:
#         db_table = 'tblS3ToxicsAltReleases'


# class Tbls4Flammablesworstcase(models.Model):
#     flammableid = models.DecimalField(db_column='FlammableID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     processchemicalid = models.DecimalField(db_column='ProcessChemicalID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     analyticalbasis = models.CharField(db_column='AnalyticalBasis', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     quantityreleased = models.BooleanField(db_column='QuantityReleased', blank=True, null=True)  # Field name made lowercase.
#     distance2endpoint = models.BooleanField(db_column='Distance2Endpoint', blank=True, null=True)  # Field name made lowercase.
#     residentialpopulation = models.BooleanField(db_column='ResidentialPopulation', blank=True, null=True)  # Field name made lowercase.
#     pr_schools = models.BooleanField(db_column='PR_Schools')  # Field name made lowercase.
#     pr_residences = models.BooleanField(db_column='PR_Residences')  # Field name made lowercase.
#     pr_hospitals = models.BooleanField(db_column='PR_Hospitals')  # Field name made lowercase.
#     pr_prisons = models.BooleanField(db_column='PR_Prisons')  # Field name made lowercase.
#     pr_publicrecreation = models.BooleanField(db_column='PR_PublicRecreation')  # Field name made lowercase.
#     pr_comm_ind = models.BooleanField(db_column='PR_Comm_Ind')  # Field name made lowercase.
#     pr_othertype = models.BooleanField(db_column='PR_OtherType', blank=True, null=True)  # Field name made lowercase.
#     er_natlstateparks = models.BooleanField(db_column='ER_NatlStateParks')  # Field name made lowercase.
#     er_wildlifesactuary = models.BooleanField(db_column='ER_WildlifeSactuary')  # Field name made lowercase.
#     er_fedwilderness = models.BooleanField(db_column='ER_FedWilderness')  # Field name made lowercase.
#     er_othertype = models.BooleanField(db_column='ER_OtherType', blank=True, null=True)  # Field name made lowercase.
#     pm_blastwalls = models.BooleanField(db_column='PM_BlastWalls')  # Field name made lowercase.
#     pm_othertype = models.CharField(db_column='PM_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     ptrgraphic = models.BooleanField(db_column='ptrGraphic', blank=True, null=True)  # Field name made lowercase.
#     cbi_flag = models.BooleanField(db_column='CBI_Flag')  # Field name made lowercase.

#     class Meta:
#         db_table = 'tblS4FlammablesWorstCase'


# class Tbls5Flammablesaltreleases(models.Model):
#     flammableid = models.DecimalField(db_column='FlammableID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     processchemicalid = models.DecimalField(db_column='ProcessChemicalID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     analyticalbasis = models.CharField(db_column='AnalyticalBasis', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     scenario = models.BooleanField(db_column='Scenario', blank=True, null=True)  # Field name made lowercase.
#     quantityreleased = models.BooleanField(db_column='QuantityReleased', blank=True, null=True)  # Field name made lowercase.
#     endpointused = models.BooleanField(db_column='EndpointUsed', blank=True, null=True)  # Field name made lowercase.
#     lfl_value = models.BooleanField(db_column='LFL_Value', blank=True, null=True)  # Field name made lowercase.
#     distance2endpoint = models.BooleanField(db_column='Distance2Endpoint', blank=True, null=True)  # Field name made lowercase.
#     residentialpopulation = models.BooleanField(db_column='ResidentialPopulation', blank=True, null=True)  # Field name made lowercase.
#     pr_schools = models.BooleanField(db_column='PR_Schools')  # Field name made lowercase.
#     pr_residences = models.BooleanField(db_column='PR_Residences')  # Field name made lowercase.
#     pr_hospitals = models.BooleanField(db_column='PR_Hospitals')  # Field name made lowercase.
#     pr_prisons = models.BooleanField(db_column='PR_Prisons')  # Field name made lowercase.
#     pr_publicrecreation = models.BooleanField(db_column='PR_PublicRecreation')  # Field name made lowercase.
#     pr_comm_ind = models.BooleanField(db_column='PR_Comm_Ind')  # Field name made lowercase.
#     pr_othertype = models.BooleanField(db_column='PR_OtherType', blank=True, null=True)  # Field name made lowercase.
#     er_natlstateparks = models.BooleanField(db_column='ER_NatlStateParks')  # Field name made lowercase.
#     er_wildlifesactuary = models.BooleanField(db_column='ER_WildlifeSactuary')  # Field name made lowercase.
#     er_fedwilderness = models.BooleanField(db_column='ER_FedWilderness')  # Field name made lowercase.
#     er_othertype = models.BooleanField(db_column='ER_OtherType', blank=True, null=True)  # Field name made lowercase.
#     pm_dikes = models.BooleanField(db_column='PM_Dikes')  # Field name made lowercase.
#     pm_firewalls = models.BooleanField(db_column='PM_FireWalls')  # Field name made lowercase.
#     pm_blastwalls = models.BooleanField(db_column='PM_BlastWalls')  # Field name made lowercase.
#     pm_enclosures = models.BooleanField(db_column='PM_Enclosures')  # Field name made lowercase.
#     pm_othertype = models.CharField(db_column='PM_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     am_sprinklersystems = models.BooleanField(db_column='AM_SprinklerSystems')  # Field name made lowercase.
#     am_delugesystems = models.BooleanField(db_column='AM_DelugeSystems')  # Field name made lowercase.
#     am_watercurtain = models.BooleanField(db_column='AM_WaterCurtain')  # Field name made lowercase.
#     am_excessflowvalve = models.BooleanField(db_column='AM_ExcessFlowValve')  # Field name made lowercase.
#     am_othertype = models.CharField(db_column='AM_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     ptrgraphic = models.BooleanField(db_column='ptrGraphic', blank=True, null=True)  # Field name made lowercase.
#     cbi_flag = models.BooleanField(db_column='CBI_Flag')  # Field name made lowercase.

#     class Meta:
#         db_table = 'tblS5FlammablesAltReleases'


class Tbls6Accidentchemicals(models.Model):
    accchem_id = models.IntegerField(
        primary_key=True,
        verbose_name='Accident Chemical Record ID',
        help_text='A unique ID for each accident chemical record.',
    )
    # TODO: ForeignKeyField candidate
    accident_id = models.IntegerField(
        help_text='The unique ID for each accident record',
    )
    # TODO: ForeignKeyField candidate
    chemical_id = models.IntegerField(
        help_text='The identifying ID for a particular chemical released in an '
                  'accident.',
    )
    quantity_lbs = models.DecimalField(
        decimal_places=1,
        max_digits=8,
        null=True,
        verbose_name='Amount Released (lbs)',
        help_text='The amount of the substance released in the accident, in '
                  'pounds, to two significant digits.',
    )
    # TODO: db_fields.tsv says this should be a float field, will decimal work?
    percent_weight = models.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=5,
        verbose_name='Percent Weight (Within Mixture)',
        help_text='The percent weight of a chemical within a mixture released '
                  'in an accident.',
    )

    objects = CopyManager()

    class Meta:
        db_table = 'tblS6AccidentChemicals'


# class Tbls6Accidenthistory(models.Model):
#     accidenthistoryid = models.DecimalField(db_column='AccidentHistoryID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     facilityid = models.DecimalField(db_column='FacilityID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     accidentdate = models.DateTimeField(db_column='AccidentDate', blank=True, null=True)  # Field name made lowercase.
#     accidenttime = models.DecimalField(db_column='AccidentTime', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     naicscode = models.DecimalField(db_column='NAICSCode', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     accidentreleaseduration = models.DecimalField(db_column='AccidentReleaseDuration', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     re_gas = models.BooleanField(db_column='RE_Gas')  # Field name made lowercase.
#     re_spill = models.BooleanField(db_column='RE_Spill')  # Field name made lowercase.
#     re_fire = models.BooleanField(db_column='RE_Fire')  # Field name made lowercase.
#     re_explosion = models.BooleanField(db_column='RE_Explosion')  # Field name made lowercase.
#     re_reactiveincident = models.BooleanField(db_column='RE_ReactiveIncident')  # Field name made lowercase.
#     rs_storagevessel = models.BooleanField(db_column='RS_StorageVessel')  # Field name made lowercase.
#     rs_piping = models.BooleanField(db_column='RS_Piping')  # Field name made lowercase.
#     rs_processvessel = models.BooleanField(db_column='RS_ProcessVessel')  # Field name made lowercase.
#     rs_transferhose = models.BooleanField(db_column='RS_TransferHose')  # Field name made lowercase.
#     rs_valve = models.BooleanField(db_column='RS_Valve')  # Field name made lowercase.
#     rs_pump = models.BooleanField(db_column='RS_Pump')  # Field name made lowercase.
#     rs_joint = models.BooleanField(db_column='RS_Joint')  # Field name made lowercase.
#     otherreleasesource = models.CharField(db_column='OtherReleaseSource', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     windspeed = models.DecimalField(db_column='WindSpeed', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     windspeedunitcode = models.CharField(db_column='WindSpeedUnitCode', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     winddirection = models.CharField(db_column='WindDirection', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     temperature = models.DecimalField(db_column='Temperature', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     stabilityclass = models.CharField(db_column='StabilityClass', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     precipitation = models.BooleanField(db_column='Precipitation')  # Field name made lowercase.
#     weatherunknown = models.BooleanField(db_column='WeatherUnknown')  # Field name made lowercase.
#     deathsworkers = models.DecimalField(db_column='DeathsWorkers', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     deathspublicresponders = models.DecimalField(db_column='DeathsPublicResponders', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     deathspublic = models.DecimalField(db_column='DeathsPublic', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     injuriesworkers = models.DecimalField(db_column='InjuriesWorkers', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     injuriespublicresponders = models.DecimalField(db_column='InjuriesPublicResponders', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     injuriespublic = models.DecimalField(db_column='InjuriesPublic', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     onsitepropertydamage = models.DecimalField(db_column='OnsitePropertyDamage', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     offsitedeaths = models.BooleanField(db_column='OffsiteDeaths', blank=True, null=True)  # Field name made lowercase.
#     hospitalization = models.DecimalField(db_column='Hospitalization', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     medicaltreatment = models.DecimalField(db_column='MedicalTreatment', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     evacuated = models.DecimalField(db_column='Evacuated', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     shelteredinplace = models.DecimalField(db_column='ShelteredInPlace', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     offsitepropertydamage = models.DecimalField(db_column='OffsitePropertyDamage', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     ed_kills = models.BooleanField(db_column='ED_Kills')  # Field name made lowercase.
#     ed_minordefoliation = models.BooleanField(db_column='ED_MinorDefoliation')  # Field name made lowercase.
#     ed_watercontamination = models.BooleanField(db_column='ED_WaterContamination')  # Field name made lowercase.
#     ed_soilcontamination = models.BooleanField(db_column='ED_SoilContamination')  # Field name made lowercase.
#     ed_other = models.CharField(db_column='ED_Other', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     initiatingevent = models.CharField(db_column='InitiatingEvent', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     cf_equipmentfailure = models.BooleanField(db_column='CF_EquipmentFailure')  # Field name made lowercase.
#     cf_humanerror = models.BooleanField(db_column='CF_HumanError')  # Field name made lowercase.
#     cf_improperprocedure = models.BooleanField(db_column='CF_ImproperProcedure')  # Field name made lowercase.
#     cf_overpressurization = models.BooleanField(db_column='CF_Overpressurization')  # Field name made lowercase.
#     cf_upsetcondition = models.BooleanField(db_column='CF_UpsetCondition')  # Field name made lowercase.
#     cf_bypasscondition = models.BooleanField(db_column='CF_BypassCondition')  # Field name made lowercase.
#     cf_maintenance = models.BooleanField(db_column='CF_Maintenance')  # Field name made lowercase.
#     cf_processdesignfailure = models.BooleanField(db_column='CF_ProcessDesignFailure')  # Field name made lowercase.
#     cf_unsuitableequipment = models.BooleanField(db_column='CF_UnsuitableEquipment')  # Field name made lowercase.
#     cf_unusualweather = models.BooleanField(db_column='CF_UnusualWeather')  # Field name made lowercase.
#     cf_managementerror = models.BooleanField(db_column='CF_ManagementError')  # Field name made lowercase.
#     cf_other = models.CharField(db_column='CF_Other', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     offsiterespondersnotify = models.CharField(db_column='OffsiteRespondersNotify', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     ci_improvedequipment = models.BooleanField(db_column='CI_ImprovedEquipment')  # Field name made lowercase.
#     ci_revisedmaintenance = models.BooleanField(db_column='CI_RevisedMaintenance')  # Field name made lowercase.
#     ci_revisedtraining = models.BooleanField(db_column='CI_RevisedTraining')  # Field name made lowercase.
#     ci_revisedopprocedures = models.BooleanField(db_column='CI_RevisedOpProcedures')  # Field name made lowercase.
#     ci_newprocesscontrols = models.BooleanField(db_column='CI_NewProcessControls')  # Field name made lowercase.
#     ci_newmitigationsystems = models.BooleanField(db_column='CI_NewMitigationSystems')  # Field name made lowercase.
#     ci_revisederplan = models.BooleanField(db_column='CI_RevisedERPlan')  # Field name made lowercase.
#     ci_changedprocess = models.BooleanField(db_column='CI_ChangedProcess')  # Field name made lowercase.
#     ci_reducedinventory = models.BooleanField(db_column='CI_ReducedInventory')  # Field name made lowercase.
#     ci_none = models.BooleanField(db_column='CI_None')  # Field name made lowercase.
#     ci_othertype = models.CharField(db_column='CI_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     cbi_flag = models.BooleanField(db_column='CBI_Flag')  # Field name made lowercase.

#     class Meta:
#         db_table = 'tblS6AccidentHistory'


# class Tbls8Preventionprogram2(models.Model):
#     preventionprogram2id = models.DecimalField(db_column='PreventionProgram2ID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     process_naics_id = models.DecimalField(db_column='Process_NAICS_ID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     safetyreviewdate = models.DateTimeField(db_column='SafetyReviewDate', blank=True, null=True)  # Field name made lowercase.
#     fr_nfpa58 = models.BooleanField(db_column='FR_NFPA58')  # Field name made lowercase.
#     fr_osha = models.BooleanField(db_column='FR_OSHA')  # Field name made lowercase.
#     fr_astm = models.BooleanField(db_column='FR_ASTM')  # Field name made lowercase.
#     fr_ansi = models.BooleanField(db_column='FR_ANSI')  # Field name made lowercase.
#     fr_asme = models.BooleanField(db_column='FR_ASME')  # Field name made lowercase.
#     fr_none = models.BooleanField(db_column='FR_None')  # Field name made lowercase.
#     fr_othertype = models.CharField(db_column='FR_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     fr_comments = models.CharField(db_column='FR_Comments', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     hazardreviewdate = models.DateTimeField(db_column='HazardReviewDate', blank=True, null=True)  # Field name made lowercase.
#     changecompletiondate = models.DateTimeField(db_column='ChangeCompletionDate', blank=True, null=True)  # Field name made lowercase.
#     mh_toxicrelease = models.BooleanField(db_column='MH_ToxicRelease')  # Field name made lowercase.
#     mh_fire = models.BooleanField(db_column='MH_Fire')  # Field name made lowercase.
#     mh_explosion = models.BooleanField(db_column='MH_Explosion')  # Field name made lowercase.
#     mh_runawayreaction = models.BooleanField(db_column='MH_RunawayReaction')  # Field name made lowercase.
#     mh_polymerization = models.BooleanField(db_column='MH_Polymerization')  # Field name made lowercase.
#     mh_overpressurization = models.BooleanField(db_column='MH_Overpressurization')  # Field name made lowercase.
#     mh_corrosion = models.BooleanField(db_column='MH_Corrosion')  # Field name made lowercase.
#     mh_overfilling = models.BooleanField(db_column='MH_Overfilling')  # Field name made lowercase.
#     mh_contamination = models.BooleanField(db_column='MH_Contamination')  # Field name made lowercase.
#     mh_equipmentfailure = models.BooleanField(db_column='MH_EquipmentFailure')  # Field name made lowercase.
#     mh_coolingloss = models.BooleanField(db_column='MH_CoolingLoss')  # Field name made lowercase.
#     mh_earthquake = models.BooleanField(db_column='MH_Earthquake')  # Field name made lowercase.
#     mh_floods = models.BooleanField(db_column='MH_Floods')  # Field name made lowercase.
#     mh_tornado = models.BooleanField(db_column='MH_Tornado')  # Field name made lowercase.
#     mh_hurricanes = models.BooleanField(db_column='MH_Hurricanes')  # Field name made lowercase.
#     mh_othertype = models.CharField(db_column='MH_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     pc_vents = models.BooleanField(db_column='PC_Vents')  # Field name made lowercase.
#     pc_reliefvalves = models.BooleanField(db_column='PC_ReliefValves')  # Field name made lowercase.
#     pc_checkvalves = models.BooleanField(db_column='PC_CheckValves')  # Field name made lowercase.
#     pc_scrubbers = models.BooleanField(db_column='PC_Scrubbers')  # Field name made lowercase.
#     pc_flares = models.BooleanField(db_column='PC_Flares')  # Field name made lowercase.
#     pc_manualshutoffs = models.BooleanField(db_column='PC_ManualShutoffs')  # Field name made lowercase.
#     pc_automaticshutoffs = models.BooleanField(db_column='PC_AutomaticShutoffs')  # Field name made lowercase.
#     pc_interlocks = models.BooleanField(db_column='PC_Interlocks')  # Field name made lowercase.
#     pc_alarms = models.BooleanField(db_column='PC_Alarms')  # Field name made lowercase.
#     pc_keyedbypass = models.BooleanField(db_column='PC_KeyedBypass')  # Field name made lowercase.
#     pc_emergencyairsupply = models.BooleanField(db_column='PC_EmergencyAirSupply')  # Field name made lowercase.
#     pc_emergencypower = models.BooleanField(db_column='PC_EmergencyPower')  # Field name made lowercase.
#     pc_backuppump = models.BooleanField(db_column='PC_BackupPump')  # Field name made lowercase.
#     pc_groundingequipment = models.BooleanField(db_column='PC_GroundingEquipment')  # Field name made lowercase.
#     pc_inhibitoraddition = models.BooleanField(db_column='PC_InhibitorAddition')  # Field name made lowercase.
#     pc_rupturedisks = models.BooleanField(db_column='PC_RuptureDisks')  # Field name made lowercase.
#     pc_excessflowdevice = models.BooleanField(db_column='PC_ExcessFlowDevice')  # Field name made lowercase.
#     pc_quenchsystem = models.BooleanField(db_column='PC_QuenchSystem')  # Field name made lowercase.
#     pc_purgesystem = models.BooleanField(db_column='PC_PurgeSystem')  # Field name made lowercase.
#     pc_none = models.BooleanField(db_column='PC_None')  # Field name made lowercase.
#     pc_othertype = models.CharField(db_column='PC_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     ms_sprinklersystem = models.BooleanField(db_column='MS_SprinklerSystem')  # Field name made lowercase.
#     ms_dikes = models.BooleanField(db_column='MS_Dikes')  # Field name made lowercase.
#     ms_firewalls = models.BooleanField(db_column='MS_FireWalls')  # Field name made lowercase.
#     ms_blastwalls = models.BooleanField(db_column='MS_BlastWalls')  # Field name made lowercase.
#     ms_delugesystem = models.BooleanField(db_column='MS_DelugeSystem')  # Field name made lowercase.
#     ms_watercurtain = models.BooleanField(db_column='MS_WaterCurtain')  # Field name made lowercase.
#     ms_enclosure = models.BooleanField(db_column='MS_Enclosure')  # Field name made lowercase.
#     ms_neutralization = models.BooleanField(db_column='MS_Neutralization')  # Field name made lowercase.
#     ms_none = models.BooleanField(db_column='MS_None')  # Field name made lowercase.
#     ms_othertype = models.CharField(db_column='MS_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     md_processareadetectors = models.BooleanField(db_column='MD_ProcessAreaDetectors')  # Field name made lowercase.
#     md_perimetermonitors = models.BooleanField(db_column='MD_PerimeterMonitors')  # Field name made lowercase.
#     md_none = models.BooleanField(db_column='MD_None')  # Field name made lowercase.
#     md_othertype = models.CharField(db_column='MD_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     ch_chemicalreduction = models.BooleanField(db_column='CH_ChemicalReduction')  # Field name made lowercase.
#     ch_chemicalincrease = models.BooleanField(db_column='CH_ChemicalIncrease')  # Field name made lowercase.
#     ch_changeprocessparameters = models.BooleanField(db_column='CH_ChangeProcessParameters')  # Field name made lowercase.
#     ch_installprocesscontrols = models.BooleanField(db_column='CH_InstallProcessControls')  # Field name made lowercase.
#     ch_installprocessdetection = models.BooleanField(db_column='CH_InstallProcessDetection')  # Field name made lowercase.
#     ch_installperimetermonitoring = models.BooleanField(db_column='CH_InstallPerimeterMonitoring')  # Field name made lowercase.
#     ch_installmitigationsystems = models.BooleanField(db_column='CH_InstallMitigationSystems')  # Field name made lowercase.
#     ch_nonerequired = models.BooleanField(db_column='CH_NoneRequired')  # Field name made lowercase.
#     ch_none = models.BooleanField(db_column='CH_None')  # Field name made lowercase.
#     ch_otherchanges = models.CharField(db_column='CH_OtherChanges', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     opproceduresreviewdate = models.DateTimeField(db_column='OpProceduresReviewDate', blank=True, null=True)  # Field name made lowercase.
#     trainingreviewdate = models.DateTimeField(db_column='TrainingReviewDate', blank=True, null=True)  # Field name made lowercase.
#     tr_classroom = models.BooleanField(db_column='TR_Classroom')  # Field name made lowercase.
#     tr_onthejob = models.BooleanField(db_column='TR_OnTheJob')  # Field name made lowercase.
#     tr_othertype = models.CharField(db_column='TR_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     ct_writtentest = models.BooleanField(db_column='CT_WrittenTest')  # Field name made lowercase.
#     ct_oraltest = models.BooleanField(db_column='CT_OralTest')  # Field name made lowercase.
#     ct_demonstration = models.BooleanField(db_column='CT_Demonstration')  # Field name made lowercase.
#     ct_observation = models.BooleanField(db_column='CT_Observation')  # Field name made lowercase.
#     ct_othertype = models.CharField(db_column='CT_OtherType', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     maintenancereviewdate = models.DateTimeField(db_column='MaintenanceReviewDate', blank=True, null=True)  # Field name made lowercase.
#     equipmentinspectiondate = models.DateTimeField(db_column='EquipmentInspectionDate', blank=True, null=True)  # Field name made lowercase.
#     equipmenttested = models.CharField(db_column='EquipmentTested', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     complianceauditdate = models.DateTimeField(db_column='ComplianceAuditDate', blank=True, null=True)  # Field name made lowercase.
#     auditcompletiondate = models.DateTimeField(db_column='AuditCompletionDate', blank=True, null=True)  # Field name made lowercase.
#     incidentinvestigationdate = models.DateTimeField(db_column='IncidentInvestigationDate', blank=True, null=True)  # Field name made lowercase.
#     investigationchangedate = models.DateTimeField(db_column='InvestigationChangeDate', blank=True, null=True)  # Field name made lowercase.
#     mostrecentchangedate = models.DateTimeField(db_column='MostRecentChangeDate', blank=True, null=True)  # Field name made lowercase.
#     cbi_flag = models.BooleanField(db_column='CBI_Flag')  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=-1, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tblS8PreventionProgram2'


# class Tbls8PreventionProgramChemicals(models.Model):
#     primarykey = models.DecimalField(db_column='PrimaryKey', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     preventionprogram2id = models.DecimalField(db_column='PreventionProgram2ID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     processchemicalid = models.DecimalField(db_column='ProcessChemicalID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tblS8_Prevention_Program_Chemicals'


# class Tbls9Emergencyresponses(models.Model):
#     facilityid = models.DecimalField(db_column='FacilityID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     er_communityplan = models.BooleanField(db_column='ER_CommunityPlan')  # Field name made lowercase.
#     er_facilityplan = models.BooleanField(db_column='ER_FacilityPlan')  # Field name made lowercase.
#     er_responseactions = models.BooleanField(db_column='ER_ResponseActions')  # Field name made lowercase.
#     er_publicinfoprocedures = models.BooleanField(db_column='ER_PublicInfoProcedures')  # Field name made lowercase.
#     er_emergencyhealthcare = models.BooleanField(db_column='ER_EmergencyHealthCare')  # Field name made lowercase.
#     er_reviewdate = models.DateTimeField(db_column='ER_ReviewDate', blank=True, null=True)  # Field name made lowercase.
#     ertrainingdate = models.DateTimeField(db_column='ERTrainingDate', blank=True, null=True)  # Field name made lowercase.
#     coordinatingagencyname = models.CharField(db_column='CoordinatingAgencyName', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     coordinatingagencyphone = models.DecimalField(db_column='CoordinatingAgencyPhone', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     fr_osha1910_38 = models.BooleanField(db_column='FR_OSHA1910_38')  # Field name made lowercase.
#     fr_osha1910_120 = models.BooleanField(db_column='FR_OSHA1910_120')  # Field name made lowercase.
#     fr_spcc = models.BooleanField(db_column='FR_SPCC')  # Field name made lowercase.
#     fr_rcra = models.BooleanField(db_column='FR_RCRA')  # Field name made lowercase.
#     fr_opa90 = models.BooleanField(db_column='FR_OPA90')  # Field name made lowercase.
#     fr_epcra = models.BooleanField(db_column='FR_EPCRA')  # Field name made lowercase.
#     fr_otherregulation = models.CharField(db_column='FR_OtherRegulation', max_length=-1, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tblS9EmergencyResponses'


# class Tlkpchemicals(models.Model):
#     chemicalid = models.DecimalField(db_column='ChemicalID', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     chemicalname = models.CharField(db_column='ChemicalName', max_length=-1)  # Field name made lowercase.
#     casnumber = models.CharField(db_column='CASNumber', max_length=-1, blank=True, null=True)  # Field name made lowercase.
#     threshold = models.DecimalField(db_column='Threshold', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
#     chemtype = models.BooleanField(db_column='ChemType', blank=True, null=True)  # Field name made lowercase.
#     flgcbi = models.BooleanField(db_column='flgCBI')  # Field name made lowercase.
#     chemowner = models.CharField(db_column='ChemOwner', max_length=-1, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tlkpChemicals'


# class Tlkpderegistrationreason(models.Model):
#     lookupcode = models.DecimalField(db_column='LookupCode', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=-1)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tlkpDeregistrationReason'


# class Tlkpdochandle(models.Model):
#     lookupcode = models.CharField(db_column='LookupCode', max_length=-1)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=-1)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tlkpDocHandle'


# class Tlkpdoctype(models.Model):
#     lookupcode = models.CharField(db_column='LookupCode', max_length=-1)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=-1)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tlkpDocType'


# class Tlkplatlongdescriptions(models.Model):
#     feat_code = models.CharField(db_column='Feat_Code', max_length=-1)  # Field name made lowercase.
#     feat_desc = models.CharField(db_column='Feat_Desc', max_length=-1)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tlkpLatLongDescriptions'


# class Tlkplatlongmethods(models.Model):
#     primary_key = models.DecimalField(db_column='Primary_Key', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
#     method_code = models.CharField(db_column='Method_Code', max_length=-1)  # Field name made lowercase.
#     method_desc = models.CharField(db_column='Method_Desc', max_length=-1)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tlkpLatLongMethods'


# class Tlkpphysicalstatecodes(models.Model):
#     lookupcode = models.CharField(db_column='LookupCode', max_length=-1)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=-1)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tlkpPhysicalStateCodes'


# class Tlkprejectreason(models.Model):
#     lookupcode = models.CharField(db_column='LookupCode', max_length=-1)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=-1)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tlkpRejectReason'


# class Tlkps2Scenariocodes(models.Model):
#     lookupcode = models.CharField(db_column='LookupCode', max_length=-1)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=-1)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tlkpS2ScenarioCodes'


# class Tlkps6Initiatingevents(models.Model):
#     lookupcode = models.CharField(db_column='LookupCode', max_length=-1)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=-1)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tlkpS6InitiatingEvents'


# class Tlkpsubmissionreasoncodes(models.Model):
#     lookupcode = models.CharField(db_column='LookupCode', max_length=-1)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=-1)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tlkpSubmissionReasonCodes'


# class Tlkptopographycode(models.Model):
#     lookupcode = models.CharField(db_column='LookupCode', max_length=-1)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=-1)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tlkpTopographyCode'


# class Tlkpwindspeedunitcodes(models.Model):
#     lookupcode = models.CharField(db_column='LookupCode', max_length=-1)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=-1)  # Field name made lowercase.

#     class Meta:
#         db_table = 'tlkpWindSpeedUnitCodes'
