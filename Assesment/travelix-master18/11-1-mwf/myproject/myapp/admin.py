from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'usertype')

admin.site.register(User, UserAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'brand', 'plate_number', 'price_per_day', 'agency')
    list_filter = ('brand', 'fuel_type', 'transmission', 'agency')
    search_fields = ('car_name', 'brand', 'plate_number')

admin.site.register(Car, CarAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'user', 'car', 'pickup_time', 'return_time', 'total_amount', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('booking_id', 'user__name', 'car__car_name')

admin.site.register(Booking, BookingAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'transaction_id', 'booking', 'user', 'amount', 'payment_method', 'status', 'paid_at')
    list_filter = ('status', 'payment_method', 'paid_at')
    search_fields = ('payment_id', 'transaction_id', 'booking__booking_id', 'user__name')

admin.site.register(Payment, PaymentAdmin)