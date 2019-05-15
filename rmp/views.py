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

class index(TemplateView):
    template_name = 'rmp/index.html'

class contact(TemplateView):
    template_name = 'rmp/contact.html'

class about(TemplateView):
    template_name = 'rmp/about.html'

class databases(TemplateView):
    template_name = 'rmp/databases.html'

class rmp(TemplateView):
    template_name = 'rmp/rmp.html'

class tri(TemplateView):
    template_name = 'rmp/tri.html'

class nrc(TemplateView):
    template_name = 'rmp/nrc.html'

class rcris(TemplateView):
    template_name = 'rmp/rcris.html'

class brs(TemplateView):
    template_name = 'rmp/brs.html'

class accident(TemplateView):
    template_name = 'rmp/accident_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        facility_list = Facility.objects.filter(
            registered=True
        ).order_by('-num_deaths')[:20]

        evacuated_list = Facility.objects.filter(
            registered=True
        ).order_by('-num_evacuated')[:20]

        prop_damage_list = Facility.objects.filter(
            registered=True
        ).order_by('-property_damage')[:20]

        context['facility_list'] = facility_list
        context['evacuated_list'] = evacuated_list
        context['prop_damage_list'] = prop_damage_list
        return context

class state_accidents(TemplateView):
    template_name = 'rmp/state_accidents.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state_list = StateCounts.objects.all()
        context['state_list'] = state_list
        return context

class facility_search(TemplateView):
    template_name = 'rmp/facility_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state_list = StateCd.objects.all()
        context['state_list'] = state_list
        return context

class location_search(TemplateView):
    template_name = 'rmp/location_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state_list = StateCd.objects.all()
        context['state_list'] = state_list
        return context

class chemical_search(TemplateView):
    template_name = 'rmp/chemical_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chemical_list = ChemCd.objects.all()
        context['chemical_list'] = chemical_list
        return context

class chemicalListView(ListView):
    template_name = 'rmp/chemical_results.html'
    queryset = ProcChem.objects.all()
    context_object_name = 'facility_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'chemical' in self.request.GET:
            chemical_query = self.request.GET['chemical']
            context['chemical_query'] = chemical_query
        else:
            context['error'] = True
        return context

    def get_queryset(self):
        chemical_query = self.request.GET.get('chemical')
        queryset = super(chemicalListView, self).get_queryset()
        if chemical_query:
            queryset = queryset.filter(chemical_name__search=chemical_query).select_related(
                'process',
            ).order_by(
                'process__facility_id', '-process__rmp_receipt_date'
            ).distinct(
                'process__facility_id'
            )
        return queryset

class locationListView(ListView):
    template_name = 'rmp/facility_by_location.html'
    queryset = Facility.objects.all()
    context_object_name = 'facility_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'state' in self.request.GET and not 'city' in self.request.GET:
            state_query = self.request.GET['state']
            context['state_query'] = state_query
        elif 'state' in self.request.GET and 'city' in self.request.GET:
            state_query = self.request.GET['state']
            city_query = self.request.GET['city']
            context['state_query']=state_query
            context['city_query']=city_query
        else:
            context['error'] = True

        return context

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

class facilityListView(ListView):
    template_name = "rmp/facility_list"
    queryset = Facility.objects.all()
    context_object_name = 'facility_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'facility' in self.request.GET and not 'parent_company' in self.request.GET:
            facility_query = self.request.GET['facility']
            context['facility_query'] = facility_query
        elif 'parent_company' in self.request.GET and not 'facility' in self.request.GET:
            pc_query = self.request.GET['parent_company']
            context['pc_query'] = pc_query
        elif 'parent_company' in self.request.GET and 'facility' in self.request.GET:
            facility_query = self.request.GET['facility']
            pc_query = self.request.GET['parent_company']
            context['pc_query'] = pc_query
            context['facility_query'] = facility_query
        else:
            context['error'] = True
        return context

    def get_queryset(self):
        facility_query = self.request.GET.get('facility')
        pc_query = self.request.GET.get('parent_company')
        queryset = super(facilityListView, self).get_queryset()
        if facility_query and not pc_query:
            queryset = queryset.filter(facility_name__search=facility_query)
        elif pc_query and not facilityP_query:
            queryset = queryset.filter(parent__search=pc_query)
        elif facility_query and pc_query:
            queryset = queryset.filter(facility_name__search=facility_query).filter(parent__search=pc_query)
        return queryset

class FacilityDetail(DetailView):
    """View a Facility's latest RMP"""
    model = Facility
