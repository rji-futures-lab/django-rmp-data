"""
Models for processed RMP data.
"""
import os
from django.conf import settings
from django.db import models
from django.db.models import F, Max, OuterRef, Subquery, Sum, Count, Case, When, Value
from django.db.models.functions import Coalesce
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
        qs = raw_models.tblS6AccidentChemicals.objects.select_related('ChemicalID').annotate(
            num_acc_flam=Subquery(
                raw_models.tblS6FlammableMixtureChemicals.objects.filter(
                    AccidentChemicalID=OuterRef('AccidentChemicalID')
                ).values('AccidentChemicalID').annotate(
                    num_acc_flam=Count('AccidentChemicalID')
                ).values('num_acc_flam')
            )
        ).annotate(
            accchem_id=F('AccidentChemicalID'),
            accident_id=F('AccidentHistoryID'),
            chemical_id=F('ChemicalID'),
            quantity_lbs=F('QuantityReleased'),
            percent_weight=F('PercentWeight'),
            num_acc_flam=F('num_acc_flam'),
            cas=F('ChemicalID__CASNumber'),
            chemical_type=F('ChemicalID__ChemType'),
        )

        return qs

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
        db_column='naics_code',
        max_length=6,
    )
    release_duration = CopyFromCharField(max_length=5)
    re_gas = CopyFromBooleanField()
    re_spill = CopyFromBooleanField()
    re_fire = CopyFromBooleanField()
    re_explosion = CopyFromBooleanField()
    re_reactive_incident = CopyFromBooleanField(
    )
    rs_storage_vessel = CopyFromBooleanField(
    )
    rs_piping = CopyFromBooleanField()
    rs_process_vessel = CopyFromBooleanField(
    )
    rs_transfer_hose = CopyFromBooleanField(
    )
    rs_valve = CopyFromBooleanField()
    rs_pump = CopyFromBooleanField()
    rs_joint = CopyFromBooleanField()
    other_release_source = CopyFromCharField(
        max_length=200,
        blank=True
    )
    wind_speed = CopyFromFloatField(
        null=True,
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
    )
    unknown_weather = CopyFromBooleanField()
    deaths_workers = CopyFromIntegerField()
    deaths_responders = CopyFromIntegerField()
    deaths_public = CopyFromIntegerField()
    injuries_workers = CopyFromIntegerField()
    injuries_responders = CopyFromIntegerField(
    )
    injuries_public = CopyFromIntegerField()
    onsite_damage = CopyFromIntegerField()
    offsite_deaths = CopyFromBooleanField()
    hospitalization = CopyFromIntegerField(
    )
    offsite_medical = CopyFromIntegerField()
    offsite_evacuated = CopyFromIntegerField()
    offsite_shelter = CopyFromIntegerField()
    offsite_damage = CopyFromIntegerField()
    ed_kills = CopyFromBooleanField()
    ed_defoliation = CopyFromBooleanField()
    ed_water_contamination = CopyFromBooleanField(
    )
    ed_soil_contamination = CopyFromBooleanField(
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
    )
    cf_human_error = CopyFromBooleanField(
    )
    cf_improper_procedure = CopyFromBooleanField(
    )
    cf_overpressure = CopyFromBooleanField()
    cf_upset_condition = CopyFromBooleanField(
    )
    cf_bypass_condition = CopyFromBooleanField(
    )
    cf_maintenance = CopyFromBooleanField()
    cf_process_design_failure = CopyFromBooleanField(
    )
    cf_unsuitable_equipment = CopyFromBooleanField(
    )
    cf_unusual_weather = CopyFromBooleanField(
    )
    cf_management_error = CopyFromBooleanField(
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

    #TODO TURN BELOW INTO AGGREGATE

    num_acc_chem = CopyFromIntegerField()
    flam_total = CopyFromIntegerField(
    )
    toxic_total = CopyFromIntegerField(
    )
    quantity_total = CopyFromIntegerField(
    )
    num_deaths = CopyFromIntegerField()
    num_injuries = CopyFromIntegerField()
    num_evacuated = CopyFromIntegerField()
    property_damage = CopyFromIntegerField()

    @classmethod
    def get_transform_queryset(self):
        qs = raw_models.tblS6AccidentHistory.objects.select_related('FacilityID').select_related('WindSpeedUnitCode').annotate(
            num_acc_chem=Subquery(
                raw_models.tblS6AccidentChemicals.objects.filter(
                    AccidentHistoryID=OuterRef('AccidentHistoryID')
                ).values('AccidentHistoryID').annotate(
                    num_acc_chem=Count('AccidentHistoryID')
                ).values('num_acc_chem')
            ),
            flam_total=Subquery(
                processed_models.AccChem.objects.filter(
                    accident_id=OuterRef('AccidentHistoryID')
                ).values('accident_id').filter(
                    chemical_type='F',
                ).exclude(
                    quantity_lbs__isnull=True,
                ).annotate(
                    flam_total=Coalesce(Sum('quantity_lbs'), 0),
                ).values('flam_total'),
                output_field=CopyFromIntegerField(),
                default=0,
            ),
            toxic_total=Subquery(
                processed_models.AccChem.objects.filter(
                    accident_id=OuterRef('AccidentHistoryID')
                ).values('accident_id').exclude(
                    quantity_lbs__isnull=True,
                ).filter(
                    chemical_type='T',
                ).annotate(
                    toxic_total=Coalesce(Sum('quantity_lbs'), 0),
                ).values('toxic_total'),
                output_field=CopyFromIntegerField(),
                default=0,
            ),
        ).annotate(
            num_deaths=F('DeathsWorkers') + F('DeathsPublicResponders') + F('DeathsPublic'),
            num_injuries=F('InjuriesPublic') + F('InjuriesWorkers') + F('InjuriesPublicResponders'),
            property_damage=F('OnsitePropertyDamage') + F('OffsitePropertyDamage'),
            quantity_total=F('flam_total') + F('toxic_total'),
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
            hospitalization=F('Hospitalization'),
            offsite_medical=F('MedicalTreatment'),
            offsite_evacuated=F('Evacuated'),
            offsite_shelter=F('ShelteredInPlace'),
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
            num_acc_chem=F('num_acc_chem'),
            flam_total=F('flam_total'),
            toxic_total=F('toxic_total'),
            quantity_total=F('quantity_total'),
            num_deaths=F('num_deaths'),
            num_injuries=F('num_injuries'),
            num_evacuated=F('Evacuated'),
            property_damage=F('property_damage'),
        )
        return qs
