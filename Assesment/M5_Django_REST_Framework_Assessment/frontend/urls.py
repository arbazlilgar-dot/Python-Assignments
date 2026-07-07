from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('menu-items/', views.menu_items, name='menu_items'),
    path('orders/', views.orders, name='orders'),
    path('profile/', views.profile, name='profile'),
]
