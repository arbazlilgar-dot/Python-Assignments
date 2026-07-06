from django.contrib import admin
from .models import Doctor, Patient, Appointment, Payment

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'phone', 'consultation_fee')
    search_fields = ('name', 'specialization', 'location')
    list_filter = ('specialization',)
    ordering = ('name',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('gender',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'status', 'payment_status')
    search_fields = ('patient__name', 'doctor__name')
    list_filter = ('status', 'payment_status', 'date')
    ordering = ('-date', '-time')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'amount', 'transaction_id', 'status', 'method')
    search_fields = ('transaction_id', 'appointment__patient__name')
    list_filter = ('status', 'method')
