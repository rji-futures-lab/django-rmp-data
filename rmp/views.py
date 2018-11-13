from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count, Sum
from rmp.models.processed.processed import Facility
# from .forms import facility_search

def index(request):
    return render(request, 'rmp/index.html')

def rmp(request):
    return render(request, 'rmp/rmp.html')

def accident(request):
    facility_list = Facility.objects.filter(deregistration_yn='n').order_by('-num_deaths')[:20]
    evacuated_list = Facility.objects.filter(deregistration_yn='n').order_by('-num_evacuated')[:20]
    prop_damage_list = Facility.objects.filter(deregistration_yn='n').order_by('-property_damage')[:20]
    context = {'facility_list': facility_list, 'evacuated_list': evacuated_list, 'prop_damage_list': prop_damage_list}
    return render(request, 'rmp/accident_list.html', context)

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
    # if request.method == 'GET':
    #     form = facility_search(request.GET)
    #     if form.is_valid():
    #         pass
    # else:
    #     form = ContactForm()
    # return render(request, 'rmp/facility_search', {'form': form})

def location_search(request):
    state_list = Facility.objects.order_by('state').values('state').distinct()
    context = {'state_list': state_list}
    return render(request, 'rmp/location_search.html', context)

def search_by_location(request):
    error=False
    if 'state' in request.GET:
        state_query = request.GET['state']
        facility_list = Facility.objects.filter(state__search=state_query)
        return render(request, 'rmp/location_results.html', {'facility_list': facility_list, 'state_query': state_query})


    return render(request, 'rmp/location_search.html', {'error': error})

def search_by_facility(request):
    error=False
    if 'facility' in request.GET and 'parent_company' in request.GET:
        facility_query = request.GET['facility']
        pc_query = request.GET['parent_company']
        if not facility_query and not pc_query:
            error=True
        elif facility_query and pc_query:
            facility_list = Facility.objects.filter(facility_name__search=facility_query).filter(parent__search=pc_query)
            return render(request, 'rmp/facility_results.html', {'facility_query': facility_query, 'pc_query': pc_query, 'facility_list': facility_list})

        elif len(facility_query) != 0:
            facility_query = request.GET['facility']
            facility_list = Facility.objects.filter(facility_name__search=facility_query)
            return render(request, 'rmp/facility_results.html', {'facility_list': facility_list, 'facility_query': facility_query})

        elif len(pc_query) != 0:
            pc_query = request.GET['parent_company']
            facility_list = Facility.objects.filter(parent__search=pc_query)
            return render(request, 'rmp/facility_results.html', {'facility_list': facility_list, 'pc_query': pc_query})

    return render(request, 'rmp/facility_search.html', {'error': error})
