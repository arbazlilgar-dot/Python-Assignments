"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api

Root URL Configuration
====================================================

This file routes all URL patterns for the project:
- /admin/          → Django Admin Interface
- /api/            → Food Delivery API endpoints (all tasks)
- /api-token-auth/ → Token Authentication endpoint (Question 6)
- /                → API Dashboard (Premium UI)

Assessment Concepts:
- Question 3: URL routing with DefaultRouter
- Question 6: Token Authentication endpoint
====================================================
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Question 6 - Token Authentication
# This view handles POST requests with username/password
# and returns an authentication token
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # Django Admin Interface
    path('admin/', admin.site.urls),

    # Question 6 - Token Authentication Endpoint
    # POST /api-token-auth/ with {"username": "...", "password": "..."}
    # Returns {"token": "..."} for authenticated requests
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),

    # API Endpoints - All assessment tasks
    # Includes Category, MenuItem, Order, Geocode, Registration endpoints
    path('api/', include('api.urls')),

    # Frontend UI Pages
    path('', include('frontend.urls')),

    # DRF Browsable API Login/Logout (for browser-based testing)
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
