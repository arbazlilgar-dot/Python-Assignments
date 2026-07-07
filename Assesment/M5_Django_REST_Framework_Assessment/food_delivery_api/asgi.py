"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api
ASGI Configuration
====================================================
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_delivery_api.settings')
application = get_asgi_application()
