"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api
Application: api

Views
====================================================

This module defines all API views for the Food Delivery API:
- CategoryListView: List all categories (ListAPIView - Task 1)
- CategoryDetailView: Retrieve a single category (APIView - Section A)
- MenuItemListCreateView: List/Create menu items (GenericAPIView - Task 2)
- MenuItemDetailView: Retrieve/Update/Delete menu items (GenericAPIView - Task 2)
- OrderViewSet: Full CRUD for orders (ModelViewSet - Task 3)
- GeocodeView: Google Maps Geocoding (APIView - Section A Q6)
- UserRegistrationView: Register new users (APIView)
- DashboardView: Premium API dashboard

Assessment Concepts Covered:
- Question 1: REST Statelessness (all views are stateless)
- Question 3: APIView (CategoryDetailView, GeocodeView)
- Question 3: GenericAPIView (MenuItemListCreateView, MenuItemDetailView)
- Question 3: ListAPIView (CategoryListView)
- Question 3: ModelViewSet (OrderViewSet)
- Question 4: PageNumberPagination (configured globally, PAGE_SIZE=5)
- Question 5: Filtering (OrderViewSet filters by status)
- Question 5: Object Level Permission (IsOwnerOrAdmin on OrderViewSet)
- Question 6: Authentication (TokenAuthentication on protected views)
- Question 6: Google Maps Geocoding API (GeocodeView)
- Section B Task 1: Category API
- Section B Task 2: MenuItem CRUD API
- Section B Task 3: Order API
- Section B Task 4: Authentication
- Section C: Complete Food Delivery API
====================================================
"""

from rest_framework import status, generics, viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, MenuItem, Order
from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
    OrderSerializer,
    UserRegistrationSerializer,
)
from .permissions import IsOwnerOrAdmin
from .pagination import StandardPageNumberPagination, OrderCursorPagination
from .filters import OrderFilter, MenuItemFilter
from .utils import geocode_address


# ====================================================
# SECTION B - TASK 1: CATEGORY LIST API
# ====================================================
# Question 3 - ListAPIView (GenericAPIView subclass)
# Endpoint: GET /api/categories/
# Returns: JSON list of all categories with HTTP 200

class CategoryListView(generics.ListCreateAPIView):
    """
    Category List API - Section B Task 1

    GET  /api/categories/ → List all categories (HTTP 200)
    POST /api/categories/ → Create a new category (HTTP 201)

    Assessment Concepts:
    - Question 3: ListAPIView (GenericAPIView)
      Uses ListCreateAPIView, a subclass of GenericAPIView,
      to provide automatic list and create functionality.
    - Question 1: REST Statelessness
      Each request is independent - no session state is maintained.
    - Section B Task 1: Category API with JSON response and HTTP 200

    Permissions:
    - GET: AllowAny (public - categories are readable by everyone)
    - POST: IsAuthenticated (only authenticated users can create)
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    pagination_class = StandardPageNumberPagination

    # Search and ordering support
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']


# ====================================================
# SECTION A - QUESTION 3: CATEGORY DETAIL (APIView)
# ====================================================
# Demonstrates the use of APIView for manual request handling.

class CategoryDetailView(APIView):
    """
    Category Detail API - Section A Question 3

    GET    /api/categories/<id>/ → Retrieve category (HTTP 200)
    PUT    /api/categories/<id>/ → Update category (HTTP 200)
    DELETE /api/categories/<id>/ → Delete category (HTTP 204)

    Assessment Concept: Question 3 - APIView
    - Uses APIView (the base class for all DRF views)
    - Manually handles GET, PUT, DELETE HTTP methods
    - Demonstrates low-level view implementation
    - Returns proper HTTP status codes (200, 404)
    """

    permission_classes = [AllowAny]

    def get_object(self, pk):
        """Retrieve a category by primary key or return 404."""
        return get_object_or_404(Category, pk=pk)

    def get(self, request, pk):
        """
        Retrieve a single category by ID.

        Assessment Concept: Question 3 - APIView (GET)
        Returns HTTP 200 with category data, or HTTP 404 if not found.
        """
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Update a category by ID.

        Assessment Concept: Question 3 - APIView (PUT)
        Returns HTTP 200 with updated data, or HTTP 400 for validation errors.
        """
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a category by ID.

        Assessment Concept: Question 3 - APIView (DELETE)
        Returns HTTP 204 No Content on successful deletion.
        """
        category = self.get_object(pk)
        category.delete()
        return Response(
            {"message": "Category deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )


# ====================================================
# SECTION B - TASK 2: MENUITEM CRUD API (GenericAPIView)
# ====================================================
# Question 3 - GenericAPIView
# Implements full CRUD using GenericAPIView with mixins.
# Demonstrates manual serializer and queryset handling.

class MenuItemListCreateView(generics.ListCreateAPIView):
    """
    MenuItem List/Create API - Section B Task 2

    GET  /api/menu-items/ → List all menu items (HTTP 200)
    POST /api/menu-items/ → Create a new menu item (HTTP 201)

    Assessment Concepts:
    - Question 3: GenericAPIView
      Uses ListCreateAPIView (GenericAPIView subclass) for list and create.
    - Question 2: ModelSerializer Validation
      MenuItemSerializer validates price > 0 and name not empty.
    - Section B Task 2: MenuItem CRUD API

    HTTP Status Codes:
    - 200: Successful list retrieval
    - 201: Successful creation
    - 400: Validation error (price <= 0, empty name)

    Permissions:
    - GET: AllowAny (menu items are publicly viewable)
    - POST: IsAuthenticated (only authenticated users can create items)
    """

    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    pagination_class = StandardPageNumberPagination

    # Question 5 - Filtering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = MenuItemFilter
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['name', 'price', 'created_at']
    ordering = ['category', 'name']

    def get_permissions(self):
        """
        Allow anyone to view menu items, but require authentication to create.
        """
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]


class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    MenuItem Detail API - Section B Task 2

    GET    /api/menu-items/<id>/ → Retrieve menu item (HTTP 200)
    PUT    /api/menu-items/<id>/ → Full update menu item (HTTP 200)
    PATCH  /api/menu-items/<id>/ → Partial update menu item (HTTP 200)
    DELETE /api/menu-items/<id>/ → Delete menu item (HTTP 204)

    Assessment Concepts:
    - Question 3: GenericAPIView
      Uses RetrieveUpdateDestroyAPIView for full CRUD detail operations.
    - Section B Task 2: Implement GET, POST, PUT, PATCH, DELETE

    HTTP Status Codes:
    - 200: Successful retrieval or update
    - 400: Validation error
    - 404: Menu item not found
    """

    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        """
        Allow anyone to view menu items, but require authentication to modify.
        """
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]


# ====================================================
# SECTION B - TASK 3: ORDER API (ModelViewSet)
# ====================================================
# Question 3 - ModelViewSet + DefaultRouter
# Question 4 - PageNumberPagination (PAGE_SIZE = 5)
# Question 5 - Filtering (?status=pending) + Object Level Permission
# Question 6 - Authentication (TokenAuthentication, IsAuthenticated)

class OrderViewSet(viewsets.ModelViewSet):
    """
    Order API - Section B Task 3 & Task 4

    Full CRUD operations on Order model using ModelViewSet.
    Registered with DefaultRouter for automatic URL generation.

    Assessment Concepts:
    - Question 3: ModelViewSet + DefaultRouter
      ModelViewSet provides list, create, retrieve, update, partial_update,
      and destroy actions automatically. Registered via DefaultRouter.
    - Question 4: PageNumberPagination (PAGE_SIZE = 5)
      Orders are paginated with 5 items per page.
    - Question 5: Filtering (/api/orders/?status=pending)
      Orders can be filtered by status using DjangoFilterBackend.
    - Question 5: Object Level Permission (IsOwnerOrAdmin)
      Users can only access their own orders.
    - Question 6: Authentication (TokenAuthentication)
      Only authenticated users can access order endpoints.
      Unauthenticated requests return HTTP 401.

    Endpoints (auto-generated by DefaultRouter):
        GET    /api/orders/       → List user's orders (HTTP 200)
        POST   /api/orders/       → Create new order (HTTP 201)
        GET    /api/orders/<id>/  → Retrieve order (HTTP 200)
        PUT    /api/orders/<id>/  → Full update order (HTTP 200)
        PATCH  /api/orders/<id>/  → Partial update order (HTTP 200)
        DELETE /api/orders/<id>/  → Delete order (HTTP 204)

    Filtering Examples:
        GET /api/orders/?status=pending
        GET /api/orders/?status=delivered
        GET /api/orders/?customer_name=John

    HTTP Status Codes:
        200: Successful list/retrieve/update
        201: Order created successfully
        400: Validation error (quantity <= 0, empty name)
        401: Unauthenticated request
        403: User trying to access another user's order
        404: Order not found
    """

    serializer_class = OrderSerializer
    pagination_class = StandardPageNumberPagination

    # Question 6 - Authentication & Authorization
    # Only authenticated users can access orders
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    # Question 5 - Filtering
    # Enable filtering by status, customer_name, etc.
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = OrderFilter
    search_fields = ['customer_name', 'item__name']
    ordering_fields = ['created_at', 'status', 'quantity']
    ordering = ['-created_at']

    def get_queryset(self):
        """
        Return orders for the authenticated user only.

        Assessment Concept: Question 5 - Object Level Permission
        Regular users see only their own orders.
        Admin users see all orders.
        """
        user = self.request.user
        if user.is_staff:
            # Admin users can see all orders
            return Order.objects.select_related('item', 'item__category', 'customer').all()
        # Regular users see only their own orders
        return Order.objects.select_related('item', 'item__category', 'customer').filter(
            customer=user
        )

    def perform_create(self, serializer):
        """
        Create a new order for the authenticated user.

        Assessment Concepts:
        - Question 5: Object Level Permission (auto-assign customer)
        - Question 6: Google Maps Geocoding API (geocode delivery address)

        The customer is automatically set to the authenticated user.
        If a delivery_address is provided, it is geocoded using Google Maps API.
        """
        # Auto-assign the authenticated user as the customer
        order = serializer.save(customer=self.request.user)

        # Question 6 - Google Maps Geocoding API Integration
        # If a delivery address is provided, geocode it
        if order.delivery_address:
            coordinates = geocode_address(order.delivery_address)
            if coordinates:
                order.latitude = coordinates['latitude']
                order.longitude = coordinates['longitude']
                order.save(update_fields=['latitude', 'longitude'])


# ====================================================
# SECTION A - QUESTION 6: GOOGLE MAPS GEOCODING VIEW
# ====================================================
# Demonstrates direct Google Maps API integration.

class GeocodeView(APIView):
    """
    Geocode API - Section A Question 6

    POST /api/geocode/ → Geocode an address to coordinates

    Assessment Concept: Question 6 - Google Maps Geocoding API Integration
    - Accepts a delivery address in the request body
    - Calls Google Maps Geocoding API to get coordinates
    - Returns latitude, longitude, and formatted address
    - Demonstrates external API integration

    Request Body:
        {"address": "1600 Amphitheatre Parkway, Mountain View, CA"}

    Response (HTTP 200):
        {
            "address": "1600 Amphitheatre Parkway, Mountain View, CA",
            "latitude": 37.4224764,
            "longitude": -122.0842499,
            "formatted_address": "1600 Amphitheatre Pkwy, Mountain View, CA 94043"
        }

    Error Response (HTTP 400):
        {"error": "Address is required."}

    Error Response (HTTP 502):
        {"error": "Unable to geocode the address."}
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Geocode an address using Google Maps Geocoding API.

        Assessment Concept: Question 6 - Google Maps Geocoding API
        """
        address = request.data.get('address', '').strip()

        if not address:
            return Response(
                {"error": "Address is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Question 6 - Call Google Maps Geocoding API
        result = geocode_address(address)

        if result:
            return Response({
                "address": address,
                "latitude": result['latitude'],
                "longitude": result['longitude'],
                "formatted_address": result['formatted_address'],
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Unable to geocode the address. Please check the address or API key."},
                status=status.HTTP_502_BAD_GATEWAY
            )


# ====================================================
# USER REGISTRATION VIEW
# ====================================================
# Supports the authentication flow (Question 6).
# New users register, then obtain a token via /api-token-auth/.

class UserRegistrationView(APIView):
    """
    User Registration API

    POST /api/register/ → Register a new user account

    Assessment Concept: Question 6 - Authentication
    - Creates a new user account
    - Generates an authentication token for the user
    - Returns user details and token

    Request Body:
        {
            "username": "john_doe",
            "email": "john@example.com",
            "password": "securepass123",
            "password_confirm": "securepass123",
            "first_name": "John",
            "last_name": "Doe"
        }

    Response (HTTP 201):
        {
            "message": "Registration successful.",
            "user": {"id": 1, "username": "john_doe", ...},
            "token": "abc123..."
        }
    """

    permission_classes = [AllowAny]

    def post(self, request):
        """
        Register a new user and return authentication token.

        Assessment Concept: Question 6 - Authentication
        """
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            # Generate authentication token for the new user
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "message": "Registration successful. Use the token for authenticated API requests.",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
                "token": token.key,
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ====================================================
# DASHBOARD VIEW
# ====================================================
# Premium API Dashboard with statistics and overview.

class DashboardView(APIView):
    """
    API Dashboard View

    GET /api/dashboard/ → Returns API statistics and overview

    Provides a summary of the Food Delivery API data:
    - Total categories, menu items, orders
    - Order status breakdown
    - Recent orders
    """

    permission_classes = [AllowAny]

    def get(self, request):
        """Return API dashboard data."""
        # Get counts
        total_categories = Category.objects.count()
        total_menu_items = MenuItem.objects.count()
        total_orders = Order.objects.count()
        available_items = MenuItem.objects.filter(is_available=True).count()

        # Order status breakdown
        status_breakdown = {}
        for status_choice in Order.STATUS_CHOICES:
            status_breakdown[status_choice[0]] = Order.objects.filter(
                status=status_choice[0]
            ).count()

        # Recent orders (last 5)
        recent_orders = Order.objects.select_related('item', 'customer').order_by('-created_at')[:5]
        recent_orders_data = OrderSerializer(recent_orders, many=True).data

        return Response({
            "dashboard": {
                "total_categories": total_categories,
                "total_menu_items": total_menu_items,
                "available_items": available_items,
                "total_orders": total_orders,
                "order_status_breakdown": status_breakdown,
                "recent_orders": recent_orders_data,
            }
        }, status=status.HTTP_200_OK)


# ====================================================
# HTML DASHBOARD VIEW (Premium UI)
# ====================================================
# Renders the premium dashboard template

def dashboard_page(request):
    """
    Render the premium HTML dashboard page.
    Displays API statistics, recent orders, and quick links.
    """
    context = {
        'total_categories': Category.objects.count(),
        'total_menu_items': MenuItem.objects.count(),
        'total_orders': Order.objects.count(),
        'available_items': MenuItem.objects.filter(is_available=True).count(),
        'pending_orders': Order.objects.filter(status='pending').count(),
        'delivered_orders': Order.objects.filter(status='delivered').count(),
        'recent_orders': Order.objects.select_related('item', 'customer').order_by('-created_at')[:10],
        'categories': Category.objects.all(),
        'popular_items': MenuItem.objects.filter(is_available=True).order_by('-created_at')[:6],
    }
    return render(request, 'api/dashboard.html', context)


# ====================================================
# CURRENT USER VIEW
# ====================================================
class CurrentUserView(APIView):
    """
    Returns details of the currently authenticated user.
    Required for frontend profile integration and setting customer_name on orders.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_joined': user.date_joined,
        })
