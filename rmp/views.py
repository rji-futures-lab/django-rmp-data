from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count, Sum, F, Max, OuterRef, Subquery
from django.views.generic import TemplateView, ListView, DetailView
from rmp.models import (
    ExecutiveSummary,
    Facility,
    Registration,
    StateCd,
    StateCounts,
    Process,
    ProcChem,
    ChemCd,
    tblExecutiveSummaries,
    tblFacility,
    tblS1Facilities,
    tblS1FlammableMixtureChemicals,
    tblS1ProcessChemicals,
    tblS6AccidentChemicals,
    tblS6AccidentHistory,
)

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
    facility_list = Facility.objects.filter(
        registered=True
    ).order_by('-num_deaths')[:20]

    evacuated_list = Facility.objects.filter(
        registered=True
    ).order_by('-num_evacuated')[:20]

    prop_damage_list = Facility.objects.filter(
        registered=True
    ).order_by('-property_damage')[:20]

    context = dict(
        facility_list=facility_list,
        evacuated_list=evacuated_list,
        prop_damage_list=prop_damage_list,
    )

    return render(request, 'rmp/accident_list.html', context)

def state_accidents(request):
    state_list = StateCounts.objects.all()
    context = dict(state_list=state_list)
    return render(request, 'rmp/state_accidents.html', context)

def facility_search(request):
    state_list = Facility.objects.order_by('state').values('state').distinct()
    context = {'state_list': state_list}
    return render(request, 'rmp/facility_search.html', context)

def facility_detail(request, facility_id):
    facility_list = Facility.objects.filter(id=facility_id)
    return render(request, 'rmp/facility_results.html', {'facility_list': facility_list})

def location_search(request):
    state_list = StateCd.objects.all()
    context = dict(state_list=state_list)
    return render(request, 'rmp/location_search.html', context)

def chemical_search(request):
    chemical_list = ChemCd.objects.all()
    context = dict(chemical_list=chemical_list)
    return render(request, 'rmp/chemical_search.html', context)

def search_by_chemical(request):
    if 'chemical' in request.GET:
        chemical = request.GET['chemical']
        facility_list = ProcChem.objects.filter(chemical_name__search=chemical).select_related('process').values(
            'process__facility_id'
        ).annotate(
            id = F('process__facility_id'),
            chemical_name = F('chemical_name'),
            quantity_total = Sum('quantity_lbs'),
        )
        response = render(
            request,
            'rmp/chemical_results.html',
            dict(
                facility_list=facility_list,
                chemical_query = chemical,
            )
        )

    return response

# def search_by_state(request):
#     if 'state' in request.GET:
#         state_query = request.GET['state']
#         facility_list = Facility.objects.filter(
#             state=state_query
#         )
#         response = render(
#             request,
#             'rmp/location_results.html',
#             dict(
#                 facility_list=facility_list,
#                 state_query=state_query,
#             )
#         )
#     else:
#         response = render(
#             request,
#             'rmp/location_search.html',
#             dict(error=True),
#         )
#
#     return response

class locationListView(ListView):
    template_name = 'rmp/facility_by_location.html'
    queryset = Facility.objects.all()
    context_object_name = 'facility_list'

    # def get_context_data(self, **kwargs):
    #     if 'state' in self.request.GET and not 'city' in self.request.GET:
    #         state_query = self.request.GET['state']
    #         context = dict(
    #                 state_query=state_query,
    #         )
    #     elif 'state' in self.request.GET and 'city' in self.request.GET:
    #         state_query = self.request.GET['state']
    #         city_query = self.request.GET['city']
    #         context=dict(
    #             state_query=state_query,
    #             city_query=city_query
    #         )
    #
    #     else:
    #         context = dict(error=True)
    #
    #     return context

    def get_queryset(self):
        state_query = self.request.GET.get('state')
        city_query = self.request.GET.get('city')
        county_query = self.request.GET.get('county')
        queryset = super(locationListView, self).get_queryset()
        if state_query and not city_query and not county_query:
            queryset = queryset.filter(state=state_query)
        elif state_query and city_query and not county_query:
            queryset = queryset.filter(state=state_query).filter(city=city_query)
        elif state_query and county_query and not city_query:
            queryset = queryset.filter(state=state_query).filter(county_name__search=county_query)
        elif state_query and county_query and city_query:
            queryset = queryset.filter(state=state_query).filter(county_name__search=county_query).filter(city=city_query)
        return queryset


# def search_by_city(request):
#     if (
#         'state' in request.GET and
#         'city' in request.GET
#     ):
#
#         if not state_query and not city_query:
#             response = render(
#                 request,
#                 'rmp/location_search.html',
#                 dict(error=True),
#             )
#         elif state_query and city_query:
#             facility_list = Facility.objects.filter(
#                 state=state_query
#             ).filter(
#                 city=city_query
#             )
#             response = render(
#                 request,
#                 'rmp/location_results.html',
#
#             )
#     else:
#         response = render(
#             request,
#             'rmp/location_search.html',
#             dict(error=True),
#         )
#     return response

def search_by_facility(request):
    error=False
    if 'facility' in request.GET and 'parent_company' in request.GET and 'city' in request.GET and 'state' in request.GET:
        facility_query = request.GET['facility']
        pc_query = request.GET['parent_company']
        state_query = request.GET['state']
        city_query = request.GET['city']
        if not facility_query and not pc_query and not state_query and not city_query:
            error=True
        elif facility_query and pc_query and state_query and city_query:
            facility_list = Facility.objects.filter(
                facility_name__search=facility_query
            ).filter(
                parent__search=pc_query
            ).filter(
                city__search=city_query
            ).filter(
                state=state_query
            ).select_related('facility').select_related(
                'execsum_rmp'
            ).select_related('rmp').latest('receipt_date')
            context = {'facility_list': facility_list, 'facility_query': facility_query, 'pc_query': pc_query}
            return render(request, 'rmp/facility_results.html', context)

        elif facility_query and state_query and city_query:
            facility_list = Facility.objects.filter(
                facility_name__search=facility_query
            ).filter(
                city__search=city_query
            ).filter(
                state=state_query
            ).select_related('execsum_rmp').select_related('rmp')
            context = {'facility_list': facility_list, 'facility_query': facility_query}
            return render(request, 'rmp/facility_results.html', context)

        elif len(pc_query) != 0:
            pc_list = Facility.objects.filter(parent__search=pc_query).select_related('execsum_rmp').select_related('rmp')
            context = {'pc_list': pc_list, 'pc_query': pc_query}
            return render(request, 'rmp/facility_results.html', context)

    return render(request, 'rmp/facility_search.html', {'error': error})
