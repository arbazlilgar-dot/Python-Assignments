import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctor_finder.settings')
django.setup()

from django.contrib.auth.models import User
from doctor.models import Doctor

# Create Superuser if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Created superuser: admin / admin123")

# Create some dummy doctors if none exist
if not Doctor.objects.exists():
    Doctor.objects.create(
        name="John Doe",
        specialization="Cardiologist",
        qualification="MBBS, MD",
        experience=10,
        hospital="City Heart Hospital",
        clinic_address="123 Heart Avenue, New York",
        phone="9876543210",
        email="johndoe@example.com",
        available_days="Mon - Fri",
        available_time="10:00 AM - 04:00 PM",
        consultation_fee=500.00,
        location="New York",
        description="Expert Cardiologist with 10 years of experience in performing open heart surgeries."
    )
    Doctor.objects.create(
        name="Jane Smith",
        specialization="Dermatologist",
        qualification="MBBS, MD",
        experience=8,
        hospital="Skin Care Clinic",
        clinic_address="456 Skin Street, London",
        phone="9876543211",
        email="janesmith@example.com",
        available_days="Tue - Sat",
        available_time="09:00 AM - 05:00 PM",
        consultation_fee=400.00,
        location="London",
        description="Specialist in skincare, acne treatment, and laser therapy."
    )
    print("Created dummy doctors.")
else:
    print("Dummy doctors already exist.")
