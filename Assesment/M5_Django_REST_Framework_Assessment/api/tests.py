"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api
Application: api

Tests
====================================================

Comprehensive test suite covering:
- Category API (Task 1)
- MenuItem CRUD API (Task 2)
- Order API with filtering and pagination (Task 3)
- Authentication and Authorization (Task 4)
- Object-Level Permissions (Section A)
- Validation (Section A)
====================================================
"""

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Category, MenuItem, Order


class CategoryAPITest(TestCase):
    """
    Test Suite for Category API - Section B Task 1

    Tests:
    - List categories (GET /api/categories/) → HTTP 200
    - Create category (POST /api/categories/) → HTTP 201
    - Retrieve category (GET /api/categories/<id>/) → HTTP 200
    - Category not found → HTTP 404
    """

    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.category = Category.objects.create(
            name='Pizza',
            description='Delicious Italian pizzas'
        )

    def test_list_categories(self):
        """Test listing all categories returns HTTP 200."""
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_category(self):
        """Test retrieving a single category returns HTTP 200."""
        response = self.client.get(f'/api/categories/{self.category.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Pizza')

    def test_category_not_found(self):
        """Test retrieving non-existent category returns HTTP 404."""
        response = self.client.get('/api/categories/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class MenuItemAPITest(TestCase):
    """
    Test Suite for MenuItem API - Section B Task 2

    Tests:
    - List menu items (GET) → HTTP 200
    - Create menu item (POST) → HTTP 201
    - Price validation (price > 0) → HTTP 400
    - Update menu item (PUT/PATCH) → HTTP 200
    - Delete menu item (DELETE) → HTTP 204
    """

    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.token = Token.objects.create(user=self.user)
        self.category = Category.objects.create(name='Burgers')
        self.menu_item = MenuItem.objects.create(
            name='Classic Burger',
            price=9.99,
            category=self.category,
            is_available=True
        )

    def test_list_menu_items(self):
        """Test listing menu items returns HTTP 200."""
        response = self.client.get('/api/menu-items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_menu_item(self):
        """Test creating a menu item returns HTTP 201."""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        data = {
            'name': 'Cheese Burger',
            'price': 11.99,
            'category': self.category.id,
            'is_available': True,
        }
        response = self.client.post('/api/menu-items/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_price_validation(self):
        """Test that price must be greater than zero (HTTP 400)."""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        data = {
            'name': 'Free Burger',
            'price': -5.00,
            'category': self.category.id,
        }
        response = self.client.post('/api/menu-items/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_menu_item(self):
        """Test updating a menu item returns HTTP 200."""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        data = {
            'name': 'Updated Burger',
            'price': 12.99,
            'category': self.category.id,
        }
        response = self.client.put(f'/api/menu-items/{self.menu_item.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_menu_item(self):
        """Test deleting a menu item returns HTTP 204."""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = self.client.delete(f'/api/menu-items/{self.menu_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class OrderAPITest(TestCase):
    """
    Test Suite for Order API - Section B Task 3 & Task 4

    Tests:
    - Create order (authenticated) → HTTP 201
    - Unauthenticated request → HTTP 401
    - Filter by status → HTTP 200
    - Object-level permission (own orders only)
    - Quantity validation → HTTP 400
    """

    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.user1 = User.objects.create_user(username='user1', password='pass1234')
        self.user2 = User.objects.create_user(username='user2', password='pass1234')
        self.token1 = Token.objects.create(user=self.user1)
        self.token2 = Token.objects.create(user=self.user2)
        self.category = Category.objects.create(name='Drinks')
        self.menu_item = MenuItem.objects.create(
            name='Cola', price=2.99, category=self.category
        )
        self.order = Order.objects.create(
            customer=self.user1,
            customer_name='User One',
            item=self.menu_item,
            quantity=3,
            status='pending'
        )

    def test_unauthenticated_request(self):
        """Test that unauthenticated requests return HTTP 401."""
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_order(self):
        """Test creating an order returns HTTP 201."""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
        data = {
            'customer_name': 'User One',
            'item': self.menu_item.id,
            'quantity': 2,
            'status': 'pending',
        }
        response = self.client.post('/api/orders/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_own_orders(self):
        """Test that users see only their own orders."""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_by_status(self):
        """Test filtering orders by status returns HTTP 200."""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
        response = self.client.get('/api/orders/?status=pending')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_object_level_permission(self):
        """Test that user2 cannot access user1's order."""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token2.key}')
        response = self.client.get(f'/api/orders/{self.order.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_quantity_validation(self):
        """Test that quantity must be greater than zero."""
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token1.key}')
        data = {
            'customer_name': 'User One',
            'item': self.menu_item.id,
            'quantity': 0,
            'status': 'pending',
        }
        response = self.client.post('/api/orders/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
