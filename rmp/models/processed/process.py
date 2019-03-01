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
    rmp = CopyFromForeignKey(
        'Registration',
        on_delete=models.PROTECT,
    )
    program_level = CopyFromIntegerField()
    cbi_flag = CopyFromBooleanField()
    num_proc_chem = CopyFromIntegerField(null=True)
    num_proc_naics = CopyFromIntegerField(null=True)
    # num_worst_tox = CopyFromIntegerField(null=True)
    # num_worst_flam = CopyFromIntegerField(null=True)
    # num_alt_tox = CopyFromIntegerField(null=True)
    # num_alt_flam = CopyFromIntegerField(null=True)
    # # num_prev_2 = CopyFromIntegerField()
    # # num_prev_3 = CopyFromIntegerField()
    # toxic_tot = CopyFromBigIntegerField(null=True)
    # flam_tot = CopyFromBigIntegerField(null=True)
    # quantity_tot = CopyFromBigIntegerField(null=True)
    # chemical_type = CopyFromCharField(max_length=1, null=True)

    @classmethod
    def get_transform_queryset(self):

        procchem_id = raw_models.tblS1Processes.objects.values('ProcessID')

        qs = raw_models.tblS1Processes.objects.annotate(
                num_proc_chem=Subquery(
                    raw_models.tblS1ProcessChemicals.objects.filter(
                        ProcessID=OuterRef('ProcessID')
                    ).values('ProcessID').annotate(
                        num_proc_chem=Count('ProcessID')
                    ).values('num_proc_chem')
                ),
                num_proc_naics=Subquery(
                    raw_models.tblS1Process_NAICS.objects.filter(
                        ProcessID=OuterRef('ProcessID')
                    ).values('ProcessID').annotate(
                        num_proc_naics=Count('ProcessID')
                    ).values('num_proc_naics')
                ),
                # num_worst_tox = processed_models.ProcChem.objects.process_set.all()

                # num_worst_tox=Subquery(
                #     processed_models.ProcChem.objects.filter(
                #         process_id=OuterRef('ProcessID')
                #     ).values('process_id').annotate(
                #         num_worst_tox=num_worst_tox
                #     ).values('num_worst_tox')
                # ),

                # num_worst_flam=Subquery(
                #     processed_models.ProcChem.objects.filter(
                #         process_id=OuterRef('ProcessID')
                #     ).values('process_id').annotate(
                #         num_worst_flam=F('num_worst_flam')
                #     ).values('num_worst_flam')
                # ),
                # num_alt_tox=Subquery(
                #     processed_models.ProcChem.objects.filter(
                #         process_id=OuterRef('ProcessID')
                #     ).values('process_id').annotate(
                #         num_alt_tox=F('num_alt_tox')
                #     ).values('num_alt_tox')
                # ),
                # num_alt_flam=Subquery(
                #     processed_models.ProcChem.objects.filter(
                #         process_id=OuterRef('ProcessID')
                #     ).values('process_id').annotate(
                #         num_alt_flam=F('num_alt_flam')
                #     ).values('num_alt_flam')
                # ),
                # flam_tot=Subquery(
                #     processed_models.ProcChem.objects.filter(
                #         process_id=OuterRef('ProcessID')
                #     ).values('process_id').filter(
                #         chemical_type='F',
                #     ).annotate(
                #         flam_tot=Sum('quantity_lbs')
                #     ).values('flam_tot'),
                #     output_field=CopyFromIntegerField(),
                # ),
                # toxic_tot=Subquery(
                #     processed_models.ProcChem.objects.filter(
                #         process_id=OuterRef('ProcessID')
                #     ).values('process_id').filter(
                #         chemical_type='T',
                #     ).annotate(
                #         toxic_tot=Sum('quantity_lbs')
                #     ).values('toxic_tot'),
                #     output_field=CopyFromIntegerField(),
                # ),
                # chemical_type=Subquery(
                #     processed_models.ProcChem.objects.filter(
                #         process_id=OuterRef('ProcessID')
                #     ).values('process_id').annotate(
                #         chemical_type=F('chemical_type')
                #     ).values('chemical_type')
                # ),
            ).annotate(
            process_id=F('ProcessID'),
            process_desc=F('AltID'),
            rmp_id=F('FacilityID'),
            program_level=F('ProgramLevel'),
            cbi_flag=F('CBI_Flag'),
            num_proc_chem=F('num_proc_chem'),
            num_proc_naics=F('num_proc_naics'),
            # num_worst_tox=F('num_worst_tox'),
            # num_worst_flam=F('num_worst_flam'),
            # num_alt_tox=F('num_alt_tox'),
            # num_alt_flam=F('num_alt_flam'),
            # flam_tot=F('flam_tot'),
            # toxic_tot=F('toxic_tot'),
            # quantity_tot=F('flam_tot') + F('toxic_tot'),
            # chemical_type=F('chemical_type'),
        )
        print(qs.query)
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
    quantity_lbs = CopyFromDecimalField(
        max_digits=28,
        decimal_places=16,
        null=True,
        verbose_name='1.17.c.3 Quantity',
        help_text='The maximum inventory quantity of the regulated substance '
                  'or mixture in the process in pounds.',
    )
    cbi_flag = CopyFromBooleanField()
    num_alt_flam = CopyFromBigIntegerField(null=True)
    num_alt_tox = CopyFromBigIntegerField(null=True)
    num_prevent_2_chem = CopyFromBigIntegerField(null=True)
    num_prevent_3_chem = CopyFromBigIntegerField(null=True)
    num_proc_flam = CopyFromBigIntegerField(null=True)
    num_worst_flam = CopyFromBigIntegerField(null=True)
    num_worst_tox = CopyFromBigIntegerField(null=True)
    cas = CopyFromCharField(
        max_length=9,
        verbose_name='CAS number',
        help_text='The identifying CAS number for a chemical.',
    )
    chemical_type = CopyFromCharField(max_length=1)

    source_file = 'rmp_proc_chem'

    @classmethod
    def get_transform_queryset(self):
        qs = raw_models.tblS1ProcessChemicals.objects.select_related('ChemicalID').annotate(
            procchem_id=F('ProcessChemicalID'),
            process_id=F('ProcessID'),
            chemical_id=F('ChemicalID'),
            quantity_lbs=F('Quantity'),
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

        # .annotate(
        #     num_alt_flam=Subquery(
        #         raw_models.tblS5FlammablesAltReleases.objects.filter(
        #             ProcessChemicalID=OuterRef('ProcessChemicalID')
        #         ).values('ProcessChemicalID').annotate(
        #             num_alt_flam=Count('FlammableID')
        #         ).values('num_alt_flam')
        #     ),
        #     num_alt_tox=Subquery(
        #         raw_models.tblS3ToxicsAltReleases.objects.filter(
        #             ProcessChemicalID=OuterRef('ProcessChemicalID')
        #         ).values('ProcessChemicalID').annotate(
        #             num_alt_tox=Count('ToxicID')
        #         ).values('num_alt_tox')
        #     ),
        #     num_proc_flam=Subquery(
        #         raw_models.tblS1FlammableMixtureChemicals.objects.filter(
        #             ProcessChemicalID=OuterRef('ProcessChemicalID')
        #         ).values('ProcessChemicalID').annotate(
        #             num_proc_flam=Count('FlamMixChemID')
        #         ).values('num_proc_flam')
        #     ),
        #     num_worst_flam=Subquery(
        #         raw_models.tblS4FlammablesWorstCase.objects.filter(
        #             ProcessChemicalID=OuterRef('ProcessChemicalID')
        #         ).values('ProcessChemicalID').annotate(
        #             num_worst_flam=Count('FlammableID')
        #         ).values('num_worst_flam')
        #     ),
        #     num_worst_tox=Subquery(
        #         raw_models.tblS2ToxicsWorstCase.objects.filter(
        #             ProcessChemicalID=OuterRef('ProcessChemicalID')
        #         ).values('ProcessChemicalID').annotate(
        #             num_worst_tox=Count('ToxicID')
        #         ).values('num_worst_tox')
        #     ),
        #     num_prevent_3_chem=Subquery(
        #         raw_models.tblS7_Prevention_Program_Chemicals.objects.filter(
        #             ProcessChemicalID=OuterRef('ProcessChemicalID')
        #         ).values('ProcessChemicalID').annotate(
        #             num_prevent_3_chem=Count('PrimaryKey')
        #         ).values('num_prevent_3_chem')
        #     ),
        #     num_prevent_2_chem=Subquery(
        #         raw_models.tblS8_Prevention_Program_Chemicals.objects.filter(
        #             ProcessChemicalID=OuterRef('ProcessChemicalID')
        #         ).values('ProcessChemicalID').annotate(
        #             num_prevent_2_chem=Count('PrimaryKey')
        #         ).values('num_prevent_2_chem')
        #     ),
        # )

        return qs


class ProcFlam(BaseRMPModel):
    id = CopyFromIntegerField(
        primary_key=True,
        source_column='flammixchem_id',
    )
    procchem = CopyFromForeignKey(
        'ProcChem',
        on_delete=models.PROTECT,
    )
    chemical = CopyFromForeignKey(
        'ChemCd',
        on_delete=models.PROTECT,
    )

    source_file = 'rmp_proc_flam'
