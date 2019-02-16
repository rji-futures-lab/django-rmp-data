from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count, Sum, F, Max, OuterRef, Subquery
from rmp.models.processed.processed import Facility, ExecutiveSummary, Registration
from rmp.models.raw.tbl import tblFacility, tblExecutiveSummaries
from rmp.models.raw.tblS1 import tblS1Facilities, tblS1FlammableMixtureChemicals, tblS1ProcessChemicals
from rmp.models.raw.tblS6 import tblS6AccidentChemicals, tblS6AccidentHistory

# from .forms import facility_search

def index(request):
    return render(request, 'rmp/index.html')

def contact(request):
    return render(request, 'rmp/contact.html')

def about(request):
    return render(request, 'rmp/about.html')

def databases(request):
    return render(request, 'rmp/databases.html')

def rmp(request):
    return render(request, 'rmp/rmp.html')

def tri(request):
    return render(request, 'rmp/tri.html')

def nrc(request):
    return render(request, 'rmp/nrc.html')

def rcris(request):
    return render(request, 'rmp/rcris.html')

def brs(request):
    return render(request, 'rmp/brs.html')

def accident(request):
    facility_list = Facility.objects.filter(deregistration_yn='n').order_by('-num_deaths')[:20]
    evacuated_list = Facility.objects.filter(deregistration_yn='n').order_by('-num_evacuated')[:20]
    prop_damage_list = Facility.objects.filter(deregistration_yn='n').order_by('-property_damage')[:20]
    context = {'facility_list': facility_list, 'evacuated_list': evacuated_list, 'prop_damage_list': prop_damage_list}
    return render(request, 'rmp/accident_list.html', context)

def test(request):
    test = tblS1Facilities.objects.select_related('FacilityID')



    context = {'test': test}
    return render(request, 'rmp/test.html', context)

def state_accidents(request):
    state_list = Facility.objects.values('state') \
                         .filter(deregistration_yn='n') \
                         .annotate(count=Count('id')) \
                         .annotate(num_accidents=Sum('num_accident')) \
                         .annotate(num_deaths=Sum('num_deaths')) \
                         .annotate(num_injuries=Sum('num_injuries')) \
                         .annotate(num_evacuated=Sum('num_evacuated')) \
                         .annotate(property_damage=Sum('property_damage')) \
                         .order_by('state')
    context = {'state_list': state_list}
    return render(request, 'rmp/state_accidents.html', context)

def facility_search(request):
    return render(request, 'rmp/facility_search.html')

def location_search(request):
    state_list = Facility.objects.order_by('state').values('state').distinct()
    context = {'state_list': state_list}
    return render(request, 'rmp/location_search.html', context)

def search_by_state(request):
    error=False
    if 'state' in request.GET:
        state_query = request.GET['state']
        facility_list = Facility.objects.filter(state__search=state_query)
        return render(request, 'rmp/location_results.html', {'facility_list': facility_list, 'state_query': state_query})
    return render(request, 'rmp/location_search.html', {'error': error})

def search_by_city(request):
    error=False
    if 'state' in request.GET and 'city' in request.GET and 'zip' in request.GET:
        state_query = request.GET['state']
        city_query = request.GET['city']
        if not state_query and not city_query:
            error=True
        elif state_query and  city_query:
            facility_list = Facility.objects.filter(state__search=state_query).filter(city__search=city_query)
            return render(request, 'rmp/location_results.html', {'facility_list': facility_list, 'state_query': state_query, 'city_query': city_query})
    return render(request, 'rmp/location_search.html', {'error': error})

def search_by_facility(request):
    error=False
    if 'facility' in request.GET and 'parent_company' in request.GET:
        facility_query = request.GET['facility']
        pc_query = request.GET['parent_company']
        if not facility_query and not pc_query:
            error=True
        elif facility_query and pc_query:
            facility_list = Facility.objects.filter(facility_name__search=facility_query).filter(parent__search=pc_query).select_related('execsum_rmp').select_related('rmp')
            # registration = Registration.objects.filter(facility_name__search=facility_query).filter(parent__search=pc_query).order_by('-complete_check_dt')[:1] , 'execsum': execsum, 'registration': registration
            # execsum = Facility.objects.filter(facility_name__search=facility_query).filter(parent__search=pc_query).select_related('execsum_rmp')
            context = {'facility_list': facility_list, 'facility_query': facility_query, 'pc_query': pc_query}
            return render(request, 'rmp/facility_results.html', context)

        elif len(facility_query) != 0:
            facility_query = request.GET['facility']
            facility_list = Facility.objects.filter(facility_name__search=facility_query).select_related('execsum_rmp').select_related('rmp')
            # execsum = Facility.objects.filter(facility_name__search=facility_query).select_related('execsum_rmp')
            # facility_id = Facility.objects.filter(facility_name__search=facility_query).values_list('rmp', flat=True) , 'facility_id': facility_id})
            # registration = Registration.objects.filter(facility_name__search=facility_query).order_by('-complete_check_dt')[:1] , 'execsum': execsum, 'registration': registration
            return render(request, 'rmp/facility_results.html', {'facility_list': facility_list, 'facility_query': facility_query})

        elif len(pc_query) != 0:
            pc_query = request.GET['parent_company']
            facility_list = Facility.objects.filter(parent__search=pc_query).select_related('execsum_rmp').select_related('rmp')
            # registration = Registration.objects.filter(parent__search=pc_query).order_by('-complete_check_dt')[:1] , 'execsum': execsum, 'registration': registration
            # execsum = Facility.objects.filter(parent__search=pc_query).select_related('execsum_rmp')
            return render(request, 'rmp/facility_results.html', {'facility_list': facility_list, 'pc_query': pc_query})

    return render(request, 'rmp/facility_search.html', {'error': error})
