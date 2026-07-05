from django.db import models
from django.contrib.auth.models import User
import random
import string


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['name']

    def __str__(self):
        return f"{self.name}, {self.state}"


class BusOperator(models.Model):
    name = models.CharField(max_length=200)
    bus_type = models.CharField(max_length=200)  # e.g. "Volvo A/C Sleeper (2+1)"
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.0)
    total_ratings = models.CharField(max_length=50, default="0 ratings")
    amenities = models.CharField(max_length=500, blank=True, default="")  # comma separated

    def __str__(self):
        return f"{self.name} - {self.bus_type}"


class Route(models.Model):
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='routes_from')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='routes_to')
    operator = models.ForeignKey(BusOperator, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    duration = models.IntegerField(help_text="Duration in minutes")
    stops = models.CharField(max_length=50, default="Non-stop")
    price = models.IntegerField()
    seats_available = models.IntegerField(default=30)
    bus_type_tags = models.CharField(max_length=200, default="ac sleeper")  # for filtering
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.from_city.name} → {self.to_city.name} | {self.operator.name} | ₹{self.price}"

    @property
    def duration_display(self):
        hours = self.duration // 60
        mins = self.duration % 60
        return f"{hours}h {mins:02d}m"


class Seat(models.Model):
    SEAT_STATUS = [
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('female', 'Female Booked'),
    ]
    SEAT_TIER = [
        ('standard', 'Standard'),
        ('window', 'Window'),
        ('upper', 'Upper Deck'),
        ('premium', 'Premium Upper'),
    ]

    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    deck = models.CharField(max_length=10, choices=[('lower', 'Lower'), ('upper', 'Upper')], default='lower')
    status = models.CharField(max_length=20, choices=SEAT_STATUS, default='available')
    tier = models.CharField(max_length=20, choices=SEAT_TIER, default='standard')
    price = models.IntegerField(default=0)

    class Meta:
        unique_together = ('route', 'seat_number')
        ordering = ['seat_number']

    def __str__(self):
        return f"{self.seat_number} - {self.status} - ₹{self.price}"


class BoardingPoint(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='boarding_points')
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.time}"


class DroppingPoint(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='dropping_points')
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.time}"


class Booking(models.Model):
    BOOKING_STATUS = [
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    pnr = models.CharField(max_length=20, unique=True, blank=True)
    seats = models.ManyToManyField(Seat)
    boarding_point = models.ForeignKey(BoardingPoint, on_delete=models.SET_NULL, null=True, blank=True)
    dropping_point = models.ForeignKey(DroppingPoint, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=BOOKING_STATUS, default='confirmed')
    passenger_name = models.CharField(max_length=200)
    passenger_email = models.CharField(max_length=200)
    passenger_phone = models.CharField(max_length=20)
    total_amount = models.IntegerField(default=0)
    booked_on = models.DateTimeField(auto_now_add=True)
    travel_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pnr:
            self.pnr = 'RB' + ''.join(random.choices(string.digits, k=8))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"PNR: {self.pnr} | {self.route} | {self.status}"


class Offer(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    badge = models.CharField(max_length=50, default="Limited time")
    color_class = models.CharField(max_length=50, default="offer-1")

    def __str__(self):
        return f"{self.code} - {self.title}"
