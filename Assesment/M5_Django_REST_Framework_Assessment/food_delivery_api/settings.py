"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api
Application: api

Django Settings Configuration
====================================================

This settings file configures:
- Installed Apps (Django, DRF, django-filter, api)
- REST Framework (Authentication, Pagination, Filtering)
- Static & Media Files
- Templates
- Database (SQLite)
- Security Settings

Assessment Concepts Covered:
- Question 1: REST Statelessness (stateless token-based auth)
- Question 4: PageNumberPagination (PAGE_SIZE = 5)
- Question 5: Filtering (DjangoFilterBackend)
- Question 6: Authentication (TokenAuthentication)
====================================================
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# ====================================================
# BASE DIRECTORY
# ====================================================
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, '.env'))

# ====================================================
# SECURITY SETTINGS
# ====================================================
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

# ====================================================
# INSTALLED APPLICATIONS
# ====================================================
# Includes Django defaults, DRF, django-filter, and our custom 'api' app
INSTALLED_APPS = [
    # Django Default Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-Party Apps
    'rest_framework',              # Django REST Framework
    'rest_framework.authtoken',    # Token Authentication (Question 6 - Authentication)
    'django_filters',              # Django Filter Backend (Question 5 - Filtering)

    # Project Apps
    'api',                         # Food Delivery API Application
    'frontend',                    # Frontend UI Application
]


# ====================================================
# MIDDLEWARE
# ====================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ====================================================
# URL CONFIGURATION
# ====================================================
ROOT_URLCONF = 'food_delivery_api.urls'


# ====================================================
# TEMPLATES CONFIGURATION
# ====================================================
# Configured to find templates in the api/templates directory
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ====================================================
# WSGI CONFIGURATION
# ====================================================
WSGI_APPLICATION = 'food_delivery_api.wsgi.application'


# ====================================================
# DATABASE CONFIGURATION
# ====================================================
# Using SQLite for assessment purposes
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ====================================================
# PASSWORD VALIDATION
# ====================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ====================================================
# INTERNATIONALIZATION
# ====================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ====================================================
# STATIC FILES CONFIGURATION
# ====================================================
# URL prefix for static files
STATIC_URL = '/static/'

# Directory where collectstatic will gather all static files
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Additional directories for static files
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# ====================================================
# MEDIA FILES CONFIGURATION
# ====================================================
# URL prefix for media files (user uploads)
MEDIA_URL = '/media/'

# Directory for uploaded media files
MEDIA_ROOT = BASE_DIR / 'media'


# ====================================================
# DEFAULT PRIMARY KEY FIELD TYPE
# ====================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ====================================================
# DJANGO REST FRAMEWORK CONFIGURATION
# ====================================================
# This section configures DRF globally for:
# - Authentication: TokenAuthentication (Question 6)
# - Permissions: IsAuthenticated by default (Question 6)
# - Pagination: PageNumberPagination with PAGE_SIZE=5 (Question 4)
# - Filtering: DjangoFilterBackend (Question 5)
# - Browsable API: Custom renderer for premium UI
REST_FRAMEWORK = {
    # Question 1 - REST Statelessness
    # Token-based authentication ensures stateless communication.
    # Each request carries its own authentication token.
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],

    # Question 6 - Authentication & Authorization
    # All API endpoints require authentication by default.
    # Individual views can override this with permission_classes.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    # Question 4 - PageNumberPagination
    # Configures global pagination with PAGE_SIZE = 5
    'DEFAULT_PAGINATION_CLASS': 'api.pagination.StandardPageNumberPagination',
    'PAGE_SIZE': 5,

    # Question 5 - Filtering
    # Enables DjangoFilterBackend globally for query filtering
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],

    # Browsable API Renderer + JSON
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],

    # Date/Time formatting
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DATE_FORMAT': '%Y-%m-%d',
}


# ====================================================
# GOOGLE MAPS API CONFIGURATION
# ====================================================
# Question 6 - Google Maps Geocoding API Integration
# Replace with your actual Google Maps API key for geocoding
GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', 'YOUR_GOOGLE_MAPS_API_KEY_HERE')
