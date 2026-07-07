"""
====================================================
M5 Django REST Framework Assessment
Project: food_delivery_api
Application: api

Admin Configuration
====================================================

This module configures the Django Admin interface for:
- Category: Manage food categories
- MenuItem: Manage menu items
- Order: Manage customer orders

Admin is customized with:
- List display columns
- Search functionality
- Filter sidebars
- Ordering
====================================================
"""

from django.contrib import admin
from .models import Category, MenuItem, Order


# ====================================================
# CATEGORY ADMIN
# ====================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for the Category model."""

    list_display = ['id', 'name', 'description', 'menu_items_count', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'description']
    ordering = ['name']
    readonly_fields = ['created_at', 'updated_at']

    def menu_items_count(self, obj):
        """Display the number of menu items in this category."""
        return obj.menu_items.count()
    menu_items_count.short_description = 'Menu Items'


# ====================================================
# MENUITEM ADMIN
# ====================================================

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Admin configuration for the MenuItem model."""

    list_display = ['id', 'name', 'price', 'category', 'is_available', 'order_count', 'created_at']
    list_display_links = ['id', 'name']
    list_filter = ['category', 'is_available']
    search_fields = ['name', 'description']
    list_editable = ['is_available', 'price']
    ordering = ['category', 'name']
    readonly_fields = ['created_at', 'updated_at']

    def order_count(self, obj):
        """Display the number of orders for this item."""
        return obj.orders.count()
    order_count.short_description = 'Orders'


# ====================================================
# ORDER ADMIN
# ====================================================

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin configuration for the Order model."""

    list_display = [
        'id', 'customer_name', 'customer', 'item',
        'quantity', 'total_price_display', 'status', 'created_at'
    ]
    list_display_links = ['id', 'customer_name']
    list_filter = ['status', 'created_at']
    search_fields = ['customer_name', 'customer__username', 'item__name', 'delivery_address']
    list_editable = ['status']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at', 'latitude', 'longitude']

    fieldsets = (
        ('Customer Information', {
            'fields': ('customer', 'customer_name')
        }),
        ('Order Details', {
            'fields': ('item', 'quantity', 'status')
        }),
        ('Delivery Information', {
            'fields': ('delivery_address', 'latitude', 'longitude')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def total_price_display(self, obj):
        """Display the total price for this order."""
        return f"${obj.total_price}"
    total_price_display.short_description = 'Total Price'


# ====================================================
# ADMIN SITE CUSTOMIZATION
# ====================================================
# Customize the admin site header and title

admin.site.site_header = '🍕 Food Delivery API - Admin'
admin.site.site_title = 'Food Delivery API Admin'
admin.site.index_title = 'API Management Dashboard'
