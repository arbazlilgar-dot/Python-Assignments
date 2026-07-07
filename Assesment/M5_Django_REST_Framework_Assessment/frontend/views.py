from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')

def login_view(request):
    return render(request, 'frontend/login.html')

def register_view(request):
    return render(request, 'frontend/register.html')

def dashboard(request):
    return render(request, 'frontend/dashboard.html')

def categories(request):
    return render(request, 'frontend/categories.html')

def menu_items(request):
    return render(request, 'frontend/menu_items.html')

def orders(request):
    return render(request, 'frontend/orders.html')

def profile(request):
    return render(request, 'frontend/profile.html')
