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
from rmp.models import processed as processed_models
from rmp.models.base import BaseRMPModel


class Process(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='process_id',
    )
    process_desc = CopyFromCharField(max_length=25, blank=True)
    rmp_id = CopyFromIntegerField()
    program_level = CopyFromIntegerField()
    cbi_flag = CopyFromBooleanField()

    # TODO AGGREGATE
    num_proc_chem = CopyFromIntegerField()
    num_proc_naics = CopyFromIntegerField()
    num_chem_real = CopyFromIntegerField()
    num_chem_fake = CopyFromIntegerField()
    num_worst_tox = CopyFromIntegerField()
    num_worst_flam = CopyFromIntegerField()
    num_alt_tox = CopyFromIntegerField()
    num_alt_flam = CopyFromIntegerField()
    num_prev_2 = CopyFromIntegerField()
    num_prev_3 = CopyFromIntegerField()
    toxic_tot = CopyFromBigIntegerField()
    flam_tot = CopyFromBigIntegerField()
    quantity_tot = CopyFromBigIntegerField()
    # while these fields are listed in rmp_fields.csv, they do not appear in
    # rmp_process.tsv ¯\_(ツ)_/¯
    # chem_tox_yn = CopyFromBooleanField()
    # chem_flam_yn = CopyFromBooleanField()

    source_file = 'rmp_process'


class ProcChem(BaseRMPModel):
    procchem_id = CopyFromBigIntegerField(
        primary_key=True,
        source_column='procchem_id',
    )
    process = CopyFromForeignKey(
        'Process',
        on_delete=models.CASCADE
    )
    chemical = CopyFromForeignKey(
        'ChemCd',
        on_delete=models.CASCADE
    )
    quantity_lbs = CopyFromBigIntegerField()
    cbi_flag = CopyFromBooleanField()
    num_alt_flam = CopyFromBigIntegerField()
    num_alt_tox = CopyFromBigIntegerField()
    num_prevent_2_chem = CopyFromBigIntegerField()
    num_prevent_3_chem = CopyFromBigIntegerField()
    num_proc_flam = CopyFromBigIntegerField()
    num_worst_flam = CopyFromBigIntegerField()
    num_worst_tox = CopyFromBigIntegerField()
    cas = CopyFromBigIntegerField()
    chemical_type = CopyFromCharField(max_length=1)

    source_file = 'rmp_proc_chem'

    @classmethod
    def get_transform_queryset(self):
        qs = raw_models.tblS1ProcessChemicals.objects.select_related('ChemicalID').annotate(
            num_alt_flam=Subquery(
                raw_models.tblS5FlammablesAltReleases.objects.filter(
                    ProcessChemicalID=OuterRef('ProcessChemicalID')
                ).values('ProcessChemicalID').annotate(
                    num_alt_flam=Count('FlammableID')
                ).values('num_alt_flam')
            ),
            num_alt_tox=Subquery(
                raw_models.tblS3ToxicsAltReleases.objects.filter(
                    ProcessChemicalID=OuterRef('ProcessChemicalID')
                ).values('ProcessChemicalID').annotate(
                    num_alt_tox=Count('ToxicID')
                ).values('num_alt_tox')
            ),
            num_proc_flam=Subquery(
                raw_models.tblS1FlammableMixtureChemicals.objects.filter(
                    ProcessChemicalID=OuterRef('ProcessChemicalID')
                ).values('ProcessChemicalID').annotate(
                    num_proc_flam=Count('FlamMixChemID')
                ).values('num_proc_flam')
            ),
            num_worst_flam=Subquery(
                raw_models.tblS4FlammablesWorstCase.objects.filter(
                    ProcessChemicalID=OuterRef('ProcessChemicalID')
                ).values('ProcessChemicalID').annotate(
                    num_worst_flam=Count('FlammableID')
                ).values('num_worst_flam')
            ),
            num_worst_tox=Subquery(
                raw_models.tblS2ToxicsWorstCase.objects.filter(
                    ProcessChemicalID=OuterRef('ProcessChemicalID')
                ).values('ProcessChemicalID').annotate(
                    num_worst_tox=Count('ToxicID')
                ).values('num_worst_tox')
            ),
            num_prevent_3_chem=Subquery(
                raw_models.tblS7_Prevention_Program_Chemicals.objects.filter(
                    ProcessChemicalID=OuterRef('ProcessChemicalID')
                ).values('ProcessChemicalID').annotate(
                    num_prevent_3_chem=Count('PrimaryKey')
                ).values('num_prevent_3_chem')
            ),
            num_prevent_2_chem=Subquery(
                raw_models.tblS8_Prevention_Program_Chemicals.objects.filter(
                    ProcessChemicalID=OuterRef('ProcessChemicalID')
                ).values('ProcessChemicalID').annotate(
                    num_prevent_2_chem=Count('PrimaryKey')
                ).values('num_prevent_2_chem')
            ),
        ).annotate(
            procchem_id=F('ProcessChemicalID'),
            process_id=F('ProcessID'),
            chemical_id=F('ChemicalID'),
            quantity_lbs=F('Quantity'),
            cbi_flag=F('CBI_Flag'),
            num_alt_flam=F('num_alt_flam'),
            num_alt_tox=F('num_alt_tox'),
            num_prevent_2_chem=F('num_prevent_2_chem'),
            num_prevent_3_chem=F('num_prevent_3_chem'),
            num_proc_flam=F('num_proc_flam'),
            num_worst_flam=F('num_worst_flam'),
            num_worst_tox=F('num_worst_tox'),
            cas=F('ChemicalID__CASNumber'),
            chemical_type=F('ChemicalID__ChemType'),
        )

        return qs


class ProcFlam(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='flammixchem_id',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.CASCADE
    )
    chemical = CopyFromForeignKey(
        'ChemCd',
        on_delete=models.CASCADE
    )

    source_file = 'rmp_proc_flam'
