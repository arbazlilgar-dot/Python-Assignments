import os
import django
import urllib.request
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctor_finder.settings')
django.setup()

from doctor.models import Doctor, WebsiteAdmin
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# 1. Create WebsiteAdmin
admin_email = "arbaz@doctor.in"
admin_pass = "Arbaz@123"

if not WebsiteAdmin.objects.filter(email=admin_email).exists():
    WebsiteAdmin.objects.create(email=admin_email, password=make_password(admin_pass))
    print(f"Created Custom Website Admin: {admin_email}")

# 2. Clear old doctors to ensure uniqueness
Doctor.objects.all().delete()
print("Cleared old doctors.")

# 3. Create 8-10 Unique Indian Doctors
doctors_data = [
    {
        "name": "Ramesh Patel", "specialization": "Cardiologist", "city": "Ahmedabad", "state": "Gujarat",
        "hospital": "Apollo Hospital", "clinic_address": "Apollo Health City, Bhat, Ahmedabad",
        "phone": "9876543001", "email": "ramesh.patel@apollo.in", "fee": 1500.00,
        "days": "Mon - Fri", "time": "09:00 AM - 04:00 PM",
        "rating": 4.9, "languages": "Gujarati, Hindi, English",
        "desc": "Dr. Ramesh Patel is a highly experienced Cardiologist with a track record of performing over 1,000 successful heart surgeries. He specializes in interventional cardiology and preventative heart care.",
        "qual": "MBBS, MD, DM (Cardiology)", "exp": 20,
        "awards": "Best Cardiologist in Gujarat 2024",
        "education": "MD from AIIMS, Delhi (2004)\nDM from CMC Vellore (2008)",
        "services": "Heart Surgery\nAngioplasty\nECG\nEchocardiography",
        "img_url": "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=400&q=80"
    },
    {
        "name": "Priya Sharma", "specialization": "Dermatologist", "city": "Mumbai", "state": "Maharashtra",
        "hospital": "Kokilaben Hospital", "clinic_address": "Rao Saheb Achutrao Patwardhan Marg, Andheri West, Mumbai",
        "phone": "9876543002", "email": "priya.sharma@kokilaben.in", "fee": 1200.00,
        "days": "Tue - Sat", "time": "10:00 AM - 06:00 PM",
        "rating": 4.8, "languages": "Marathi, Hindi, English",
        "desc": "Dr. Priya Sharma is a renowned Dermatologist in Mumbai, offering advanced skin care treatments, laser therapies, and anti-aging solutions. She believes in holistic skincare.",
        "qual": "MBBS, MD (Dermatology)", "exp": 12,
        "awards": "Excellence in Clinical Dermatology 2023",
        "education": "MBBS from KEM Hospital, Mumbai (2010)\nMD from Grant Medical College (2014)",
        "services": "Acne Treatment\nLaser Hair Removal\nChemical Peels\nSkin Biopsy",
        "img_url": "https://images.unsplash.com/photo-1594824432258-00c73d9e3650?w=400&q=80"
    },
    {
        "name": "Vikram Singh", "specialization": "Orthopedic", "city": "Delhi", "state": "Delhi",
        "hospital": "AIIMS", "clinic_address": "Sri Aurobindo Marg, Ansari Nagar, New Delhi",
        "phone": "9876543003", "email": "vikram.singh@aiims.edu.in", "fee": 500.00,
        "days": "Mon - Wed, Fri", "time": "08:00 AM - 02:00 PM",
        "rating": 4.7, "languages": "Hindi, English, Punjabi",
        "desc": "Dr. Vikram Singh is a senior Orthopedic surgeon at AIIMS, specializing in joint replacements, sports injuries, and complex fracture management.",
        "qual": "MBBS, MS (Orthopedics)", "exp": 18,
        "awards": "AIIMS Best Faculty Award 2021",
        "education": "MBBS from MAMC, Delhi (2006)\nMS from AIIMS, Delhi (2010)",
        "services": "Knee Replacement\nHip Replacement\nFracture Treatment\nArthroscopy",
        "img_url": "https://images.unsplash.com/photo-1537368910025-700350fe46c7?w=400&q=80"
    },
    {
        "name": "Ananya Reddy", "specialization": "Neurologist", "city": "Hyderabad", "state": "Telangana",
        "hospital": "Apollo Hospital", "clinic_address": "Jubilee Hills, Hyderabad",
        "phone": "9876543004", "email": "ananya.reddy@apollo.in", "fee": 1500.00,
        "days": "Mon - Thu", "time": "11:00 AM - 05:00 PM",
        "rating": 4.9, "languages": "Telugu, Hindi, English",
        "desc": "Dr. Ananya Reddy is a leading Neurologist with deep expertise in treating epilepsy, stroke, and Parkinson's disease. She runs advanced research programs in neuro-rehabilitation.",
        "qual": "MBBS, MD, DM (Neurology)", "exp": 15,
        "awards": "Top Neuro-physician South India 2025",
        "education": "MD from Osmania Medical College (2009)\nDM from NIMHANS (2013)",
        "services": "Stroke Management\nEpilepsy Treatment\nMigraine Care\nEEG",
        "img_url": "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=400&q=80"
    },
    {
        "name": "Arjun Menon", "specialization": "Pediatrician", "city": "Bengaluru", "state": "Karnataka",
        "hospital": "Manipal Hospital", "clinic_address": "Old Airport Road, Bengaluru",
        "phone": "9876543005", "email": "arjun.menon@manipal.in", "fee": 800.00,
        "days": "Mon - Sat", "time": "09:00 AM - 01:00 PM",
        "rating": 4.6, "languages": "Kannada, Malayalam, English",
        "desc": "Dr. Arjun Menon is a friendly and compassionate Pediatrician dedicated to children's health, vaccinations, and developmental monitoring from infancy to adolescence.",
        "qual": "MBBS, MD (Pediatrics)", "exp": 10,
        "awards": "Best Pediatrician Award 2022",
        "education": "MBBS from St John's Medical College (2014)",
        "services": "Vaccination\nChildhood Nutrition\nNewborn Care\nFever Treatment",
        "img_url": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?w=400&q=80"
    },
    {
        "name": "Neha Gupta", "specialization": "Gynecologist", "city": "Pune", "state": "Maharashtra",
        "hospital": "Max Healthcare", "clinic_address": "Bund Garden Road, Pune",
        "phone": "9876543006", "email": "neha.gupta@max.in", "fee": 1000.00,
        "days": "Mon, Wed, Fri", "time": "04:00 PM - 08:00 PM",
        "rating": 4.8, "languages": "Marathi, Hindi, English",
        "desc": "Dr. Neha Gupta focuses on women's health, high-risk pregnancies, and minimally invasive gynecological surgeries. She is known for her patient-centric approach.",
        "qual": "MBBS, MS (OBG)", "exp": 14,
        "awards": "Women in Medicine 2024",
        "education": "MBBS from BJ Medical College (2010)",
        "services": "Prenatal Care\nHigh-Risk Pregnancy\nLaparoscopy\nUltrasound",
        "img_url": "https://images.unsplash.com/photo-1651008376811-b90baee60c1f?w=400&q=80"
    },
    {
        "name": "Sanjay Verma", "specialization": "ENT Specialist", "city": "Jaipur", "state": "Rajasthan",
        "hospital": "Fortis Hospital", "clinic_address": "JLN Marg, Malviya Nagar, Jaipur",
        "phone": "9876543007", "email": "sanjay.verma@fortis.in", "fee": 700.00,
        "days": "Tue - Sun", "time": "10:00 AM - 02:00 PM",
        "rating": 4.5, "languages": "Hindi, English",
        "desc": "Dr. Sanjay Verma treats disorders of the ear, nose, and throat with precision. He has performed numerous successful sinus and cochlear implant surgeries.",
        "qual": "MBBS, MS (ENT)", "exp": 9,
        "awards": "",
        "education": "MS from SMS Medical College, Jaipur (2017)",
        "services": "Sinus Surgery\nHearing Aids\nTonsillectomy\nThyroid Treatment",
        "img_url": "https://images.unsplash.com/photo-1612349317208-569614742a78?w=400&q=80"
    },
    {
        "name": "Deepa Nambiar", "specialization": "Ophthalmologist", "city": "Chennai", "state": "Tamil Nadu",
        "hospital": "Apollo Hospital", "clinic_address": "Greams Road, Chennai",
        "phone": "9876543008", "email": "deepa.nambiar@apollo.in", "fee": 1000.00,
        "days": "Mon - Fri", "time": "09:00 AM - 03:00 PM",
        "rating": 4.9, "languages": "Tamil, English",
        "desc": "Dr. Deepa Nambiar is a pioneer in LASIK and cataract surgery. She uses state-of-the-art technology to ensure optimal vision correction for her patients.",
        "qual": "MBBS, DO, DNB", "exp": 16,
        "awards": "Visionary Eye Care Award 2020",
        "education": "MBBS from Madras Medical College (2008)",
        "services": "LASIK Surgery\nCataract Surgery\nGlaucoma Treatment\nEye Exams",
        "img_url": "https://images.unsplash.com/photo-1590611936760-eeb9bc598548?w=400&q=80"
    },
]

for d in doctors_data:
    doc = Doctor(
        name=d['name'], specialization=d['specialization'], city=d['city'], state=d['state'],
        hospital=d['hospital'], clinic_address=d['clinic_address'], phone=d['phone'],
        email=d['email'], consultation_fee=d['fee'], available_days=d['days'],
        available_time=d['time'], rating=d['rating'], languages_spoken=d['languages'],
        description=d['desc'], qualification=d['qual'], experience=d['exp'],
        awards=d['awards'], education_timeline=d['education'], services_offered=d['services'],
        location=d['city'] # mapping location to city for map
    )
    
    # Download image
    try:
        req = urllib.request.Request(d['img_url'], headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        filename = d['name'].replace(' ', '_').lower() + '.jpg'
        doc.profile_image.save(filename, ContentFile(response.read()), save=False)
    except Exception as e:
        print(f"Could not fetch image for {d['name']}: {e}")
        
    doc.save()
    print(f"Created Dr. {d['name']}")

print("Database population complete!")
