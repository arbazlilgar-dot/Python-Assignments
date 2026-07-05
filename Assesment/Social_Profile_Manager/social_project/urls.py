# Section C - Question 4: Clean URL Routing for List, Create, and Export views.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),
]
