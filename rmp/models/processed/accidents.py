"""
Models for processed RMP data.
"""
import os
from django.conf import settings
from django.db import models
from django.db.models import F, Max, OuterRef, Subquery, Sum, Count, Case, When, Value, Q
from django.db.models.functions import Cast, Coalesce
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
    CopyFromManyToManyField,
)
from rmp.models import raw as raw_models
from rmp.models import processed as processed_models
from rmp.models.base import BaseRMPModel


class Accident(BaseRMPModel):
    """
    Possible additions from Registration: Facility_name, city, county, parent_1? This would turn Process, Accident and Registration into the top level tables.
    """
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='accident_id',
    )
    rmp = CopyFromForeignKey(
        'Registration',
        on_delete=models.PROTECT,
    )
    accident_date = CopyFromDateField(
        null=True,
    )
    accident_time = CopyFromCharField(
        max_length=4,
        blank=True,
    )
    naics_code = CopyFromForeignKey(
        'NAICS',
        db_column='naics_code',
        on_delete=models.PROTECT,
    )
    release_duration = CopyFromCharField(
        max_length=5
    )
    re_gas = CopyFromBooleanField(
        verbose_name='Gas release',
    )
    re_spill = CopyFromBooleanField(
        verbose_name='Liquid spills/evaporation',
    )
    re_fire = CopyFromBooleanField(
        verbose_name='Fire',
    )
    re_explosion = CopyFromBooleanField(
        verbose_name='Explosion',
    )
    re_reactive_incident = CopyFromBooleanField(
        verbose_name='Uncontrolled/runaway reaction',
    )
    rs_storage_vessel = CopyFromBooleanField(
        verbose_name='Storage vessel',
    )
    rs_piping = CopyFromBooleanField(
        verbose_name='Piping',
    )
    rs_process_vessel = CopyFromBooleanField(
        verbose_name='Process vessel',
    )
    rs_transfer_hose = CopyFromBooleanField(
        verbose_name='Transfer hose',
    )
    rs_valve = CopyFromBooleanField(
        verbose_name='Valve',
    )
    rs_pump = CopyFromBooleanField(
        verbose_name='Pump',
    )
    rs_joint = CopyFromBooleanField(
        verbose_name='Joint',
    )
    other_release_source = CopyFromCharField(
        max_length=200,
        blank=True
    )
    wind_speed = CopyFromFloatField(
        null=True,
    )
    wind_speed_unit = CopyFromForeignKey(
        'WindCd',
        null=True,
        on_delete=models.PROTECT,
        db_column='wind_speed_unit',
    )
    wind_direction = CopyFromCharField(max_length=3, blank=True)
    temperature = CopyFromDecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    stability_class = CopyFromCharField(max_length=1, blank=True)
    precipitation = CopyFromBooleanField()
    unknown_weather = CopyFromBooleanField()
    deaths_workers = CopyFromIntegerField(null=True)
    deaths_responders = CopyFromIntegerField(null=True)
    deaths_public = CopyFromIntegerField(null=True)
    injuries_workers = CopyFromIntegerField(null=True)
    injuries_responders = CopyFromIntegerField(null=True)
    injuries_public = CopyFromIntegerField(null=True)
    onsite_damage = CopyFromIntegerField(null=True)
    offsite_deaths = CopyFromIntegerField(null=True)
    hospitalization = CopyFromIntegerField(null=True)
    offsite_medical = CopyFromIntegerField(null=True)
    offsite_evacuated = CopyFromIntegerField(null=True)
    offsite_shelter = CopyFromIntegerField(null=True)
    offsite_damage = CopyFromIntegerField(null=True)
    ed_kills = CopyFromBooleanField(
        verbose_name='Fish or animal kills',
    )
    ed_defoliation = CopyFromBooleanField(
        verbose_name='Tree, lawn, shrub, or crop damage',
    )
    ed_water_contamination = CopyFromBooleanField(
        verbose_name='Water contamination',
    )
    ed_soil_contamination = CopyFromBooleanField(
        verbose_name='Soil Contamination',
    )
    ed_other = CopyFromCharField(
        max_length=200,
        blank=True
    )
    initiating_event = CopyFromForeignKey(
        'EventsCd',
        null=True,
        on_delete=models.PROTECT,
        db_column='initiating_event',
    )
    cf_equipment_failure = CopyFromBooleanField(
        verbose_name='Equipment failure',
    )
    cf_human_error = CopyFromBooleanField(
        verbose_name='Human error',
    )
    cf_improper_procedure = CopyFromBooleanField(
        verbose_name='Improper procedure',
    )
    cf_overpressure = CopyFromBooleanField(
        verbose_name='Overpressurization',
    )
    cf_upset_condition = CopyFromBooleanField(
        verbose_name='Upset condition',
    )
    cf_bypass_condition = CopyFromBooleanField(
        verbose_name='By-pass condition',
    )
    cf_maintenance = CopyFromBooleanField(
        verbose_name='Maintenance activity/inactivity',
    )
    cf_process_design_failure = CopyFromBooleanField(
        verbose_name='Process design failure',
    )
    cf_unsuitable_equipment = CopyFromBooleanField(
        verbose_name='Unsuitable equipment',
    )
    cf_unusual_weather = CopyFromBooleanField(
        verbose_name='Unusual weather conditions',
    )
    cf_management_error = CopyFromBooleanField(
        verbose_name='Management error',
    )
    cf_other = CopyFromCharField(
        max_length=200,
        blank=True,
    )
    offsite_responders_notify = CopyFromCharField(
        max_length=25,
        blank=True,
    )
    ci_improved_equipment = CopyFromBooleanField(
    )
    ci_revised_maintenance = CopyFromBooleanField(
    )
    ci_revised_training = CopyFromBooleanField(
    )
    ci_revised_op_procedures = CopyFromBooleanField(
    )
    ci_new_process_controls = CopyFromBooleanField(
    )
    ci_new_mitigation_systems = CopyFromBooleanField(
    )
    ci_response_plan = CopyFromBooleanField(
    )
    ci_changed_process = CopyFromBooleanField(
    )
    ci_reduced_inventory = CopyFromBooleanField(
    )
    ci_none = CopyFromBooleanField()
    ci_other = CopyFromCharField(max_length=200, blank=True)
    cbi_flag = CopyFromBooleanField()
    num_acc_chem = CopyFromIntegerField(null=True)
    flam_total = CopyFromIntegerField(null=True)
    toxic_total = CopyFromIntegerField(null=True)
    quantity_total = CopyFromIntegerField(null=True)
    num_deaths = CopyFromIntegerField(null=True)
    num_injuries = CopyFromIntegerField(null=True)
    num_evacuated = CopyFromIntegerField(null=True)
    property_damage = CopyFromIntegerField(null=True)

    @classmethod
    def get_transform_queryset(self):
        """
        This is the top level containing information about accidents at different facilities.
        Aggregated fields:
        num_acc_chem = Counts AccidentIDs in tblS6AccidentChemicals
        flam_total, tox_total = Sums QuantityReleased column in accident chemicals depending on whether the ChemicalType flag is 'T' or 'F'
        quantity_total = Sum of flam_total and tox_total for each accident
        num_deaths = Sum of worker, public responder, and citizen deaths
        num_injuries = Sum of worker, public responder, and citizen injuries. These fields already exist on the raw models.
        property_damage = Sum of onsite and offsite property damage. Again, these fields already exist on the raw models.
        """
        qs = raw_models.tblS6AccidentHistory.objects.values(
            'AccidentHistoryID',
            'FacilityID',
            'AccidentDate',
            'AccidentTime',
            'NAICSCode',
            'AccidentReleaseDuration',
            'RE_Gas',
            'RE_Spill',
            'RE_Fire',
            'RE_Explosion',
            'RE_ReactiveIncident',
            'RS_StorageVessel',
            'RS_Piping',
            'RS_ProcessVessel',
            'RS_TransferHose',
            'RS_Valve',
            'RS_Pump',
            'RS_Joint',
            'OtherReleaseSource',
            'WindSpeed',
            'WindSpeedUnitCode',
            'WindDirection',
            'Temperature',
            'StabilityClass',
            'Precipitation',
            'WeatherUnknown',
            'DeathsWorkers',
            'DeathsPublicResponders',
            'DeathsPublic',
            'InjuriesWorkers',
            'InjuriesPublicResponders',
            'InjuriesPublic',
            'OnsitePropertyDamage',
            'OffsiteDeaths',
            'Hospitalization',
            'MedicalTreatment',
            'Evacuated',
            'ShelteredInPlace',
            'OffsitePropertyDamage',
            'ED_Kills',
            'ED_MinorDefoliation',
            'ED_WaterContamination',
            'ED_SoilContamination',
            'ED_Other',
            'InitiatingEvent',
            'CF_EquipmentFailure',
            'CF_HumanError',
            'CF_ImproperProcedure',
            'CF_Overpressurization',
            'CF_UpsetCondition',
            'CF_BypassCondition',
            'CF_Maintenance',
            'CF_ProcessDesignFailure',
            'CF_UnsuitableEquipment',
            'CF_UnusualWeather',
            'CF_ManagementError',
            'CF_Other',
            'OffsiteRespondersNotify',
            'CI_ImprovedEquipment',
            'CI_RevisedMaintenance',
            'CI_RevisedTraining',
            'CI_RevisedOpProcedures',
            'CI_NewProcessControls',
            'CI_NewMitigationSystems',
            'CI_RevisedERPlan',
            'CI_ChangedProcess',
            'CI_ReducedInventory',
            'CI_None',
            'CI_OtherType',
            'CBI_Flag',
        ).annotate(
            accident_id=F('AccidentHistoryID'),
            rmp_id=F('FacilityID'),
            accident_date=F('AccidentDate'),
            accident_time=F('AccidentTime'),
            naics_code=F('NAICSCode'),
            release_duration=F('AccidentReleaseDuration'),
            re_gas=F('RE_Gas'),
            re_spill=F('RE_Spill'),
            re_fire=F('RE_Fire'),
            re_explosion=F('RE_Explosion'),
            re_reactive_incident=F('RE_ReactiveIncident'),
            rs_storage_vessel=F('RS_StorageVessel'),
            rs_piping=F('RS_Piping'),
            rs_process_vessel=F('RS_ProcessVessel'),
            rs_transfer_hose=F('RS_TransferHose'),
            rs_valve=F('RS_Valve'),
            rs_pump=F('RS_Pump'),
            rs_joint=F('RS_Joint'),
            other_release_source=F('OtherReleaseSource'),
            wind_speed=F('WindSpeed'),
            wind_speed_unit=F('WindSpeedUnitCode'),
            wind_direction=F('WindDirection'),
            temperature=F('Temperature'),
            stability_class=F('StabilityClass'),
            precipitation=F('Precipitation'),
            unknown_weather=F('WeatherUnknown'),
            deaths_workers=F('DeathsWorkers'),
            deaths_responders=F('DeathsPublicResponders'),
            deaths_public=F('DeathsPublic'),
            injuries_workers=F('InjuriesWorkers'),
            injuries_responders=F('InjuriesPublicResponders'),
            injuries_public=F('InjuriesPublic'),
            onsite_damage=F('OnsitePropertyDamage'),
            offsite_deaths=F('OffsiteDeaths'),
            hospitalization=Cast('Hospitalization', CopyFromIntegerField()),
            offsite_medical=Cast('MedicalTreatment', CopyFromIntegerField()),
            offsite_evacuated=Cast('Evacuated', CopyFromIntegerField()),
            offsite_shelter=Cast('ShelteredInPlace', CopyFromIntegerField()),
            offsite_damage=F('OffsitePropertyDamage'),
            ed_kills=F('ED_Kills'),
            ed_defoliation=F('ED_MinorDefoliation'),
            ed_water_contamination=F('ED_WaterContamination'),
            ed_soil_contamination=F('ED_SoilContamination'),
            ed_other=F('ED_Other'),
            initiating_event=F('InitiatingEvent'),
            cf_equipment_failure=F('CF_EquipmentFailure'),
            cf_human_error=F('CF_HumanError'),
            cf_improper_procedure=F('CF_ImproperProcedure'),
            cf_overpressure=F('CF_Overpressurization'),
            cf_upset_condition=F('CF_UpsetCondition'),
            cf_bypass_condition=F('CF_BypassCondition'),
            cf_maintenance=F('CF_Maintenance'),
            cf_process_design_failure=F('CF_ProcessDesignFailure'),
            cf_unsuitable_equipment=F('CF_UnsuitableEquipment'),
            cf_unusual_weather=F('CF_UnusualWeather'),
            cf_management_error=F('CF_ManagementError'),
            cf_other=F('CF_Other'),
            offsite_responders_notify=F('OffsiteRespondersNotify'),
            ci_improved_equipment=F('CI_ImprovedEquipment'),
            ci_revised_maintenance=F('CI_RevisedMaintenance'),
            ci_revised_training=F('CI_RevisedTraining'),
            ci_revised_op_procedures=F('CI_RevisedOpProcedures'),
            ci_new_process_controls=F('CI_NewProcessControls'),
            ci_new_mitigation_systems=F('CI_NewMitigationSystems'),
            ci_response_plan=F('CI_RevisedERPlan'),
            ci_changed_process=F('CI_ChangedProcess'),
            ci_reduced_inventory=F('CI_ReducedInventory'),
            ci_none=F('CI_None'),
            ci_other=F('CI_OtherType'),
            cbi_flag=F('CBI_Flag'),
            num_acc_chem=Count('tbls6accidentchemicals'),
            flam_total=Sum(Case(When(tbls6accidentchemicals__ChemicalID__ChemType='F', then=('tbls6accidentchemicals__QuantityReleased')), default=Value(0))),
            toxic_total=Sum(Case(When(tbls6accidentchemicals__ChemicalID__ChemType='T', then=('tbls6accidentchemicals__QuantityReleased')), default=Value(0))),
            quantity_total=F('flam_total') + F('toxic_total'),
            num_deaths=F('DeathsWorkers') + F('DeathsPublicResponders') + F('DeathsPublic'),
            num_injuries=F('InjuriesPublic') + F('InjuriesWorkers') + F('InjuriesPublicResponders'),
            num_evacuated=F('Evacuated'),
            property_damage=F('OnsitePropertyDamage') + F('OffsitePropertyDamage'),
        )
        return qs

    @property
    def formatted_time(self):
        try:
            self._formatted_time
        except AttributeError:
            if self.accident_time == '':
                self._formatted_time = 'unspecified time'
            else:
                self._formatted_time = '{0}:{1}'.format(
                    self.accident_time[0:2],
                    self.accident_time[2:4],
                )

        return self._formatted_time

    @property
    def formatted_duration(self):
        try:
            self._formatted_duration
        except AttributeError:
            if self.release_duration != '':
                hrs = int(self.release_duration[0:3])
                mins = int( self.release_duration[3:6])

                if hrs > 0 and mins > 0:
                    self._formatted_duration = '{0} hours and {1} minutes'.format(
                        hrs, mins
                    )
                elif hrs > 0:
                    self._formatted_duration = '{0} hours'.format(hrs)
                elif mins > 0:
                    self._formatted_duration = '{0} minutes'.format(mins)
            else:
                self._formatted_duration = self.release_duration

        return self._formatted_duration

    @property
    def release_events(self):
        try:
            self._release_events
        except AttributeError:
            self._release_events = [
                f.verbose_name for f
                in self._meta.model.get_prefixed_boolean_fields('re_')
                if self.__dict__[f.name]
            ]

        return self._release_events

    @property
    def release_sources(self):
        try:
            self._release_sources
        except AttributeError:
            self._release_sources = [
                f.verbose_name for f
                in self._meta.model.get_prefixed_boolean_fields('rs_')
                if self.__dict__[f.name]
            ]

            if self.other_release_source != '':
                self._release_sources.append(self.other_release_source)

        return self._release_sources

    @property
    def environmental_damages(self):
        try:
            self._environmental_damages
        except AttributeError:
            self._environmental_damages = [
                f.verbose_name for f
                in self._meta.model.get_prefixed_boolean_fields('ed_')
                if self.__dict__[f.name]
            ]

            if self.ed_other != '':
                self._environmental_damages.append(self.ed_other)

        return self._environmental_damages

    @property
    def contributing_factors(self):
        try:
            self._contributing_factors
        except AttributeError:
            self._contributing_factors = [
                f.verbose_name for f
                in self._meta.model.get_prefixed_boolean_fields('cf_')
                if self.__dict__[f.name]
            ]

            if self.cf_other != '':
                self._contributing_factors.append(self.cf_other)

        return self._contributing_factors

    @property
    def changes_introduced(self):
        try:
            self._changes_introduced
        except AttributeError:
            self._changes_introduced = [
                f.verbose_name for f
                in self._meta.model.get_prefixed_boolean_fields('ci_')
                if self.__dict__[f.name]
            ]

            if self.ci_other != '':
                self._changes_introduced.append(self.ci_other)

        return self._changes_introduced


    class Meta:
        ordering = ['rmp_id', '-accident_date']


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

    @classmethod
    def get_transform_queryset(self):
        """
        num_acc_fhem is calculated by getting the count of AccidentChemicalID from tblS6FlammableMixtureChemicals
        """
        qs = raw_models.tblS6AccidentChemicals.objects.annotate(
            accchem_id=F('AccidentChemicalID'),
            accident_id=F('AccidentHistoryID'),
            chemical_id=F('ChemicalID'),
            quantity_lbs=F('QuantityReleased'),
            percent_weight=F('PercentWeight'),
            num_acc_flam=Count('tbls6flammablemixturechemicals'),
            cas=F('ChemicalID__CASNumber'),
            chemical_type=F('ChemicalID__ChemType'),
        ).order_by('accchem_id')

        return qs

class AccFlam(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='FlamMixChemID',
        verbose_name='Flammable Chemical ID',
        help_text='A unique ID for each flammable chemical record.',
    )
    accchem = CopyFromForeignKey(
        'AccChem',
        on_delete=models.PROTECT,
        source_column='AccidentChemicalID',
        verbose_name='Accident Chemical Record ID',
        help_text='A unique ID for each accident chemical record.'
    )
    chemical = CopyFromForeignKey(
        'ChemCd',
        on_delete=models.PROTECT,
        source_column='ChemicalID',
        verbose_name='Chemical ID',
        help_text='The identifying ID for a particular flammable chemical released in an accident.',
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tblS6FlammableMixtureChemicals
        """
        Baseline table for accidents
        """
        return m.objects.get_default_transform_queryset()
