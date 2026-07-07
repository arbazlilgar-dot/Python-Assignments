"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api
Application: api

Pagination Classes
====================================================

This module defines custom pagination classes:
- StandardPageNumberPagination: Page-based pagination (PAGE_SIZE=5)
- OrderCursorPagination: Cursor-based pagination for orders

Assessment Concepts Covered:
- Question 4: PageNumberPagination (PAGE_SIZE = 5)
- Question 4: CursorPagination (alternative pagination style)
====================================================
"""

from rest_framework.pagination import PageNumberPagination, CursorPagination


# ====================================================
# QUESTION 4 - PAGE NUMBER PAGINATION
# ====================================================
# Configured as the default pagination class in settings.py
# PAGE_SIZE = 5 as required by the assessment

class StandardPageNumberPagination(PageNumberPagination):
    """
    Standard Page Number Pagination - Question 4

    Implements PageNumberPagination with PAGE_SIZE = 5.
    This is the default pagination class configured in settings.py.

    Assessment Concept: Question 4 - PageNumberPagination
    - PAGE_SIZE = 5 (returns 5 items per page)
    - Supports ?page=N query parameter
    - Supports ?page_size=N to override default (max 50)
    - Returns count, next, previous, and results in response

    Example Response:
    {
        "count": 15,
        "next": "http://localhost:8000/api/orders/?page=2",
        "previous": null,
        "results": [...]  // 5 items
    }

    Usage:
        GET /api/orders/            → Page 1 (items 1-5)
        GET /api/orders/?page=2     → Page 2 (items 6-10)
        GET /api/orders/?page=3     → Page 3 (items 11-15)
    """

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'page'


# ====================================================
# QUESTION 4 - CURSOR PAGINATION
# ====================================================
# Alternative pagination style using opaque cursors
# Useful for real-time data where items may be added/removed

class OrderCursorPagination(CursorPagination):
    """
    Cursor-Based Pagination for Orders - Question 4

    Implements CursorPagination as an alternative pagination style.
    Uses opaque cursors instead of page numbers.

    Assessment Concept: Question 4 - CursorPagination
    - page_size = 5 (returns 5 items per page)
    - Ordering by '-created_at' (newest first)
    - Uses cursor tokens instead of page numbers
    - More efficient for large datasets
    - Prevents issues with items being added/removed during pagination

    Usage:
        GET /api/orders/?cursor=<opaque_token>

    Note: This class is available for demonstration purposes.
    The default pagination uses PageNumberPagination.
    """

    page_size = 5
    ordering = '-created_at'
    cursor_query_param = 'cursor'
