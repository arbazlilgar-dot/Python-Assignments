import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Doctor, Patient, Appointment, Payment
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.hashers import check_password

def home(request):
    featured_doctors = Doctor.objects.all()[:4]
    return render(request, 'home.html', {'featured_doctors': featured_doctors})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def doctor_list(request):
    query = request.GET.get('q')
    specialization = request.GET.get('specialization')
    city = request.GET.get('city')
    hospital = request.GET.get('hospital')
    fee_max = request.GET.get('fee_max')
    
    doctors = Doctor.objects.all()
    if query:
        doctors = doctors.filter(Q(name__icontains=query) | Q(specialization__icontains=query))
    if specialization:
        doctors = doctors.filter(specialization__icontains=specialization)
    if city:
        doctors = doctors.filter(city__icontains=city)
    if hospital:
        doctors = doctors.filter(hospital__icontains=hospital)
    if fee_max and fee_max.isdigit():
        doctors = doctors.filter(consultation_fee__lte=fee_max)
        
    return render(request, 'doctor_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctor_detail.html', {'doctor': doctor})

def user_login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        e = request.POST.get('email')
        p1 = request.POST.get('password')
        p2 = request.POST.get('confirm_password')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        
        if p1 != p2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')
            
        if User.objects.filter(username=e).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')
            
        user = User.objects.create_user(username=e, email=e, password=p1)
        Patient.objects.create(user=user, name=n, age=age, gender=gender, phone=phone, email=e)
        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')
        
    return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    if request.user.is_superuser:
        appointments = Appointment.objects.all().order_by('-date')
        doctors = Doctor.objects.all()
        return render(request, 'dashboard_admin.html', {'appointments': appointments, 'doctors': doctors})
    else:
        patient = getattr(request.user, 'patient', None)
        if patient:
            appointments = patient.appointments.all().order_by('-date')
            return render(request, 'dashboard_patient.html', {'appointments': appointments, 'patient': patient})
        return redirect('home')

@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.method == 'POST':
        d = request.POST.get('date')
        t = request.POST.get('time')
        patient = request.user.patient
        appointment = Appointment.objects.create(doctor=doctor, patient=patient, date=d, time=t)
        return redirect('payment', appointment_id=appointment.id)
    return render(request, 'book_appointment.html', {'doctor': doctor})

@login_required
def payment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'payment.html', {'appointment': appointment})

@login_required
def process_payment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        Payment.objects.create(
            appointment=appointment,
            amount=appointment.doctor.consultation_fee,
            transaction_id='TXN' + str(appointment.id) + 'DUMMY',
            status='Success'
        )
        appointment.payment_status = True
        appointment.status = 'Confirmed'
        appointment.save()
        messages.success(request, "Payment Successful. Appointment Confirmed!")
        return redirect('dashboard')
    return redirect('home')

# AJAX CRUD for Doctors (Admin only)
@login_required
def ajax_add_doctor(request):
    if request.user.is_superuser and request.method == 'POST':
        try:
            name = request.POST.get('name')
            spec = request.POST.get('specialization')
            qual = request.POST.get('qualification')
            exp = request.POST.get('experience')
            hosp = request.POST.get('hospital')
            addr = request.POST.get('clinic_address')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            days = request.POST.get('available_days')
            time = request.POST.get('available_time')
            fee = request.POST.get('consultation_fee')
            loc = request.POST.get('location')
            desc = request.POST.get('description')
            
            doc = Doctor.objects.create(
                name=name, specialization=spec, qualification=qual, experience=exp,
                hospital=hosp, clinic_address=addr, phone=phone, email=email,
                available_days=days, available_time=time, consultation_fee=fee,
                location=loc, description=desc
            )
            return JsonResponse({'status': 'success', 'id': doc.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Unauthorized'})

@login_required
def ajax_update_doctor(request, pk):
    if request.user.is_superuser and request.method == 'POST':
        try:
            doc = get_object_or_404(Doctor, pk=pk)
            doc.name = request.POST.get('name', doc.name)
            doc.specialization = request.POST.get('specialization', doc.specialization)
            doc.experience = request.POST.get('experience', doc.experience)
            doc.consultation_fee = request.POST.get('consultation_fee', doc.consultation_fee)
            doc.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Unauthorized'})

@login_required
def ajax_delete_doctor(request, pk):
    if request.user.is_superuser and request.method == 'POST':
        doc = get_object_or_404(Doctor, pk=pk)
        doc.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Unauthorized'})

# Custom Website Admin Panel
from .models import WebsiteAdmin
from django.core.paginator import Paginator

def website_admin_login(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('password')
        try:
            admin = WebsiteAdmin.objects.get(email=e)
            if check_password(p, admin.password):
                request.session['website_admin_id'] = admin.id
                return redirect('website_admin_dashboard')
            else:
                messages.error(request, "Invalid Website Admin Credentials")
        except WebsiteAdmin.DoesNotExist:
            messages.error(request, "Invalid Website Admin Credentials")
    return render(request, 'website_admin_login.html')

def website_admin_dashboard(request):
    admin_id = request.session.get('website_admin_id')
    if not admin_id:
        return redirect('website_admin_login')
        
    # Dashboard features: Doctors, Patients, Appointments, Payments
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all().order_by('-date')
    payments = Payment.objects.all()
    
    # Simple pagination for appointments
    paginator = Paginator(appointments, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'doctors_count': doctors.count(),
        'patients_count': patients.count(),
        'appointments_count': appointments.count(),
        'revenue': sum(p.amount for p in payments if p.status == 'Success'),
        'doctors': doctors,
        'page_obj': page_obj
    }
    return render(request, 'website_admin_dashboard.html', context)

def website_admin_logout(request):
    if 'website_admin_id' in request.session:
        del request.session['website_admin_id']
    return redirect('home')

