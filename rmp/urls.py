from django.urls import path
from django.conf import urls
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accident/', views.accident, name='accident'),
    path('states/', views.state_accidents, name='state_accidents')
]
