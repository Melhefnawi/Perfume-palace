from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.add_comment, name='add_comment'),
    path('review_detail/<int:pk>', views.review_detail, name='review_detail'),
    path('review/create/', views.create_review, name='create_review'),
   
]