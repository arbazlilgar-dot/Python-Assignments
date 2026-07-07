"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api
Application: api

Serializers
====================================================

This module defines all serializers for the Food Delivery API:
- CategorySerializer: Serializes Category data (Task 1)
- MenuItemSerializer: Serializes MenuItem data with validation (Task 2)
- OrderSerializer: Serializes Order data with validation (Task 3)
- UserRegistrationSerializer: Handles user registration

Assessment Concepts Covered:
- Question 2: ModelSerializer - All serializers use ModelSerializer
- Question 2: Field Validation - Price > 0, Quantity > 0, Name not empty
- Section B Task 1: CategorySerializer
- Section B Task 2: MenuItemSerializer with price validation
- Section B Task 3: OrderSerializer
====================================================
"""

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, MenuItem, Order


# ====================================================
# SECTION B - TASK 1: CATEGORY SERIALIZER
# ====================================================
# Question 2 - ModelSerializer
# Using ModelSerializer to automatically generate fields
# from the Category model.

class CategorySerializer(serializers.ModelSerializer):
    """
    CategorySerializer - Section B Task 1

    Serializes the Category model using ModelSerializer.
    Automatically generates serializer fields from model fields.

    Assessment Concept: Question 2 - ModelSerializer
    - Demonstrates the use of ModelSerializer
    - Automatically maps model fields to serializer fields
    - Provides default create() and update() implementations
    """

    # Read-only field showing count of menu items in this category
    menu_items_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'menu_items_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_menu_items_count(self, obj):
        """Return the count of menu items in this category."""
        return obj.menu_items.count()

    # Question 2 - Field Validation
    # Name cannot be empty
    def validate_name(self, value):
        """
        Validate that the category name is not empty or whitespace.
        Assessment Concept: Question 2 - Field Validation
        """
        if not value or not value.strip():
            raise serializers.ValidationError("Category name cannot be empty.")
        return value.strip()


# ====================================================
# SECTION B - TASK 2: MENUITEM SERIALIZER
# ====================================================
# Question 2 - ModelSerializer Validation
# Validates that price is greater than zero.
# Validates that name is not empty.

class MenuItemSerializer(serializers.ModelSerializer):
    """
    MenuItemSerializer - Section B Task 2

    Serializes the MenuItem model with custom validation.

    Assessment Concepts:
    - Question 2: ModelSerializer - Uses ModelSerializer
    - Question 2: Field Validation - Price must be > 0, Name not empty

    Validation Rules:
    - price: Must be greater than zero (returns HTTP 400 if invalid)
    - name: Cannot be empty (returns HTTP 400 if invalid)
    """

    # Display category name (read-only)
    category_name = serializers.CharField(source='category.name', read_only=True)

    # Display total orders for this item
    total_orders = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = [
            'id', 'name', 'price', 'category', 'category_name',
            'is_available', 'description', 'total_orders',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_total_orders(self, obj):
        """Return the total number of orders for this menu item."""
        return obj.orders.count()

    # Question 2 - Field Validation: Price must be greater than zero
    def validate_price(self, value):
        """
        Validate that the price is greater than zero.

        Assessment Concept: Question 2 - ModelSerializer Validation
        Returns HTTP 400 Bad Request if validation fails.
        """
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than zero."
            )
        return value

    # Question 2 - Field Validation: Name cannot be empty
    def validate_name(self, value):
        """
        Validate that the menu item name is not empty or whitespace.

        Assessment Concept: Question 2 - Field Validation
        Returns HTTP 400 Bad Request if validation fails.
        """
        if not value or not value.strip():
            raise serializers.ValidationError(
                "Menu item name cannot be empty."
            )
        return value.strip()


# ====================================================
# SECTION B - TASK 3: ORDER SERIALIZER
# ====================================================
# Question 2 - ModelSerializer Validation
# Validates quantity > 0 and customer_name not empty.
# Question 5 - Object Level Permission
# The customer field is automatically set to the authenticated user.

class OrderSerializer(serializers.ModelSerializer):
    """
    OrderSerializer - Section B Task 3

    Serializes the Order model with custom validation.

    Assessment Concepts:
    - Question 2: ModelSerializer Validation (quantity > 0, name not empty)
    - Question 5: Object Level Permission (customer auto-set to request.user)
    - Question 6: Authentication (only authenticated users can create orders)

    Validation Rules:
    - quantity: Must be greater than zero
    - customer_name: Cannot be empty
    - customer: Automatically set to the authenticated user
    """

    # Read-only fields for display
    item_name = serializers.CharField(source='item.name', read_only=True)
    item_price = serializers.DecimalField(
        source='item.price', max_digits=8, decimal_places=2, read_only=True
    )
    total_price = serializers.SerializerMethodField()
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'customer', 'customer_name', 'item', 'item_name',
            'item_price', 'quantity', 'total_price', 'status',
            'status_display', 'delivery_address', 'latitude', 'longitude',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'customer', 'latitude', 'longitude', 'created_at', 'updated_at']

    def get_total_price(self, obj):
        """Calculate and return the total price (item price × quantity)."""
        return str(obj.item.price * obj.quantity)

    # Question 2 - Field Validation: Quantity must be greater than zero
    def validate_quantity(self, value):
        """
        Validate that the quantity is greater than zero.

        Assessment Concept: Question 2 - ModelSerializer Validation
        Returns HTTP 400 Bad Request if validation fails.
        """
        if value <= 0:
            raise serializers.ValidationError(
                "Quantity must be greater than zero."
            )
        return value

    # Question 2 - Field Validation: Customer name cannot be empty
    def validate_customer_name(self, value):
        """
        Validate that the customer name is not empty or whitespace.

        Assessment Concept: Question 2 - Field Validation
        Returns HTTP 400 Bad Request if validation fails.
        """
        if not value or not value.strip():
            raise serializers.ValidationError(
                "Customer name cannot be empty."
            )
        return value.strip()

    # Question 5 - Object Level Permission
    # Automatically assign the authenticated user as the customer
    def create(self, validated_data):
        """
        Create a new order with the authenticated user as customer.

        Assessment Concept: Question 5 - Object Level Permission
        The customer field is automatically set to request.user,
        ensuring users can only create orders for themselves.
        """
        validated_data['customer'] = self.context['request'].user
        return super().create(validated_data)


# ====================================================
# USER REGISTRATION SERIALIZER
# ====================================================
# Enables new users to register and receive an auth token.
# Supports the authentication flow (Question 6).

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    UserRegistrationSerializer

    Handles user registration for the Food Delivery API.
    Creates a new user and returns user details.

    Assessment Concept: Question 6 - Authentication
    New users must register before they can obtain a token
    and access protected API endpoints.
    """

    password = serializers.CharField(
        write_only=True,
        min_length=8,
        help_text="Password must be at least 8 characters long."
    )
    password_confirm = serializers.CharField(
        write_only=True,
        help_text="Confirm your password."
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password_confirm', 'first_name', 'last_name']
        read_only_fields = ['id']

    def validate(self, data):
        """Validate that passwords match."""
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({
                "password_confirm": "Passwords do not match."
            })
        return data

    def validate_username(self, value):
        """Validate that username is unique."""
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    def create(self, validated_data):
        """Create a new user with hashed password."""
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        return user
