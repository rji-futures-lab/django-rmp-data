from django.urls import path
from django.conf import urls
from . import views

urlpatterns = [
    path('', views.rmp, name='rmp'),
    path('accident/', views.accident, name='accident'),
    path('states/', views.state_accidents, name='state_accidents'),
    path('facility_search/', views.facility_search, name='facility_search'),
    path('location_search/', views.location_search, name='location_search'),
    path('location_search/search_by_location/', views.search_by_location, name="search_by_location"),
    path('facility_search/search_by_facility/', views.search_by_facility, name="search_by_facility"),
]
