"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api
Application: api

Models Definition
====================================================

This module defines all database models for the Food Delivery API:
- Category: Food categories (Section B - Task 1)
- MenuItem: Individual food items (Section B - Task 2)
- Order: Customer orders (Section B - Task 3)

Assessment Concepts Covered:
- Question 1: REST Statelessness (models are resource representations)
- Question 2: ModelSerializer Validation (models define data structure)
- Section B Task 1: Category Model
- Section B Task 2: MenuItem Model
- Section B Task 3: Order Model
- Section C: Complete Food Delivery API (all models work together)
====================================================
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# ====================================================
# SECTION B - TASK 1: CATEGORY MODEL
# ====================================================
# Question 1 - REST Statelessness
# Each Category is a RESTful resource with its own URI.
# The API is stateless - no session data is stored between requests.

class Category(models.Model):
    """
    Category Model - Section B Task 1

    Represents a food category in the delivery system.
    Examples: Pizza, Burgers, Drinks, Desserts, etc.

    Fields:
        - name: The category name (unique, required)
        - description: Optional description of the category
        - created_at: Timestamp of creation
        - updated_at: Timestamp of last update
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Name of the food category (e.g., Pizza, Burgers, Drinks)"
    )
    description = models.TextField(
        blank=True,
        default='',
        help_text="Optional description of the category"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the category was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the category was last updated"
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


# ====================================================
# SECTION B - TASK 2: MENUITEM MODEL
# ====================================================
# Question 2 - ModelSerializer Validation
# The MenuItem model defines fields that will be validated
# by the MenuItemSerializer (e.g., price > 0).

class MenuItem(models.Model):
    """
    MenuItem Model - Section B Task 2

    Represents an individual food item available for ordering.
    Each item belongs to a Category and has a price.

    Fields:
        - name: The item name (required)
        - price: Price in decimal (must be > 0, validated in serializer)
        - category: ForeignKey to Category
        - is_available: Whether the item is currently available
        - description: Optional item description
        - created_at: Timestamp of creation
        - updated_at: Timestamp of last update

    Validation (in serializer):
        - Price must be greater than zero
        - Name cannot be empty
    """

    name = models.CharField(
        max_length=200,
        help_text="Name of the menu item (e.g., Margherita Pizza)"
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        help_text="Price of the item (must be greater than zero)"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='menu_items',
        help_text="Category this item belongs to"
    )
    is_available = models.BooleanField(
        default=True,
        help_text="Whether this item is currently available for ordering"
    )
    description = models.TextField(
        blank=True,
        default='',
        help_text="Optional description of the menu item"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the item was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the item was last updated"
    )

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} - ${self.price}"


# ====================================================
# SECTION B - TASK 3: ORDER MODEL
# ====================================================
# Question 3 - ModelViewSet + DefaultRouter
# The Order model is managed by OrderViewSet (ModelViewSet)
# and registered using DefaultRouter for automatic CRUD URLs.
#
# Question 4 - Pagination
# Orders are paginated using PageNumberPagination (PAGE_SIZE=5).
#
# Question 5 - Filtering & Object Level Permission
# Orders can be filtered by status (?status=pending).
# Users can only see their own orders (Object Level Permission).
#
# Question 6 - Authentication
# Only authenticated users can create and view orders.

class Order(models.Model):
    """
    Order Model - Section B Task 3

    Represents a customer's food order in the delivery system.
    Linked to a User (customer) and a MenuItem.

    Fields:
        - customer: ForeignKey to User (the person placing the order)
        - customer_name: Display name for the customer
        - item: ForeignKey to MenuItem (the food item ordered)
        - quantity: Number of items ordered (must be > 0)
        - status: Current order status (pending/confirmed/preparing/
                  out_for_delivery/delivered/cancelled)
        - delivery_address: Delivery address text
        - latitude: Geocoded latitude (from Google Maps API - Question 6)
        - longitude: Geocoded longitude (from Google Maps API - Question 6)
        - created_at: Timestamp when order was placed
        - updated_at: Timestamp of last update

    Filtering:
        - /api/orders/?status=pending (Question 5 - Filtering)

    Pagination:
        - PageNumberPagination with PAGE_SIZE=5 (Question 4)

    Permissions:
        - IsAuthenticated: Only logged-in users can access (Question 6)
        - IsOwnerOrAdmin: Users see only their own orders (Question 5)
    """

    # Order Status Choices
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        help_text="The user who placed this order"
    )
    customer_name = models.CharField(
        max_length=200,
        help_text="Display name of the customer"
    )
    item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        related_name='orders',
        help_text="The menu item that was ordered"
    )
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        help_text="Number of items ordered (must be greater than zero)"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        help_text="Current status of the order"
    )
    delivery_address = models.TextField(
        blank=True,
        default='',
        help_text="Delivery address for this order"
    )
    # Question 6 - Google Maps Geocoding API Integration
    # These fields store geocoded coordinates from the delivery address
    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True,
        help_text="Geocoded latitude of delivery address (Google Maps API)"
    )
    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True,
        help_text="Geocoded longitude of delivery address (Google Maps API)"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the order was placed"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the order was last updated"
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.pk} - {self.customer_name} - {self.item.name} x{self.quantity}"

    @property
    def total_price(self):
        """Calculate the total price for this order."""
        return self.item.price * self.quantity
