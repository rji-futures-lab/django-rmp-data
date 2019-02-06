"""Function to create processed data files from raw models."""
import os
from django.conf import settings
from django.db.models import F, Max, OuterRef, Subquery
from rmp.models import tblFacility, tblS1Facilities, tblExecutiveSummaries


def transform_executive_summaries():
    latest_exec_sums = Subquery(
        tblExecutiveSummaries.objects.filter(
            facilityid=OuterRef('facilityid'),
        ).values('facilityid').annotate(
            max_seqnum=Max('esseqnum')
        ).values('max_seqnum')[:1]
    )

    qs = tblExecutiveSummaries.objects.filter(esseqnum=latest_exec_sums).annotate(
        rmp_id=F('facilityid_id'),
        execsum=F('summarytext')
    )

    file_path = os.path.join(settings.RMP_PROCESSED_DATA_DIR, 'rmp_execsum.csv')

    return qs.to_csv(file_path, 'rmp_id', 'execsum', header=True)


# def transform_facilities():
#     qs = tblFacility.objects.
#     file_path = os.path.join(settings.RMP_PROCESSED_DATA_DIR, 'rmp_facility.csv')

#     return qs.to_csv(file_path, header=True)


# def tranform_registrations():
#     qs = tblS1Facilities.objects.
#     file_path = os.path.join(settings.RMP_PROCESSED_DATA_DIR, 'rmp_registration.csv')

#     return qs.to_csv(file_path, header=True)
