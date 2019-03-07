"""
Models for processed RMP data.
"""
import os
from django.conf import settings
from django.db import models
from django.db.models import (
    F, Max, OuterRef, Subquery, Sum, Count, Case, When, Value
)
from django.db.models.functions import Cast
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


class Process(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='process_id',
    )
    process_desc = CopyFromCharField(max_length=25, blank=True)
    rmp = CopyFromForeignKey(
        'Registration',
        on_delete=models.PROTECT,
    )
    program_level = CopyFromIntegerField()
    cbi_flag = CopyFromBooleanField()
    num_proc_chem = CopyFromIntegerField()
    num_proc_naics = CopyFromIntegerField()
    num_worst_tox = CopyFromIntegerField()
    num_worst_flam = CopyFromIntegerField()
    num_alt_tox = CopyFromIntegerField()
    num_alt_flam = CopyFromIntegerField()
    # num_prev_2 = CopyFromIntegerField()
    # num_prev_3 = CopyFromIntegerField()
    toxic_tot = CopyFromBigIntegerField()
    flam_tot = CopyFromBigIntegerField()
    quantity_tot = CopyFromBigIntegerField()

    @classmethod
    def get_transform_queryset(self):
        qs = raw_models.tblS1Processes.objects.annotate(
            process_id=F('ProcessID'),
            process_desc=F('AltID'),
            rmp_id=F('FacilityID'),
            program_level=F('ProgramLevel'),
            cbi_flag=F('CBI_Flag'),
            num_proc_chem=Count('tbls1processchemicals'),
            num_proc_naics=Count('tbls1process_naics'),
            num_worst_tox=Count('tbls1processchemicals__tbls2toxicsworstcase__ProcessChemicalID'),
            num_worst_flam=Count('tbls1processchemicals__tbls4flammablesworstcase'),
            num_alt_tox=Count('tbls1processchemicals__tbls3toxicsaltreleases__ProcessChemicalID'),
            num_alt_flam=Count('tbls1processchemicals__tbls5flammablesaltreleases'),
            flam_tot=Sum(
                Case(
                    When(
                        tbls1processchemicals__ChemicalID__ChemType='F',
                        then=(Cast('tbls1processchemicals__Quantity', CopyFromBigIntegerField()))
                    ),
                    default=Value(0)
                )
            ),
            toxic_tot=Sum(
                Case(
                    When(
                        tbls1processchemicals__ChemicalID__ChemType='T',
                        then=(Cast('tbls1processchemicals__Quantity', CopyFromBigIntegerField()))
                    ),
                    default=Value(0)
                )
            ),
            quantity_tot=F('flam_tot') + F('toxic_tot'),
        )
        return qs

class ProcChem(BaseRMPModel):
    procchem_id = CopyFromBigIntegerField(
        primary_key=True,
        source_column='procchem_id',
    )
    process = CopyFromForeignKey(
        'Process',
        on_delete=models.PROTECT,
    )
    chemical = CopyFromForeignKey(
        'ChemCd',
        on_delete=models.PROTECT,
    )
    quantity_lbs = CopyFromBigIntegerField(
        null=True,
        verbose_name='1.17.c.3 Quantity',
        help_text='The maximum inventory quantity of the regulated substance '
                  'or mixture in the process in pounds.',
    )
    cbi_flag = CopyFromBooleanField()
    num_alt_flam = CopyFromBigIntegerField()
    num_alt_tox = CopyFromBigIntegerField()
    num_prevent_2_chem = CopyFromBigIntegerField()
    num_prevent_3_chem = CopyFromBigIntegerField()
    num_proc_flam = CopyFromBigIntegerField()
    num_worst_flam = CopyFromBigIntegerField()
    num_worst_tox = CopyFromBigIntegerField()
    cas = CopyFromCharField(
        max_length=9,
        verbose_name='CAS number',
        help_text='The identifying CAS number for a chemical.',
    )
    chemical_type = CopyFromCharField(max_length=1)

    @classmethod
    def get_transform_queryset(self):
        qs = raw_models.tblS1ProcessChemicals.objects.select_related(
            'ChemicalID'
        ).annotate(
            procchem_id=F('ProcessChemicalID'),
            process_id=F('ProcessID'),
            chemical_id=F('ChemicalID'),
            quantity_lbs=Cast('Quantity', CopyFromBigIntegerField()),
            cbi_flag=F('CBI_Flag'),
            num_alt_flam=Count('tbls5flammablesaltreleases'),
            num_alt_tox=Count('tbls3toxicsaltreleases'),
            num_prevent_2_chem=Count('tbls8_prevention_program_chemicals'),
            num_prevent_3_chem=Count('tbls7_prevention_program_chemicals'),
            num_proc_flam=Count('tbls1flammablemixturechemicals'),
            num_worst_flam=Count('tbls4flammablesworstcase'),
            num_worst_tox=Count('tbls2toxicsworstcase'),
            cas=F('ChemicalID__CASNumber'),
            chemical_type=F('ChemicalID__ChemType'),
        )
        return qs


class ProcFlam(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='FlamMixChemID',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.PROTECT,
        source_column="ProcessChemicalID",
    )
    chemical = CopyFromForeignKey(
        'ChemCd',
        on_delete=models.PROTECT,
        source_column="ChemicalID",
    )

    @classmethod
    def get_transform_queryset(self):
        m = raw_models.tblS1FlammableMixtureChemicals

        return m.objects.get_default_transform_queryset()
