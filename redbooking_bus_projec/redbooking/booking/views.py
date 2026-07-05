from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import City, BusOperator, Route, Seat, BoardingPoint, DroppingPoint, Booking, Offer
import json
from datetime import date


def home(request):
    """Home page with search, popular routes, offers, features"""
    cities = City.objects.all()
    popular_routes = Route.objects.filter(is_active=True).select_related(
        'from_city', 'to_city', 'operator'
    ).order_by('-operator__rating')[:6]
    offers = Offer.objects.all()[:4]

    context = {
        'cities': cities,
        'popular_routes': popular_routes,
        'offers': offers,
    }
    return render(request, 'booking/index.html', context)


def bus_listing(request):
    """Bus listing page with filters"""
    from_city = request.GET.get('from', '')
    to_city = request.GET.get('to', '')
    travel_date = request.GET.get('date', '')

    routes = Route.objects.filter(is_active=True).select_related(
        'from_city', 'to_city', 'operator'
    )

    if from_city:
        routes = routes.filter(from_city__name__icontains=from_city)
    if to_city:
        routes = routes.filter(to_city__name__icontains=to_city)

    context = {
        'routes': routes,
        'from_city': from_city or 'Bengaluru',
        'to_city': to_city or 'Hyderabad',
        'travel_date': travel_date or str(date.today()),
        'result_count': routes.count(),
    }
    return render(request, 'booking/listing.html', context)


def seat_selection(request, route_id):
    """Seat selection page"""
    route = get_object_or_404(Route, id=route_id)
    seats = route.seats.all()
    boarding_points = route.boarding_points.all()
    dropping_points = route.dropping_points.all()

    lower_seats = seats.filter(deck='lower')
    upper_seats = seats.filter(deck='upper')

    context = {
        'route': route,
        'lower_seats': lower_seats,
        'upper_seats': upper_seats,
        'boarding_points': boarding_points,
        'dropping_points': dropping_points,
    }
    return render(request, 'booking/seats.html', context)


def booking_details(request, route_id):
    """Passenger details / booking form page"""
    route = get_object_or_404(Route, id=route_id)
    selected_seats_param = request.GET.get('seats', '')
    selected_seats = []

    if selected_seats_param:
        seat_numbers = selected_seats_param.split(',')
        selected_seats = Seat.objects.filter(route=route, seat_number__in=seat_numbers)

    base_fare = sum(s.price for s in selected_seats) if selected_seats else route.price * 2
    tax = int(base_fare * 0.05)
    discount = 250
    total = base_fare + tax - discount

    context = {
        'route': route,
        'selected_seats': selected_seats,
        'base_fare': base_fare,
        'tax': tax,
        'discount': discount,
        'total': total,
        'seat_count': len(selected_seats) if selected_seats else 2,
    }
    return render(request, 'booking/booking.html', context)


def payment(request, route_id):
    """Payment page"""
    route = get_object_or_404(Route, id=route_id)
    selected_seats_param = request.GET.get('seats', '')

    selected_seats = []
    if selected_seats_param:
        seat_numbers = selected_seats_param.split(',')
        selected_seats = Seat.objects.filter(route=route, seat_number__in=seat_numbers)

    base_fare = sum(s.price for s in selected_seats) if selected_seats else route.price * 2
    tax = int(base_fare * 0.05)
    discount = 250
    total = base_fare + tax - discount

    if request.method == 'POST':
        if request.user.is_authenticated:
            # Create booking
            booking_obj = Booking.objects.create(
                user=request.user,
                route=route,
                passenger_name=request.POST.get('name', 'Guest'),
                passenger_email=request.POST.get('email', ''),
                passenger_phone=request.POST.get('phone', ''),
                total_amount=total,
                status='confirmed',
                travel_date=date.today(),
            )
            if selected_seats:
                booking_obj.seats.set(selected_seats)
                selected_seats.update(status='booked')
            messages.success(request, f'Booking confirmed! PNR: {booking_obj.pnr}')
            return redirect('my_bookings')
        else:
            messages.warning(request, 'Please login to complete booking.')
            return redirect('auth_page')

    context = {
        'route': route,
        'selected_seats': selected_seats,
        'base_fare': base_fare,
        'tax': tax,
        'discount': discount,
        'total': total,
    }
    return render(request, 'booking/payment.html', context)


def auth_page(request):
    """Login / Signup page"""
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'booking/auth.html')


def login_view(request):
    """Handle login"""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Welcome back!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('auth_page')
    return redirect('auth_page')


def signup_view(request):
    """Handle signup"""
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        password = request.POST.get('password', '')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Account already exists with this email.')
            return redirect('auth_page')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name.split()[0] if name else '',
            last_name=' '.join(name.split()[1:]) if name and len(name.split()) > 1 else '',
        )
        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('home')
    return redirect('auth_page')


def logout_view(request):
    """Handle logout"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def my_bookings(request):
    """My bookings page"""
    user_bookings = Booking.objects.filter(user=request.user).select_related(
        'route', 'route__from_city', 'route__to_city', 'route__operator'
    ).prefetch_related('seats').order_by('-booked_on')

    context = {
        'bookings': user_bookings,
        'total_bookings': user_bookings.count(),
    }
    return render(request, 'booking/bookings.html', context)
