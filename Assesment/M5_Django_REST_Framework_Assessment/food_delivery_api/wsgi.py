"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api
WSGI Configuration
====================================================
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_delivery_api.settings')
application = get_wsgi_application()
