# 🍕 Food Delivery REST API

## M5 Django REST Framework Assessment

A complete, industry-level Food Delivery REST API built with **Django REST Framework**. This project demonstrates all core DRF concepts including ModelSerializer, APIView, GenericAPIView, ModelViewSet, DefaultRouter, Pagination, Filtering, Authentication, Authorization, Object-Level Permissions, and Google Maps Geocoding API integration.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Assessment Concepts](#assessment-concepts)
- [Project Structure](#project-structure)
- [Sample API Requests](#sample-api-requests)
- [Testing](#testing)

---

## 🏗️ Project Overview

| Detail | Value |
|---|---|
| **Project Name** | `food_delivery_api` |
| **Application Name** | `api` |
| **Framework** | Django 4.2 + Django REST Framework |
| **Database** | SQLite |
| **Authentication** | Token Authentication |
| **Pagination** | PageNumberPagination (PAGE_SIZE = 5) |

---

## 🚀 Setup Instructions

### 1. Navigate to the Project Directory

```bash
cd M5_Django_REST_Framework_Assessment
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Environment Variables (.env)

Create a `.env` file in the root directory and add your secrets. Never expose this file.

```env
SECRET_KEY=YOUR_SECRET_KEY
DEBUG=True
ALLOWED_HOSTS=*
GOOGLE_MAPS_API_KEY=YOUR_API_KEY
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Server

```bash
python manage.py runserver
```

### 8. Access the Application

| URL | Description |
|---|---|
| `http://127.0.0.1:8000/api/` | API Dashboard |
| `http://127.0.0.1:8000/admin/` | Admin Panel |
| `http://127.0.0.1:8000/api/categories/` | Categories API |
| `http://127.0.0.1:8000/api/menu-items/` | Menu Items API |
| `http://127.0.0.1:8000/api/orders/` | Orders API |

---

## 🔗 API Endpoints

### Category Endpoints (Section B - Task 1)

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `GET` | `/api/categories/` | List all categories | No |
| `POST` | `/api/categories/` | Create a category | No |
| `GET` | `/api/categories/<id>/` | Retrieve a category | No |
| `PUT` | `/api/categories/<id>/` | Update a category | No |
| `DELETE` | `/api/categories/<id>/` | Delete a category | No |

### MenuItem Endpoints (Section B - Task 2)

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `GET` | `/api/menu-items/` | List all menu items | No |
| `POST` | `/api/menu-items/` | Create a menu item | Yes |
| `GET` | `/api/menu-items/<id>/` | Retrieve a menu item | No |
| `PUT` | `/api/menu-items/<id>/` | Update a menu item | Yes |
| `PATCH` | `/api/menu-items/<id>/` | Partial update menu item | Yes |
| `DELETE` | `/api/menu-items/<id>/` | Delete a menu item | Yes |

### Order Endpoints (Section B - Task 3 & 4)

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `GET` | `/api/orders/` | List user's orders | Yes |
| `POST` | `/api/orders/` | Create a new order | Yes |
| `GET` | `/api/orders/<id>/` | Retrieve an order | Yes |
| `PUT` | `/api/orders/<id>/` | Update an order | Yes |
| `PATCH` | `/api/orders/<id>/` | Partial update order | Yes |
| `DELETE` | `/api/orders/<id>/` | Delete an order | Yes |
| `GET` | `/api/orders/?status=pending` | Filter by status | Yes |

### Authentication Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/register/` | Register a new user |
| `POST` | `/api-token-auth/` | Obtain auth token |

### Utility Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/api/geocode/` | Geocode an address | Yes |
| `GET` | `/api/dashboard/` | API statistics | No |

---

## 🔐 Authentication

This project uses **Token Authentication** (Section B - Task 4).

### Step 1: Register a User

```bash
curl -X POST http://127.0.0.1:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepass123",
    "password_confirm": "securepass123"
  }'
```

### Step 2: Get Auth Token

```bash
curl -X POST http://127.0.0.1:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "password": "securepass123"}'
```

### Step 3: Use Token in Requests

```bash
curl -X GET http://127.0.0.1:8000/api/orders/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

**In Postman:**
- Go to the **Authorization** tab
- Select **API Key**
- Key: `Authorization`
- Value: `Token YOUR_TOKEN_HERE`
- Add to: **Header**

---

## 📚 Assessment Concepts

### Section A Concepts

| # | Concept | Implementation |
|---|---|---|
| Q1 | REST Statelessness | All API views are stateless; token-based auth |
| Q2 | ModelSerializer | `CategorySerializer`, `MenuItemSerializer`, `OrderSerializer` |
| Q2 | Field Validation | Price > 0, Quantity > 0, Name not empty |
| Q3 | APIView | `CategoryDetailView`, `GeocodeView` |
| Q3 | GenericAPIView | `MenuItemListCreateView`, `MenuItemDetailView` |
| Q3 | ModelViewSet | `OrderViewSet` |
| Q3 | DefaultRouter | Auto-generates Order CRUD URLs |
| Q4 | PageNumberPagination | PAGE_SIZE = 5 (global default) |
| Q4 | CursorPagination | `OrderCursorPagination` class |
| Q5 | Filtering | `?status=pending` via DjangoFilterBackend |
| Q5 | Object Level Permission | `IsOwnerOrAdmin` - users see own orders only |
| Q6 | Authentication | TokenAuthentication + IsAuthenticated |
| Q6 | Google Maps Geocoding | `GeocodeView` + `geocode_address()` utility |

### Section B Tasks

| Task | Description | Status |
|---|---|---|
| Task 1 | Category API with ListAPIView | ✅ Complete |
| Task 2 | MenuItem CRUD with validation | ✅ Complete |
| Task 3 | Order API with ModelViewSet + pagination + filtering | ✅ Complete |
| Task 4 | Token Authentication + user-only access | ✅ Complete |

### Section C

| Requirement | Status |
|---|---|
| Complete Food Delivery API | ✅ Complete |
| All resources work together | ✅ Complete |
| Category + MenuItem + Order models | ✅ Complete |
| Clean project structure | ✅ Complete |

---

## 📁 Project Structure

```
M5_Django_REST_Framework_Assessment/
│
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore file
├── README.md                          # Project documentation
│
├── food_delivery_api/                 # Django Project Package
│   ├── __init__.py
│   ├── settings.py                    # Project settings (DRF config)
│   ├── urls.py                        # Root URL configuration
│   ├── wsgi.py                        # WSGI configuration
│   └── asgi.py                        # ASGI configuration
│
├── api/                               # Django App Package
│   ├── __init__.py
│   ├── apps.py                        # App configuration
│   ├── models.py                      # Category, MenuItem, Order models
│   ├── serializers.py                 # ModelSerializers with validation
│   ├── views.py                       # APIView, GenericAPIView, ModelViewSet
│   ├── urls.py                        # URL patterns + DefaultRouter
│   ├── permissions.py                 # IsOwnerOrAdmin (Object Level Permission)
│   ├── pagination.py                  # PageNumberPagination, CursorPagination
│   ├── filters.py                     # OrderFilter, MenuItemFilter
│   ├── utils.py                       # Google Maps Geocoding API utility
│   ├── admin.py                       # Admin configuration
│   ├── tests.py                       # Test suite
│   └── templates/
│       ├── rest_framework/
│       │   └── api.html               # Custom Browsable API template
│       └── api/
│           └── dashboard.html         # Premium dashboard template
│
├── static/                            # Static files
├── media/                             # Media files (uploads)
└── templates/                         # Global templates
```

---

## 📮 Sample API Requests (Postman)

### Create a Category

```http
POST /api/categories/
Content-Type: application/json

{
    "name": "Pizza",
    "description": "Delicious Italian-style pizzas"
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "name": "Pizza",
    "description": "Delicious Italian-style pizzas",
    "menu_items_count": 0,
    "created_at": "2024-01-01 12:00:00",
    "updated_at": "2024-01-01 12:00:00"
}
```

### Create a Menu Item

```http
POST /api/menu-items/
Authorization: Token YOUR_TOKEN
Content-Type: application/json

{
    "name": "Margherita Pizza",
    "price": 12.99,
    "category": 1,
    "is_available": true,
    "description": "Classic pizza with tomato sauce and mozzarella"
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "name": "Margherita Pizza",
    "price": "12.99",
    "category": 1,
    "category_name": "Pizza",
    "is_available": true,
    "description": "Classic pizza with tomato sauce and mozzarella",
    "total_orders": 0,
    "created_at": "2024-01-01 12:00:00",
    "updated_at": "2024-01-01 12:00:00"
}
```

### Create an Order

```http
POST /api/orders/
Authorization: Token YOUR_TOKEN
Content-Type: application/json

{
    "customer_name": "John Doe",
    "item": 1,
    "quantity": 2,
    "status": "pending",
    "delivery_address": "123 Main Street, New York, NY"
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "customer": 1,
    "customer_name": "John Doe",
    "item": 1,
    "item_name": "Margherita Pizza",
    "item_price": "12.99",
    "quantity": 2,
    "total_price": "25.98",
    "status": "pending",
    "status_display": "Pending",
    "delivery_address": "123 Main Street, New York, NY",
    "latitude": null,
    "longitude": null,
    "created_at": "2024-01-01 12:00:00",
    "updated_at": "2024-01-01 12:00:00"
}
```

### Filter Orders by Status

```http
GET /api/orders/?status=pending
Authorization: Token YOUR_TOKEN
```

### Validation Error (Price <= 0)

```http
POST /api/menu-items/
Authorization: Token YOUR_TOKEN
Content-Type: application/json

{
    "name": "Free Item",
    "price": -5.00,
    "category": 1
}
```

**Response (400 Bad Request):**
```json
{
    "price": ["Price must be greater than zero."]
}
```

### Unauthenticated Request

```http
GET /api/orders/
```

**Response (401 Unauthorized):**
```json
{
    "detail": "Authentication credentials were not provided."
}
```

---

## 🧪 Testing

Run the test suite:

```bash
python manage.py test api
```

Test coverage includes:
- Category API (list, retrieve, not found)
- MenuItem CRUD (create, read, update, delete)
- Price validation (price > 0)
- Order API (create, list, filter)
- Authentication (401 for unauthenticated)
- Object-level permissions (users see own orders only)
- Quantity validation (quantity > 0)

---

## 📊 HTTP Status Codes Used

| Code | Meaning | Usage |
|---|---|---|
| `200` | OK | Successful GET, PUT, PATCH |
| `201` | Created | Successful POST |
| `204` | No Content | Successful DELETE |
| `400` | Bad Request | Validation errors |
| `401` | Unauthorized | Unauthenticated request |
| `403` | Forbidden | Permission denied |
| `404` | Not Found | Resource not found |

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Django 4.2**
- **Django REST Framework**
- **django-filter** (Query Filtering)
- **requests** (Google Maps API)
- **Pillow** (Image Processing)
- **SQLite** (Database)

---

## 👨‍💻 Author

M5 Django REST Framework Assessment Project

---

*Built with ❤️ using Django REST Framework*
