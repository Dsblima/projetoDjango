from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.homePage),
    # path('lista',views.listaProcessos),
    
    # path('^$',TemplateView.as_view(template_name='index.html'))
]   