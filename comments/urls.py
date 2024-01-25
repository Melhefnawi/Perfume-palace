from . import views
from django.urls import path

urlpatterns = [
    path('add_comments/', views.add_comment, name='add_comments'),
]