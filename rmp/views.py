from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from models.processed import processed

class state_accidents(ListView):
    
