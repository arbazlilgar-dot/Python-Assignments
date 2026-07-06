from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('book-appointment/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('payment/<int:appointment_id>/', views.payment, name='payment'),
    path('payment/process/<int:appointment_id>/', views.process_payment, name='process_payment'),
    
    # Custom Website Admin Endpoints
    path('website-admin/login/', views.website_admin_login, name='website_admin_login'),
    path('website-admin/dashboard/', views.website_admin_dashboard, name='website_admin_dashboard'),
    path('website-admin/logout/', views.website_admin_logout, name='website_admin_logout'),
    
    # AJAX Endpoints for CRUD
    path('ajax/doctors/add/', views.ajax_add_doctor, name='ajax_add_doctor'),
    path('ajax/doctors/update/<int:pk>/', views.ajax_update_doctor, name='ajax_update_doctor'),
    path('ajax/doctors/delete/<int:pk>/', views.ajax_delete_doctor, name='ajax_delete_doctor'),
]
