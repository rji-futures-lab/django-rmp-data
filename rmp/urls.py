from django.urls import path, re_path
from django.conf import urls
from . import views
from rmp.views import locationListView

app_name = 'rmp'

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
        'chemical_search/',
        views.chemical_search,
        name='chemical_search',
    ),
    path(
        'chemical_search/search_by_chemical/',
        views.search_by_chemical,
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
        views.search_by_facility,
        name="search_by_facility",
    ),
    path(
        'facility_search/<int:facility_id>',
        views.facility_detail,
        name="facility_detail",
    ),
]
