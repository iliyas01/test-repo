from django import views
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from . import views



urlpatterns = [
    #path('',views.home,name='home'),
    path('',TemplateView.as_view(template_name='dash/main.html')),
    #path('dashboard',views.dashboard,name='dashboard'),
    
    
    
]
