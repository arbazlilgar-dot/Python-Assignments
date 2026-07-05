# Section C - Question 4: Clean URL Routing for List, Create, and Export views.
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_profiles, name='list_profiles'),
    path('create/', views.create_profile, name='create_profile'),
    path('export/', views.export_profiles_csv, name='export_profiles_csv'),
    path('', views.list_profiles, name='home'),
]
