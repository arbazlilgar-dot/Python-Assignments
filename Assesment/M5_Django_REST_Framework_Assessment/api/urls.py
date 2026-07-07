"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api
Application: api

URL Configuration
====================================================

This module defines all API URL patterns:
- DefaultRouter for OrderViewSet (Question 3)
- Manual URL patterns for Category, MenuItem, Geocode, Registration

Assessment Concepts Covered:
- Question 3: DefaultRouter
  Automatically generates CRUD URLs for OrderViewSet.
- Question 3: URL routing for all API endpoints
====================================================
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


# ====================================================
# QUESTION 3 - DEFAULT ROUTER
# ====================================================
# DefaultRouter automatically generates URL patterns for ViewSets.
# For OrderViewSet, it generates:
#   GET    /api/orders/       → list
#   POST   /api/orders/       → create
#   GET    /api/orders/<pk>/  → retrieve
#   PUT    /api/orders/<pk>/  → update
#   PATCH  /api/orders/<pk>/  → partial_update
#   DELETE /api/orders/<pk>/  → destroy
#   GET    /api/orders/       → API root (browsable)

router = DefaultRouter()

# Register OrderViewSet with DefaultRouter
# Question 3 - ModelViewSet + DefaultRouter
router.register(r'orders', views.OrderViewSet, basename='order')


# ====================================================
# URL PATTERNS
# ====================================================
# Combines router-generated URLs with manual URL patterns.

urlpatterns = [
    # ================================================
    # SECTION B - TASK 1: CATEGORY ENDPOINTS
    # ================================================
    # Question 3 - ListAPIView
    # GET  /api/categories/     → List all categories (HTTP 200)
    # POST /api/categories/     → Create category (HTTP 201)
    path(
        'categories/',
        views.CategoryListView.as_view(),
        name='category-list'
    ),

    # Question 3 - APIView
    # GET    /api/categories/<id>/ → Retrieve category (HTTP 200)
    # PUT    /api/categories/<id>/ → Update category (HTTP 200)
    # DELETE /api/categories/<id>/ → Delete category (HTTP 204)
    path(
        'categories/<int:pk>/',
        views.CategoryDetailView.as_view(),
        name='category-detail'
    ),

    # ================================================
    # SECTION B - TASK 2: MENUITEM ENDPOINTS
    # ================================================
    # Question 3 - GenericAPIView
    # GET  /api/menu-items/     → List all menu items (HTTP 200)
    # POST /api/menu-items/     → Create menu item (HTTP 201)
    path(
        'menu-items/',
        views.MenuItemListCreateView.as_view(),
        name='menuitem-list'
    ),

    # GET    /api/menu-items/<id>/ → Retrieve (HTTP 200)
    # PUT    /api/menu-items/<id>/ → Full update (HTTP 200)
    # PATCH  /api/menu-items/<id>/ → Partial update (HTTP 200)
    # DELETE /api/menu-items/<id>/ → Delete (HTTP 204)
    path(
        'menu-items/<int:pk>/',
        views.MenuItemDetailView.as_view(),
        name='menuitem-detail'
    ),

    # ================================================
    # SECTION A - QUESTION 6: GEOCODE ENDPOINT
    # ================================================
    # POST /api/geocode/ → Geocode address to coordinates
    path(
        'geocode/',
        views.GeocodeView.as_view(),
        name='geocode'
    ),

    # ================================================
    # USER REGISTRATION ENDPOINT
    # ================================================
    # POST /api/register/ → Register a new user
    path(
        'register/',
        views.UserRegistrationView.as_view(),
        name='register'
    ),

    # ================================================
    # API DASHBOARD ENDPOINT
    # ================================================
    # GET /api/dashboard/ → API statistics (JSON)
    path(
        'dashboard/',
        views.DashboardView.as_view(),
        name='api-dashboard'
    ),

    # ================================================
    # HTML DASHBOARD (Premium UI)
    # ================================================
    path(
        '',
        views.dashboard_page,
        name='dashboard-page'
    ),

    # ================================================
    # CURRENT USER ENDPOINT
    # ================================================
    path(
        'me/',
        views.CurrentUserView.as_view(),
        name='current-user'
    ),

    # ================================================
    # SECTION B - TASK 3: ORDER ENDPOINTS (DefaultRouter)
    # ================================================
    # Question 3 - DefaultRouter
    # Automatically includes all OrderViewSet URLs
    path('', include(router.urls)),
]
