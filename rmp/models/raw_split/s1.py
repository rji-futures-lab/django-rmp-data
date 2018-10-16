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
from rmp.models import BaseRMPModel


class Tblfacility(BaseRMPModel):
    epafacilityid = CopyFromIntegerField(primary_key=True)  # Field name made lowercase.
    facilityname = CopyFromCharField(max_length=200)  # Field name made lowercase.
    marplotid = CopyFromBooleanField(null=True)  # Field name made lowercase.
    cameoid = CopyFromBooleanField(null=True)  # Field name made lowercase.
    # rmpid = CopyFromForeignKey(
    #     'Tblexecutivesummaries', # <-????
    #     on_delete=models.PROTECT,
    # )
    rmpid = CopyFromIntegerField()
    facilitystr1 = CopyFromCharField(max_length=35) # Field name made lowercase.
    facilitystr2 = CopyFromCharField(max_length=35)  # Field name made lowercase.
    facilitycity = CopyFromCharField(max_length=19)  # Field name made lowercase.
    facilitystate = CopyFromCharField(max_length=2)  # Field name made lowercase.
    facilityzipcode = CopyFromCharField(max_length=5)  # Field name made lowercase.
    facility4digitzipext = CopyFromCharField(max_length=4)  # Field name made lowercase.
    facilitycountyfips = CopyFromIntegerField()  # Field name made lowercase.
    countoffacilityid = CopyFromIntegerField()  # Field name made lowercase.
    facilitylatdecdegs = CopyFromIntegerField()  # Field name made lowercase.
    facilitylongdecdegs = CopyFromIntegerField()  # Field name made lowercase.

    source_file = 'tblFacility'

    class Meta:
        db_table = 'tblFacility'

class Tbls1Facilities(BaseRMPModel):
    facilityid = CopyFromIntegerField(
        primary_key=True
    )
    facilityname = CopyFromCharField(max_length=255, blank=True)
    facilitystr1 = CopyFromCharField(max_length=35, blank=True)
    facilitystr2 = CopyFromCharField(max_length=35, blank=True)
    facilitycity = CopyFromCharField(max_length=19, blank=True)
    facilitystate = CopyFromCharField(max_length=2, blank=True)
    facilityzipcode = CopyFromCharField(max_length=5, blank=True)
    facility4digitzipext = CopyFromCharField(max_length=4, blank=True)  # Field name made lowercase.
    facilitycountyfips = CopyFromCharField(max_length=5, blank=True)  # Field name made lowercase.
    lepc = CopyFromCharField(max_length=30, blank=True)  # Field name made lowercase.
    facilitylatdecdegs = CopyFromDecimalField(max_digits=8, decimal_places=6)  # Field name made lowercase.
    facilitylongdecdegs = CopyFromDecimalField(max_digits=8, decimal_places=6)  # Field name made lowercase.
    validlatlongflag = CopyFromCharField(max_length=1, blank=True)  # Field name made lowercase.
    latlongmethod = CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    latlongdescription = CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    facilityurl = CopyFromCharField(max_length=100, blank=True)  # Field name made lowercase.
    facilityphonenumber = CopyFromCharField(max_length=10, blank=True)  # Field name made lowercase.
    facilityemailaddress = CopyFromCharField(max_length=100, blank=True)  # Field name made lowercase.
    facilityduns = CopyFromCharField(max_length=9, blank=True)  # Field name made lowercase.
    parentcompanyname = CopyFromCharField(max_length=250, blank=True)  # Field name made lowercase.
    company2name = CopyFromCharField(max_length=50, blank=True)  # Field name made lowercase.
    companyduns = CopyFromCharField(max_length=9, blank=True)  # Field name made lowercase.
    company2duns = CopyFromCharField(max_length=9, blank=True)  # Field name made lowercase.
    operatorname = CopyFromCharField(max_length=250, blank=True)  # Field name made lowercase.
    operatorphone = CopyFromCharField(max_length=10, blank=True)  # Field name made lowercase.
    operatorstr1 = CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    operatorstr2 = CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    operatorcity = CopyFromCharField(max_length=19, blank=True)  # Field name made lowercase.
    operatorstatefips = CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    operatorzipcode = CopyFromCharField(max_length=5, blank=True)  # Field name made lowercase.
    operatorzipcodeext = CopyFromCharField(max_length=4, blank=True)  # Field name made lowercase.
    rmpcontact = CopyFromCharField(max_length=35, blank=True) # Field name made lowercase.
    rmptitle = CopyFromCharField(max_length=250, blank=True)  # Field name made lowercase.
    emergencycontactname = CopyFromCharField(max_length=250, blank=True)  # Field name made lowercase.
    emergencycontacttitle = CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    emergencycontactphone = CopyFromCharField(max_length=10, blank=True)  # Field name made lowercase.
    phone24 = CopyFromCharField(max_length=10, blank=True)  # Field name made lowercase.
    emergencycontactext_pin = CopyFromCharField(max_length=10, blank=True)  # Field name made lowercase.
    fte = CopyFromIntegerField()  # Field name made lowercase.
    otherepafacilityid = CopyFromIntegerField()  # Field name made lowercase.
    epafacilityid = CopyFromForeignKey(
        Tblfacility,
        on_delete=models.PROTECT,
    )  # Field name made lowercase.
    osha_psm = CopyFromBooleanField()  # Field name made lowercase.
    epcra_302 = CopyFromBooleanField() # Field name made lowercase.
    caa_titlev = CopyFromBooleanField()# Field name made lowercase.
    clearairoppermitid = CopyFromIntegerField()  # Field name made lowercase.
    safetyinspectiondate = models.DateTimeField(blank=True)  # Field name made lowercase.
    safetyinspectionby = CopyFromCharField(max_length=50, blank=True)  # Field name made lowercase.
    osharanking = CopyFromBooleanField()# Field name made lowercase.
    predictivefilingflag = CopyFromBooleanField()  # Field name made lowercase.
    submissiontype = CopyFromCharField(max_length=1, blank=True)  # Field name made lowercase.
    rmpdescription = CopyFromCharField(max_length=50, blank=True)  # Field name made lowercase.
    noaccidents = CopyFromBooleanField()  # Field name made lowercase.
    foreignstateprov = CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    foreignzipcode = CopyFromCharField(max_length=14, blank=True)  # Field name made lowercase.
    foreigncountry = CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    cbi_flag = CopyFromBooleanField() # Field name made lowercase.
    completioncheckdate = models.DateTimeField(blank=True) # Field name made lowercase.
    errorreportdate = models.DateTimeField(blank=True)  # Field name made lowercase.
    receiptdate = CopyFromCharField(max_length=25, blank=True)  # Field name made lowercase.
    graphicsindicator = CopyFromBooleanField()  # Field name made lowercase.
    attachmentsindicator = CopyFromBooleanField()  # Field name made lowercase.
    certificationreceivedflag = CopyFromBooleanField()  # Field name made lowercase.
    submissionmethod = CopyFromCharField(max_length=50, blank=True)  # Field name made lowercase.
    cbisubstantiationflag = CopyFromBooleanField()  # Field name made lowercase.
    electronicwaiverreceivedflag = CopyFromBooleanField()  # Field name made lowercase.
    postmarkdate = models.DateTimeField(blank=True)  # Field name made lowercase.
    rmpcompleteflag = CopyFromBooleanField()  # Field name made lowercase.
    deregistrationdate = models.DateTimeField(blank=True)  # Field name made lowercase.
    deregistrationeffectivedate = models.DateTimeField(blank=True)  # Field name made lowercase.
    anniversarydate = models.DateTimeField(blank=True)  # Field name made lowercase.
    cbiflag = CopyFromBooleanField()  # Field name made lowercase.
    cbiunsanitizedversionflag = CopyFromBooleanField()  # Field name made lowercase.
    versionnumber = CopyFromCharField(max_length=200, blank=True)  # Field name made lowercase.
    frs_lat = CopyFromDecimalField(max_digits=8, decimal_places=5)  # Field name made lowercase.
    frs_long = CopyFromDecimalField(max_digits=8, decimal_places=5)  # Field name made lowercase.
    frs_description = CopyFromCharField(max_length=40, blank=True)  # Field name made lowercase.
    frs_method = CopyFromCharField(max_length=60, blank=True)  # Field name made lowercase.
    horizontalaccmeasure = CopyFromCharField(max_length=6, blank=True)  # Field name made lowercase.
    horizontalrefdatumcode = CopyFromCharField(max_length=3, blank=True) # Field name made lowercase.
    sourcemapscalenumber = CopyFromCharField(max_length=10, blank=True)  # Field name made lowercase.
    emergencycontactemail = CopyFromCharField(max_length=100, blank=True)  # Field name made lowercase.
    rmppreparername = CopyFromCharField(max_length=70, blank=True)  # Field name made lowercase.
    rmppreparerstreet1 = CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    rmppreparerstreet2 = CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    rmppreparercity = CopyFromCharField(max_length=30, blank=True)  # Field name made lowercase.
    rmppreparerstate = CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    rmppreparerzip = CopyFromCharField(max_length=5, blank=True)  # Field name made lowercase.
    rmppreparerzip4ext = CopyFromCharField(max_length=4, blank=True)  # Field name made lowercase.
    rmppreparertelephone = CopyFromCharField(max_length=10, blank=True)# Field name made lowercase.
    rmppreparerforeignstateorprovince = CopyFromCharField(max_length=35, blank=True)  # Field name made lowercase.
    rmppreparerforeigncountry = CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    rmppreparerforeignpostalcode = CopyFromCharField(max_length=14, blank=True)  # Field name made lowercase.
    rmpsubmissionreasoncode = CopyFromCharField(max_length=3, blank=True)  # Field name made lowercase.
    rmpemail = CopyFromCharField(max_length=100, blank=True)  # Field name made lowercase.
    deregistrationreasoncode = CopyFromCharField(max_length=2, blank=True)  # Field name made lowercase.
    deregistrationreasonothertext = CopyFromCharField(max_length=80, blank=True)  # Field name made lowercase.

    source_file = 'tblS1Facilities'

    class Meta:
        db_table = 'tblS1Facilities'

class Tbls1Flammablemixturechemicals(BaseRMPModel):
    flammixchemid = CopyFromIntegerField(primary_key=True)  # Field name made lowercase.
    processchemicalid = CopyFromForeignKey(
        'tbls1ProcessChemicals',
        on_delete=models.PROTECT,
    )  # Field name made lowercase.
    chemicalid = CopyFromForeignKey(
        # 'TlkpChemicals', # <- source file
        'ChemCd',
        on_delete=models.PROTECT
    )  # Field name made lowercase.

    source_file = 'tblS1FlammableMixtureChemicals'

    class Meta:
        db_table = 'tblS1FlammableMixtureChemicals'


class Tbls1Processchemicals(BaseRMPModel):
    processchemicalid = CopyFromIntegerField(primary_key=True)  # Field name made lowercase.
    processid = CopyFromForeignKey(
        'Tbls1Processes',
        on_delete=models.PROTECT
    )  # Field name made lowercase.
    chemicalid = CopyFromForeignKey(
        # 'TlkpChemicals', # <- source file
        'ChemCd',
        on_delete=models.PROTECT
    )  # Field name made lowercase.
    quantity = CopyFromDecimalField(
        max_digits=6,
        decimal_places=2,
    )  # Field name made lowercase.
    cbi_flag = CopyFromBooleanField()  # Field name made lowercase.

    source_file = 'tblS1ProcessChemicals'

    class Meta:
        db_table = 'tblS1ProcessChemicals'


class Tbls1ProcessNaics(BaseRMPModel):
    process_naics_id = CopyFromIntegerField(primary_key=True)
    processid = CopyFromForeignKey(
        'Tbls1Processes',
        on_delete=models.PROTECT,
    )
    naicscode = CopyFromIntegerField()

    source_file = 'tblS1Process_NAICS'

    class Meta:
        db_table = 'tblS1Process_NAICS'

class Tbls1Processes(BaseRMPModel):
    processid = CopyFromIntegerField()
    altid = CopyFromCharField(
        max_length=25,
    )
    facilityid = CopyFromForeignKey(
        'Tbls1Facilities',
        on_delete=models.PROTECT,
    )
    programlevel = CopyFromCharField(
        max_length=1,
    )
    cbi_flag = CopyFromBooleanField()

    source_file = 'tblS1Processes'

    class Meta:
        db_table = 'tblS1Processes'
