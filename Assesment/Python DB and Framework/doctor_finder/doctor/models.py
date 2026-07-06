from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Years of experience")
    hospital = models.CharField(max_length=150)
    clinic_address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    available_days = models.CharField(max_length=100, help_text="e.g., Monday to Friday")
    available_time = models.CharField(max_length=100, help_text="e.g., 09:00 AM - 05:00 PM")
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    profile_image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    location = models.CharField(max_length=200, help_text="Specific area for map", blank=True, null=True)
    city = models.CharField(max_length=100, default='Mumbai')
    state = models.CharField(max_length=100, default='Maharashtra')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.5)
    languages_spoken = models.CharField(max_length=200, default='English, Hindi')
    awards = models.TextField(blank=True, null=True)
    education_timeline = models.TextField(blank=True, null=True)
    services_offered = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    status_choices = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment: {self.patient.name} with {self.doctor.name} on {self.date}"

class Payment(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status_choices = [
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Failed', 'Failed')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')
    method = models.CharField(max_length=50, default='Dummy Paytm')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Appointment {self.appointment.id} - {self.status}"

class WebsiteAdmin(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

