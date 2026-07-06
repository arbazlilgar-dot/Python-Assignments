from django.urls import path
from myapp import views

urlpatterns = [
      path('', views.index, name='index'),
      path('signup/', views.signup, name='signup'),
      path('login/', views.login, name='login'),
      path('logout/', views.logout, name='logout'),
      path('forgot-password/', views.forgot_password, name='forgot_password'),
      path('verify-otp/', views.verify_otp, name='verify_otp'),
      path('new-password/', views.new_password, name='new_password'),
      path('update-profile/', views.update_profile, name='update_profile'),
      
      # User URLs
      path('car-rentals/', views.car_rentals, name='car_rentals'),
      path('car-details/<int:pk>/', views.car_details, name='car_details'),
      path('payment/<int:pk>/', views.payment, name='payment'),
      path('edit-car/<int:pk>/', views.edit_car, name='edit_car'),
      path('delete-car/<int:pk>/', views.delete_car, name='delete_car'),
      
      # Wishlist URLs
      path('add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
      path('show-wishlist/', views.show_wishlist, name='show_wishlist'),
      path('remove-from-wishlist/<int:pk>/', views.remove_from_wishlist, name='remove_from_wishlist'),
      
      # Booking & Payment URLs
      path('process-payment/', views.process_payment, name='process_payment'),
      path('my-orders/', views.my_orders, name='my_orders'),
      path('booking-details/<int:pk>/', views.booking_details, name='booking_details'),
      path('cancel-booking/<int:pk>/', views.cancel_booking, name='cancel_booking'),
      path('download-invoice/<int:pk>/', views.download_invoice, name='download_invoice'),
]
