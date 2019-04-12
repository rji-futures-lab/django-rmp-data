from django.urls import path
from django.conf import urls
from . import views

urlpatterns = [
    path('', views.rmp, name='rmp'),
    path('accident/', views.accident, name='accident'),
    path('states/', views.state_accidents, name='state_accidents'),
    path(
        'facility_search/',
        views.facility_search,
        name='facility_search',
    ),
    path(
        'location_search/',
        views.location_search,
        name='location_search',
    ),
    path(
        'location_search/search_by_state/',
        views.search_by_state,
        name="search_by_state",
    ),
    path(
        'location_search/search_by_city/',
        views.search_by_city,
        name="search_by_city",
    ),
    path(
        'facility_search/search_by_facility/',
        views.search_by_facility,
        name="search_by_facility",
    ),
]
