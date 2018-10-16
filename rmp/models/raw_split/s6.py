"""
tblS6AccidentChemicals.csv
tblS6AccidentHistory.csv
tblS6FlammableMixtureChemicals.csv
"""
from django.db import models
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDecimalField,
    CopyFromIntegerField,
    CopyFromForeignKey,
)
from rmp.models.base import BaseRMPModel


class Tbls6Accidentchemicals(BaseRMPModel):
    accidentchemicalid = models.IntegerField(primary_key=True)  # Field name made lowercase.
    accidenthistoryid = models.ForeignKey(
        'Tbls6Accidenthistory',
        on_delete=models.PROTECT,
    )  # Field name made lowercase.
    chemicalid = models.ForeignKey(
        'ChemCd',
        on_delete=models.PROTECT
    )  # Field name made lowercase.
    quantityreleased = models.IntegerField(null=True)  # Field name made lowercase.
    percentweight = models.DecimalField(max_digits=4, decimal_places=1, null=True)  # Field name made lowercase.

    source_file = 'tblS6AccidentChemicals'

    class Meta:
        db_table = 'tblS6AccidentChemicals'


class Tbls6Accidenthistory(BaseRMPModel):
    accidenthistoryid = models.IntegerField(primary_key=True)
    facilityid = models.ForeignKey(
        'Tbls1Facilities',
        on_delete=models.PROTECT,
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
    otherreleasesource = models.CharField(
        max_length=200,
        blank=True
    )
    windspeed = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    windspeedunitcode = models.CharField(max_length=1, blank=True)
    winddirection = models.CharField(max_length=3, blank=True)
    temperature = models.DecimalField(max_digits=6, decimal_places=2)
    stabilityclass = models.CharField(max_length=1, blank=True)
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
    ed_other = models.CharField(max_length=200, blank=True)
    initiatingevent = models.CharField(max_length=1, blank=True)
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
    cf_other = models.CharField(max_length=200, blank=True)
    offsiterespondersnotify = models.CharField(
        max_length=25, blank=True
    )
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
    ci_othertype = models.CharField(max_length=200, blank=True)
    cbi_flag = models.BooleanField()

    source_file = 'tblS6AccidentHistory'

    class Meta:
        db_table = 'tblS6AccidentHistory'


class Tbls6Flammablemixturechemicals(BaseRMPModel):
    flammixchemid = models.IntegerField(primary_key=True)  # Field name made lowercase.
    accidentchemicalid = models.ForeignKey(
        'Tbls6Accidentchemicals',
        on_delete=models.PROTECT,
    )  # Field name made lowercase.
    chemicalid = models.ForeignKey(
        'ChemCd',
        on_delete=models.PROTECT
    )  # Field name made lowercase.

    source_file = 'tblS6FlammableMixtureChemicals'

    class Meta:
        db_table = 'tblS6FlammableMixtureChemicals'
