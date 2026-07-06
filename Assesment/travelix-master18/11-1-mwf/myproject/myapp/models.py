from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    usertype = models.CharField(max_length=30, default="customer")
    

    def __str__(self):
        return f"{self.name}"

class Car(models.Model):
    # Agency relationship
    agency = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'usertype': 'agency'})
    
    # Basic Information
    car_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model_year = models.IntegerField()
    plate_number = models.CharField(max_length=20, unique=True)
    
    # Pricing
    price_per_hour = models.IntegerField()
    price_per_day = models.IntegerField()
    
    # Capacity & Specs
    SEAT_CHOICES = [(4, '4'), (5, '5'), (7, '7'), (9, '9')]
    seats = models.IntegerField(choices=SEAT_CHOICES)
    
    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('CNG', 'CNG'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    
    TRANS_CHOICES = [('Manual', 'Manual'), ('Automatic', 'Automatic')]
    transmission = models.CharField(max_length=20, choices=TRANS_CHOICES)
    
    # Features
    has_ac = models.BooleanField(default=False)
    has_airbags = models.BooleanField(default=False)
    has_abs = models.BooleanField(default=False)
    has_gps = models.BooleanField(default=False)
    has_music_system = models.BooleanField(default=False)
    has_reverse_camera = models.BooleanField(default=False)
    
    # Safety
    airbags_count = models.IntegerField(default=0)
    tyre_condition = models.CharField(max_length=50)
    
    # Media
    car_image = models.ImageField(upload_to='cars/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.brand} {self.car_name} ({self.plate_number})"

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.car.car_name}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pickup_time = models.DateTimeField()
    return_time = models.DateTimeField()
    rental_days = models.IntegerField()
    total_amount = models.IntegerField()
    booking_id = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.booking_id} by {self.user.name}"

class Payment(models.Model):
    STATUS_CHOICES = [
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
        ('PENDING', 'Pending'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=50, unique=True)
    payment_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SUCCESS')
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.payment_id} for Booking {self.booking.booking_id}"
