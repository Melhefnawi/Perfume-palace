from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.add_comment, name='add_comment'),
]