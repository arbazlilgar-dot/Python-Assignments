"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api
Application: api

Custom Permissions
====================================================

This module defines custom permission classes:
- IsOwnerOrAdmin: Object-level permission for order access

Assessment Concepts Covered:
- Question 5: Object Level Permission
  Users must access only their own orders.
  Admin users can access all orders.
- Question 6: Authorization
  Combined with IsAuthenticated to protect API endpoints.
====================================================
"""

from rest_framework import permissions


# ====================================================
# QUESTION 5 - OBJECT LEVEL PERMISSION
# ====================================================
# This permission class ensures that:
# - Users can only view/edit their OWN orders
# - Admin users can view/edit ALL orders
# - This is checked at the object level (per-instance)

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Object-Level Permission - Question 5

    Custom permission to only allow owners of an order to access it.
    Admin users (is_staff=True) can access any order.

    Assessment Concept: Question 5 - Object Level Permission
    - has_permission(): Checks if user is authenticated (view-level)
    - has_object_permission(): Checks if user owns the object (object-level)

    Usage:
        permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    Behavior:
        - Authenticated owner → ALLOWED
        - Authenticated admin → ALLOWED
        - Authenticated non-owner → DENIED (HTTP 403)
        - Unauthenticated → DENIED (HTTP 401)
    """

    def has_permission(self, request, view):
        """
        View-level permission check.
        Only authenticated users can access the view.

        Assessment Concept: Question 6 - Authentication
        """
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Object-level permission check.
        Only the owner of the order or an admin can access it.

        Assessment Concept: Question 5 - Object Level Permission
        - Checks if the requesting user is the owner of the order
        - Admin users (is_staff) bypass this check
        """
        # Admin users can access any order
        if request.user.is_staff:
            return True

        # Regular users can only access their own orders
        return obj.customer == request.user
