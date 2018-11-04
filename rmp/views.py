from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count, Sum
from rmp.models.processed.processed import Facility

def index(request):
    return render(request, 'rmp/index.html')

def accident(request):
    facility_list = Facility.objects.filter(deregistration_yn='n').order_by('-num_deaths')[:50]
    context = {'facility_list': facility_list}
    return render(request, 'rmp/accident_list.html', context)

def state_accidents(request):
    state_list = Facility.objects.values('state') \
                         .filter(deregistration_yn='n') \
                         .annotate(count=Count('id'k)) \
                         .annotate(num_accidents=Sum('num_accident')) \
                         .annotate(num_deaths=Sum('num_deaths')) \
                         .annotate(num_injuries=Sum('num_injuries')) \
                         .annotate(num_evacuated=Sum('num_evacuated')) \
                         .annotate(property_damage=Sum('property_damage')) \
                         .order_by('state')
    context = {'state_list': state_list}
    return render(request, 'rmp/state_accidents.html', context)
