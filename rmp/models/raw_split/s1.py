"""
tblFacility
tblS1Facilities.csv
tblS1FlammableMixtureChemicals.csv
tblS1Process_NAICS.csv
tblS1ProcessChemicals.csv
tblS1Processes.csv
"""

from django.db import models
from rmp.fields import (
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDecimalField,
    CopyFromIntegerField,
    CopyFromForeignKey,
)
from .base import BaseRMPModel

class Tblfacility(BaseRMPModel):
    epafacilityid = models.CopyFromIntegerField(primary_key=True)  # Field name made lowercase.
    facilityname = models.CopyFromCharField(max_length=200)  # Field name made lowercase.
    marplotid = models.CopyFromBooleanField(null=True)  # Field name made lowercase.
    cameoid = models.CopyFromBooleanField(null=True)  # Field name made lowercase.
    rmpid = models.CopyFromForeignKey(
        Tbls1Facilities,
        on_delete=models.PROTECT,
    )  # Field name made lowercase.
    facilitystr1 = models.CopyFromCharField() # Field name made lowercase.
    facilitystr2 = models.CopyFromCharField()  # Field name made lowercase.
    facilitycity = models.CopyFromCharField()  # Field name made lowercase.
    facilitystate = models.CopyFromCharField(max_length=2)  # Field name made lowercase.
    facilityzipcode = models.CopyFromCharField(max_length=5)  # Field name made lowercase.
    facility4digitzipext = models.CopyFromCharField(max_length=4)  # Field name made lowercase.
    facilitycountyfips = models.CopyFromIntegerField()  # Field name made lowercase.
    countoffacilityid = models.CopyFromIntegerField()  # Field name made lowercase.
    facilitylatdecdegs = models.CopyFromIntegerField()  # Field name made lowercase.
    facilitylongdecdegs = models.CopyFromIntegerField()  # Field name made lowercase.

    source_file = 'tblFacility'

    class Meta:
        db_table = 'tblFacility'

class Tbls1Facilities(BaseRMPModel):
    facilityid = models.models.CopyFromIntegerField(
        primary_key=True
    )
    facilityname = models.CopyFromCharField(max_length=255, blank=True)
    facilitystr1 = models.CopyFromCharField(max_length=35, blank=True)
    facilitystr2 = models.CopyFromCharField(max_length=35, blank=True)
    facilitycity = models.CopyFromCharField(max_length=19, blank=True)
    facilitystate = models.CopyFromCharField(max_length=2, blank=True)
    facilityzipcode = models.CopyFromCharField(max_length=5, blank=True)
    facility4digitzipext = models.CopyFromCharField(max_length=4, blank=True)  # Field name made lowercase.
    facilitycountyfips = models.CopyFromCharField(max_length=5, blank=True)  # Field name made lowercase.
    lepc = models.CopyFromCharField(max_length=30, blank=True)  # Field name made lowercase.
    facilitylatdecdegs = models.CopyFromDecimalField(max_digits=8, decimal_places=6)  # Field name made lowercase.
    facilitylongdecdegs = models.CopyFromDecimalField(max_digits=8, decimal_places=6)  # Field name made lowercase.
    validlatlongflag = models.CopyFromCharField(max_length=1, blank=True)  # Field name made lowercase.
    latlongmethod = models.CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    latlongdescription = models.CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    facilityurl = models.CopyFromCharField(max_length=100, blank=True)  # Field name made lowercase.
    facilityphonenumber = models.CopyFromCharField(max_length=10, blank=True)  # Field name made lowercase.
    facilityemailaddress = models.CopyFromCharField(max_length=100, blank=True)  # Field name made lowercase.
    facilityduns = models.CopyFromCharField(max_length=9, blank=True)  # Field name made lowercase.
    parentcompanyname = models.CopyFromCharField(max_length=250, blank=True)  # Field name made lowercase.
    company2name = models.CopyFromCharField(max_length=50, blank=True)  # Field name made lowercase.
    companyduns = models.CopyFromCharField(max_length=9, blank=True)  # Field name made lowercase.
    company2duns = models.CopyFromCharField(max_length=9, blank=True)  # Field name made lowercase.
    operatorname = models.CopyFromCharField(max_length=250, blank=True)  # Field name made lowercase.
    operatorphone = models.CopyFromCharField(max_length=10, blank=True)  # Field name made lowercase.
    operatorstr1 = models.CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    operatorstr2 = models.CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    operatorcity = models.CopyFromCharField(max_length=19, blank=True)  # Field name made lowercase.
    operatorstatefips = models.CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    operatorzipcode = models.CopyFromCharField(max_length=5, blank=True)  # Field name made lowercase.
    operatorzipcodeext = models.CopyFromCharField(max_length=4, blank=True)  # Field name made lowercase.
    rmpcontact = models.CopyFromCharField(max_length=35, blank=True) # Field name made lowercase.
    rmptitle = models.CopyFromCharField(max_length=250, blank=True)  # Field name made lowercase.
    emergencycontactname = models.CopyFromCharField(max_length=250, blank=True)  # Field name made lowercase.
    emergencycontacttitle = models.CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    emergencycontactphone = models.CopyFromCharField(max_length=10, blank=True)  # Field name made lowercase.
    phone24 = models.CopyFromCharField(max_length=10, blank=True)  # Field name made lowercase.
    emergencycontactext_pin = models.CopyFromCharField(max_length=10, blank=True)  # Field name made lowercase.
    fte = models.CopyFromIntegerField()  # Field name made lowercase.
    otherepafacilityid = models.CopyFromIntegerField()  # Field name made lowercase.
    epafacilityid = models.CopyFromForeignKey(
        Tblfacility,
        on_delete=models.PROTECTED,
    )  # Field name made lowercase.
    osha_psm = models.CopyFromBooleanField()  # Field name made lowercase.
    epcra_302 = models.CopyFromBooleanField() # Field name made lowercase.
    caa_titlev = models.CopyFromBooleanField()# Field name made lowercase.
    clearairoppermitid = models.CopyFromIntegerField()  # Field name made lowercase.
    safetyinspectiondate = models.DateTimeField(blank=True)  # Field name made lowercase.
    safetyinspectionby = models.CopyFromCharField(max_length=50, blank=True)  # Field name made lowercase.
    osharanking = models.CopyFromBooleanField()# Field name made lowercase.
    predictivefilingflag = models.CopyFromBooleanField()  # Field name made lowercase.
    submissiontype = models.CopyFromCharField(max_length=1, blank=True)  # Field name made lowercase.
    rmpdescription = models.CopyFromCharField(max_length=50, blank=True)  # Field name made lowercase.
    noaccidents = models.CopyFromBooleanField()  # Field name made lowercase.
    foreignstateprov = models.CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    foreignzipcode = models.CopyFromCharField(max_length=14, blank=True)  # Field name made lowercase.
    foreigncountry = models.CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    cbi_flag = models.CopyFromBooleanField() # Field name made lowercase.
    completioncheckdate = models.DateTimeField(blank=True) # Field name made lowercase.
    errorreportdate = models.DateTimeField(blank=True)  # Field name made lowercase.
    receiptdate = models.CopyFromCharField(max_length=25, blank=True)  # Field name made lowercase.
    graphicsindicator = models.CopyFromBooleanField()  # Field name made lowercase.
    attachmentsindicator = models.CopyFromBooleanField()  # Field name made lowercase.
    certificationreceivedflag = models.CopyFromBooleanField()  # Field name made lowercase.
    submissionmethod = models.CopyFromCharField(max_length=50, blank=True)  # Field name made lowercase.
    cbisubstantiationflag = models.CopyFromBooleanField()  # Field name made lowercase.
    electronicwaiverreceivedflag = models.CopyFromBooleanField()  # Field name made lowercase.
    postmarkdate = models.DateTimeField(blank=True)  # Field name made lowercase.
    rmpcompleteflag = models.CopyFromBooleanField()  # Field name made lowercase.
    deregistrationdate = models.DateTimeField(blank=True)  # Field name made lowercase.
    deregistrationeffectivedate = models.DateTimeField(blank=True)  # Field name made lowercase.
    anniversarydate = models.DateTimeField(blank=True)  # Field name made lowercase.
    cbiflag = models.CopyFromBooleanField()  # Field name made lowercase.
    cbiunsanitizedversionflag = models.CopyFromBooleanField()  # Field name made lowercase.
    versionnumber = models.CopyFromCharField(max_length=200, blank=True)  # Field name made lowercase.
    frs_lat = models.CopyFromDecimalField(max_digits=8, decimal_places=5)  # Field name made lowercase.
    frs_long = models.CopyFromDecimalField(max_digits=8, decimal_places=5)  # Field name made lowercase.
    frs_description = models.CopyFromCharField(max_length=40, blank=True)  # Field name made lowercase.
    frs_method = models.CopyFromCharField(max_length=60, blank=True)  # Field name made lowercase.
    horizontalaccmeasure = models.CopyFromCharField(max_length=6, blank=True)  # Field name made lowercase.
    horizontalrefdatumcode = models.CopyFromCharField(max_length=3, blank=True) # Field name made lowercase.
    sourcemapscalenumber = models.CopyFromCharField(max_length=10, blank=True)  # Field name made lowercase.
    emergencycontactemail = models.CopyFromCharField(max_length=100, blank=True)  # Field name made lowercase.
    rmppreparername = models.CopyFromCharField(max_length=70, blank=True)  # Field name made lowercase.
    rmppreparerstreet1 = models.CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    rmppreparerstreet2 = models.CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    rmppreparercity = models.CopyFromCharField(max_length=30, blank=True)  # Field name made lowercase.
    rmppreparerstate = models.CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    rmppreparerzip = models.CopyFromCharField(max_length=5, blank=True)  # Field name made lowercase.
    rmppreparerzip4ext = models.CopyFromCharField(max_length=4, blank=True)  # Field name made lowercase.
    rmppreparertelephone = models.CopyFromCharField(max_length=10, blank=True)# Field name made lowercase.
    rmppreparerforeignstateorprovince = models.CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    rmppreparerforeigncountry = models.CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    rmppreparerforeignpostalcode = models.CopyFromCharField(max_length=14, blank=True)  # Field name made lowercase.
    rmpsubmissionreasoncode = models.CopyFromCharField(max_length=3, blank=True)  # Field name made lowercase.
    rmpemail = models.CopyFromCharField(max_length=100, blank=True)  # Field name made lowercase.
    deregistrationreasoncode = models.CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    deregistrationreasonothertext = models.CopyFromCharField(max_length=80, blank=True)  # Field name made lowercase.

    source_file = 'tblS1Facilities'

    class Meta:
        db_table = 'tblS1Facilities'

class Tbls1Flammablemixturechemicals(BaseRMPModel):
    flammixchemid = models.CopyFromIntegerField(primary_key=True)  # Field name made lowercase.
    processchemicalid = models.CopyFromForeignKey(
        tbls1ProcessChemicals,
        on_delete=models.PROTECT,
    )  # Field name made lowercase.
    chemicalid = models.CopyFromForeignKey(
        TlkpChemicals,
        on_delete=models.PROTECT
    )  # Field name made lowercase.

    source_file = 'tblS1FlammableMixtureChemicals'

    class Meta:
        db_table = 'tblS1FlammableMixtureChemicals'


class Tbls1Processchemicals(BaseRMPModel):
    processchemicalid = models.CopyFromIntegerField(primary_key=True)  # Field name made lowercase.
    processid = models.CopyFromForeignKey(
        Tbls1Processes,
        on_delete=models.PROTECT
    )  # Field name made lowercase.
    chemicalid = models.CopyFromForeignKey(
        TlkpChemicals,
        on_delete=models.PROTECT
    )  # Field name made lowercase.
    quantity = models.CopyFromDecimalField()  # Field name made lowercase.
    cbi_flag = models.CopyFromBooleanField()  # Field name made lowercase.

    source_file = 'tblS1ProcessChemicals'

    class Meta:
        db_table = 'tblS1ProcessChemicals'

class Tbls1ProcessNaics(BaseRMPModel):
    process_naics_id = models.CopyFromIntegerField(primary_key=True)
    processid = models.CopyFromForeignKey(
        Tbls1Processes,
        on_delete=models.PROTECT,
    )
    naicscode = models.CopyFromIntegerField()

    source_file = 'tblS1Process_NAICS'

    class Meta:
        db_table = 'tblS1Process_NAICS'

class Tbls1Processes(BaseRMPModel):
    processid = models.CopyFromIntegerField()
    altid = models.CopyFromCharField()
    facilityid = models.CopyFromForeignKey(
        Tbls1Facilities,
        on_delete=models.PROTECT,
    )
    programlevel = models.CopyFromCharField()
    cbi_flag = models.CopyFromBooleanField()

    source_file = 'tblS1Processes'

    class Meta:
        db_table = 'tblS1Processes'
