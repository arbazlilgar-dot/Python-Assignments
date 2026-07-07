"""
====================================================
M5 Django REST Framework Assessment
Application: api
App Configuration
====================================================
"""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Configuration class for the Food Delivery API application.
    Sets the default auto field and application name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    verbose_name = 'Food Delivery API'

    def ready(self):
        """
        Perform initialization tasks when the app is ready.
        This method is called once when Django starts.
        """
        pass
