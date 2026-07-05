from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='home_index'),        # /index bhi chalega
    path('index.html', views.home, name='home_html'),     # /index.html bhi chalega
    path('listing/', views.bus_listing, name='bus_listing'),
    path('seats/<int:route_id>/', views.seat_selection, name='seat_selection'),
    path('booking/<int:route_id>/', views.booking_details, name='booking_details'),
    path('payment/<int:route_id>/', views.payment, name='payment'),
    path('auth/', views.auth_page, name='auth_page'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]
