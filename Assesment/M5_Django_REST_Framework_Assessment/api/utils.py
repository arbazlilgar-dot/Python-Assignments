"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api
Application: api

Utility Functions
====================================================

This module provides utility functions:
- geocode_address(): Google Maps Geocoding API integration

Assessment Concepts Covered:
- Question 6: Google Maps Geocoding API Integration
  Convert delivery addresses to latitude/longitude coordinates.
====================================================
"""

import requests
from django.conf import settings


# ====================================================
# QUESTION 6 - GOOGLE MAPS GEOCODING API INTEGRATION
# ====================================================
# This function calls the Google Maps Geocoding API to convert
# a text address into geographic coordinates (latitude, longitude).

def geocode_address(address):
    """
    Google Maps Geocoding API Integration - Question 6

    Converts a text address into geographic coordinates using
    the Google Maps Geocoding API.

    Assessment Concept: Question 6 - Google Maps Geocoding API
    - Sends HTTP GET request to Google Maps Geocoding API
    - Parses the JSON response to extract lat/lng
    - Returns coordinates or None if geocoding fails
    - Uses the 'requests' library for HTTP communication

    Args:
        address (str): The delivery address to geocode.
                       Example: "1600 Amphitheatre Parkway, Mountain View, CA"

    Returns:
        dict: A dictionary with 'latitude' and 'longitude' keys,
              or None if geocoding fails.

    Example:
        >>> result = geocode_address("1600 Amphitheatre Parkway, Mountain View, CA")
        >>> print(result)
        {'latitude': 37.4224764, 'longitude': -122.0842499, 'formatted_address': '...'}

    Note:
        Requires a valid Google Maps API key in settings.GOOGLE_MAPS_API_KEY
        Set the key via environment variable: GOOGLE_MAPS_API_KEY
    """

    # Get the API key from settings
    api_key = settings.GOOGLE_MAPS_API_KEY

    # Google Maps Geocoding API endpoint
    geocoding_url = 'https://maps.googleapis.com/maps/api/geocode/json'

    # Request parameters
    params = {
        'address': address,
        'key': api_key,
    }

    try:
        # Question 6 - Making HTTP request to external API
        # Using the 'requests' library as specified in requirements
        response = requests.get(geocoding_url, params=params, timeout=10)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        # Check if geocoding was successful
        if data.get('status') == 'OK' and data.get('results'):
            # Extract the first result
            result = data['results'][0]
            location = result['geometry']['location']

            return {
                'latitude': location['lat'],
                'longitude': location['lng'],
                'formatted_address': result.get('formatted_address', address),
            }
        else:
            # Geocoding failed - return None
            return None

    except requests.exceptions.RequestException:
        # Network error or API error - return None
        return None

    except (KeyError, IndexError, ValueError):
        # Parsing error - return None
        return None
