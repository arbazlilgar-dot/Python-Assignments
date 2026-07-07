"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api
Application: api

Filter Classes
====================================================

This module defines custom filter classes:
- OrderFilter: Filters orders by status, customer_name, etc.
- MenuItemFilter: Filters menu items by category, availability, price

Assessment Concepts Covered:
- Question 5: Filtering
  Support query filtering on orders (e.g., ?status=pending)
====================================================
"""

import django_filters
from .models import Order, MenuItem


# ====================================================
# QUESTION 5 - ORDER FILTER
# ====================================================
# Enables filtering orders by status, customer_name, and date range.
# Example: /api/orders/?status=pending

class OrderFilter(django_filters.FilterSet):
    """
    Order Filter - Question 5

    Enables query parameter filtering on the Order model.

    Assessment Concept: Question 5 - Filtering
    - Filter by status: /api/orders/?status=pending
    - Filter by customer_name: /api/orders/?customer_name=John
    - Filter by date range: /api/orders/?created_after=2024-01-01

    Supported Filters:
        - status: Exact match (e.g., pending, confirmed, delivered)
        - customer_name: Case-insensitive contains
        - item: Filter by menu item ID
        - created_after: Orders created after a specific date
        - created_before: Orders created before a specific date
        - min_quantity: Minimum quantity filter
    """

    # Question 5 - Filtering by status
    # Example: /api/orders/?status=pending
    status = django_filters.CharFilter(
        field_name='status',
        lookup_expr='exact',
        help_text="Filter by order status (e.g., pending, confirmed, delivered)"
    )

    # Filter by customer name (case-insensitive partial match)
    customer_name = django_filters.CharFilter(
        field_name='customer_name',
        lookup_expr='icontains',
        help_text="Filter by customer name (case-insensitive)"
    )

    # Filter by menu item
    item = django_filters.NumberFilter(
        field_name='item__id',
        help_text="Filter by menu item ID"
    )

    # Date range filters
    created_after = django_filters.DateTimeFilter(
        field_name='created_at',
        lookup_expr='gte',
        help_text="Filter orders created after this date"
    )
    created_before = django_filters.DateTimeFilter(
        field_name='created_at',
        lookup_expr='lte',
        help_text="Filter orders created before this date"
    )

    # Quantity filter
    min_quantity = django_filters.NumberFilter(
        field_name='quantity',
        lookup_expr='gte',
        help_text="Filter orders with minimum quantity"
    )

    class Meta:
        model = Order
        fields = ['status', 'customer_name', 'item', 'created_after', 'created_before', 'min_quantity']


# ====================================================
# MENUITEM FILTER
# ====================================================
# Additional filter for menu items

class MenuItemFilter(django_filters.FilterSet):
    """
    MenuItem Filter

    Enables query parameter filtering on the MenuItem model.

    Supported Filters:
        - category: Filter by category ID
        - is_available: Filter by availability
        - min_price: Minimum price filter
        - max_price: Maximum price filter
        - name: Case-insensitive name search
    """

    category = django_filters.NumberFilter(
        field_name='category__id',
        help_text="Filter by category ID"
    )
    is_available = django_filters.BooleanFilter(
        field_name='is_available',
        help_text="Filter by availability (true/false)"
    )
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        help_text="Minimum price"
    )
    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        help_text="Maximum price"
    )
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        help_text="Search by item name (case-insensitive)"
    )

    class Meta:
        model = MenuItem
        fields = ['category', 'is_available', 'min_price', 'max_price', 'name']
