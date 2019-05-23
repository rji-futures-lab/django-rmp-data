from django.urls import path, re_path
from django.conf import urls
from . import views
from rmp.views import (
    locationListView,
    rmp,
    facilityListView,
    chemicalListView,
    accident,
    state_accidents,
    facility_search,
    location_search,
    chemical_search,
)

app_name = 'rmp'

urlpatterns = [
    path('', rmp.as_view(), name='rmp'),
    path('accident/', accident.as_view(), name='accident'),
    path('states/', state_accidents.as_view(), name='state_accidents'),
    path(
        'facility_search/',
        facility_search.as_view(),
        name='facility_search',
    ),
    path(
        'location_search/',
        location_search.as_view(),
        name='location_search',
    ),
    path(
        'chemical_search/',
        chemical_search.as_view(),
        name='chemical_search',
    ),
    path(
        'chemical_search/search_by_chemical/',
        chemicalListView.as_view(),
        name='search_by_chemical',
    ),
    path(
        'location_search/search_by_location/',
        locationListView.as_view(),
        name="search_by_location",
    ),
    # re_path(
    #     r'^location_search/search_by_location/$',
    #     locationListView.as_view(),
    #     name="search_by_location"
    # ),
    # path(
    #     'location_search/search_by_city/',
    #     views.search_by_city,
    #     name="search_by_city",
    # ),
    path(
        'facility_search/search_by_facility/',
        facilityListView.as_view(),
        name="search_by_facility",
    ),
    path(
        'facility/<int:pk>',
        views.FacilityDetail.as_view(),
        name="facility_detail",
    ),
]
