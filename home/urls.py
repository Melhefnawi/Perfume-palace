
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('company/', views.company, name='company'),
    path('help/', views.help, name='help'),    
]


