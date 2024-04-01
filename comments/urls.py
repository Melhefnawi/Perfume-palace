from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.add_comment, name='add_comment'),
    path('contact/contact_us', views.contact_us, name='contact_us'),
    path('review/create/', views.create_review, name='create_review'),
   
]