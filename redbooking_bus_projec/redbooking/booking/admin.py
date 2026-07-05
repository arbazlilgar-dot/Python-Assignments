from django.contrib import admin
from .models import City, BusOperator, Route, Seat, BoardingPoint, DroppingPoint, Booking, Offer


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    search_fields = ('name', 'state')


@admin.register(BusOperator)
class BusOperatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bus_type', 'rating', 'total_ratings')
    search_fields = ('name',)


class SeatInline(admin.TabularInline):
    model = Seat
    extra = 0


class BoardingPointInline(admin.TabularInline):
    model = BoardingPoint
    extra = 0


class DroppingPointInline(admin.TabularInline):
    model = DroppingPoint
    extra = 0


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('from_city', 'to_city', 'operator', 'departure_time', 'price', 'seats_available')
    list_filter = ('from_city', 'to_city', 'is_active')
    inlines = [SeatInline, BoardingPointInline, DroppingPointInline]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('pnr', 'user', 'route', 'status', 'total_amount', 'booked_on')
    list_filter = ('status',)
    search_fields = ('pnr', 'passenger_name', 'passenger_email')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'badge', 'color_class')
