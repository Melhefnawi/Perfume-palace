from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.add_comment, name='add_comment'),
    path('contact/contact_us', views.contact_us, name='contact_us'),
    path('review/create/', views.create_review, name='create_review'),
    path('show_review/show_rev/', views.show_review, name='show_review'),
    path('show_review/rev_details/<int:product_id>/', views.review_details, name='review_details'),
   
]