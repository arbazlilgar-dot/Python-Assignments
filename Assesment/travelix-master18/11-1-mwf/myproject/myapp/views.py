from django.shortcuts import render,redirect
from .models import *
import random
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method=="POST":
                return render(request,'signup.html',{'msg':msg})

    else:
        return render(request,'signup.html')


def login(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            print("****************",type(user.password))
            if user.password==request.POST['password']:
                print("*****************gaya he andar!!")
                request.session['email']=user.email
                return redirect('index')
            else:
                msg = "Password does not match!!"
                return render(request,'login.html',{'msg':msg})

        except:
            msg = "Email does not exist!!"
            return render(request,'login.html',{'msg':msg})
    
    else:
        return render(request,'login.html')
    
def logout(request):
    del request.session['email']
    return redirect('login')

def forgot_password(request):
    if request.method == "POST":
        try:
            email = request.POST['email']
            user = User.objects.get(email=email)
            otp = random.randint(1000, 9999)
            request.session['otp'] = otp
            request.session['reset_email'] = email
            
            # Send Email
            subject = 'Password Reset OTP'
            message = f'Your OTP for password reset is: {otp}'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
            
            return redirect('verify_otp')
        except User.DoesNotExist:
            msg = "Email does not exist!!"
            return render(request, 'forgot_password.html', {'msg': msg})
    return render(request, 'forgot_password.html')

def verify_otp(request):
    email = request.session.get('reset_email', '')
    masked_email = email
    if email and '@' in email:
        name, domain = email.split('@')
        if len(name) > 3:
            masked_email = name[:3] + '***@' + domain
        else:
            masked_email = name[0] + '***@' + domain
            
    if request.method == "POST":
        user_otp = request.POST.get('otp', '')
        session_otp = str(request.session.get('otp', ''))
        
        if user_otp == session_otp:
            return redirect('new_password')
        else:
            msg = "Invalid OTP!"
            return render(request, 'verify_otp.html', {'msg': msg, 'masked_email': masked_email, 'email': email})
            
    return render(request, 'verify_otp.html', {'masked_email': masked_email, 'email': email})

def new_password(request):
    if request.method == "POST":
        new_pass = request.POST.get('new_password')
        conf_pass = request.POST.get('cpassword')
        if new_pass == conf_pass:
            email = request.session.get('reset_email')
            user = User.objects.get(email=email)
            user.password = new_pass
            user.save()
            return redirect('login')
        else:
            msg = "Password & confirm password do not match!!"
            return render(request, 'new_password.html', {'msg': msg})
    return render(request, 'new_password.html')

def update_profile(request):
    try:
        user = User.objects.get(email=request.session.get('email'))
    except:
        return redirect('login')
        
from django.shortcuts import render,redirect
from .models import *
import random
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
import uuid
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils.crypto import get_random_string
# Create your views here.

def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method=="POST":
        # Check if email already exists
        if User.objects.filter(email=request.POST['email']).exists():
            msg = "Email already exists!!"
            return render(request,'signup.html',{'msg':msg})
            
        # Check if mobile already exists
        if User.objects.filter(mobile=request.POST['mobile']).exists():
            msg = "Mobile number already exists!!"
            return render(request,'signup.html',{'msg':msg})
            
        if request.POST['password'] == request.POST['cpassword']:
            try:
                User.objects.create(
                    name=request.POST['name'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    password = request.POST['password'],
                    usertype=request.POST.get('usertype', 'customer')
                )
                msg = "Signup Successfully!! Please login."
                return render(request,'signup.html',{'msg':msg})
            except Exception as e:
                msg = f"Error during signup: {str(e)}"
                return render(request,'signup.html',{'msg':msg})
        else:
            msg = "Password & confirm password does not match!!"
            return render(request,'signup.html',{'msg':msg})

    else:
        return render(request,'signup.html')


def login(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            print("****************",type(user.password))
            if user.password==request.POST['password']:
                print("*****************gaya he andar!!")
                request.session['email']=user.email
                request.session['usertype'] = user.usertype
                return redirect('index')
            else:
                msg = "Password does not match!!"
                return render(request,'login.html',{'msg':msg})

        except:
            msg = "Email does not exist!!"
            return render(request,'login.html',{'msg':msg})
    
    else:
        return render(request,'login.html')
    
def logout(request):
    del request.session['email']
    return redirect('login')

def forgot_password(request):
    if request.method == "POST":
        try:
            email = request.POST['email']
            user = User.objects.get(email=email)
            otp = random.randint(1000, 9999)
            request.session['otp'] = otp
            request.session['reset_email'] = email
            
            # Send Email
            subject = 'Password Reset OTP'
            message = f'Your OTP for password reset is: {otp}'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
            
            return redirect('verify_otp')
        except User.DoesNotExist:
            msg = "Email does not exist!!"
            return render(request, 'forgot_password.html', {'msg': msg})
    return render(request, 'forgot_password.html')

def verify_otp(request):
    email = request.session.get('reset_email', '')
    masked_email = email
    if email and '@' in email:
        name, domain = email.split('@')
        if len(name) > 3:
            masked_email = name[:3] + '***@' + domain
        else:
            masked_email = name[0] + '***@' + domain
            
    if request.method == "POST":
        user_otp = request.POST.get('otp', '')
        session_otp = str(request.session.get('otp', ''))
        
        if user_otp == session_otp:
            return redirect('new_password')
        else:
            msg = "Invalid OTP!"
            return render(request, 'verify_otp.html', {'msg': msg, 'masked_email': masked_email, 'email': email})
            
    return render(request, 'verify_otp.html', {'masked_email': masked_email, 'email': email})

def new_password(request):
    if request.method == "POST":
        new_pass = request.POST.get('new_password')
        conf_pass = request.POST.get('cpassword')
        if new_pass == conf_pass:
            email = request.session.get('reset_email')
            user = User.objects.get(email=email)
            user.password = new_pass
            user.save()
            return redirect('login')
        else:
            msg = "Password & confirm password do not match!!"
            return render(request, 'new_password.html', {'msg': msg})
    return render(request, 'new_password.html')

def update_profile(request):
    try:
        user = User.objects.get(email=request.session.get('email'))
    except:
        return redirect('login')
        
    if request.method == "POST":
        user.name = request.POST.get('name')
        user.mobile = request.POST.get('mobile')
        if 'profile_image' in request.FILES:
            user.profile_pic = request.FILES['profile_image']
        user.save()
        return redirect('index')
        
    return render(request, 'update_profile.html', {'user': user})



# ==========================================
# USER CAR RENTAL VIEWS
# ==========================================

def car_rentals(request):
    # Check if a user is logged in
    email = request.session.get('email')
    
    if email:
        try:
            user = User.objects.get(email=email)
            # Agar agency login hai, toh sirf uski apni cars dikhaani hain
            if user.usertype == 'agency':
                cars = Car.objects.filter(agency=user)
            else:
                # Agar customer hai, toh sabhi agencies ki cars dikhaani hain
                cars = Car.objects.all()
        except User.DoesNotExist:
            cars = Car.objects.all()
    else:
        # Agar koi login nahi hai, toh bhi sabhi cars dikhaani hain
        cars = Car.objects.all()
        
    return render(request, 'car_rentals.html', {'cars': cars})

def car_details(request, pk):
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return redirect('car_rentals')
        
    return render(request, 'car_details.html', {'car': car})

def edit_car(request, pk):
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return redirect('car_rentals')
        
    email = request.session.get('email')
    if not email:
        return redirect('login')
        
    user = User.objects.get(email=email)
    if user.usertype != 'agency' or car.agency != user:
        return redirect('car_rentals')
        
    if request.method == "POST":
        car.car_name = request.POST.get('car_name')
        car.brand = request.POST.get('brand')
        car.model_year = request.POST.get('model_year')
        # plate_number is readonly, not updating it here
        car.price_per_hour = request.POST.get('price_per_hour')
        car.price_per_day = request.POST.get('price_per_day')
        car.seats = request.POST.get('seats')
        car.fuel_type = request.POST.get('fuel_type')
        car.transmission = request.POST.get('transmission')
        
        car.has_ac = 'has_ac' in request.POST
        car.has_airbags = 'has_airbags' in request.POST
        car.has_abs = 'has_abs' in request.POST
        car.has_gps = 'has_gps' in request.POST
        car.has_music_system = 'has_music_system' in request.POST
        car.has_reverse_camera = 'has_reverse_camera' in request.POST
        
        car.airbags_count = request.POST.get('airbags_count')
        car.tyre_condition = request.POST.get('tyre_condition')
        
        if 'car_image' in request.FILES:
            car.car_image = request.FILES['car_image']
            
        car.save()
        return redirect('car_rentals')
        
    return render(request, 'edit_car.html', {'car': car})

def delete_car(request, pk):
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return redirect('car_rentals')
        
    email = request.session.get('email')
    if email:
        user = User.objects.get(email=email)
        if user.usertype == 'agency' and car.agency == user:
            car.delete()
            
    return redirect('car_rentals')

def add_to_wishlist(request):
    if request.method == 'POST':
        email = request.session.get('email')
        if not email:
            return redirect('login')
        user = User.objects.get(email=email)
        car = Car.objects.get(pk=request.POST.get('car_id'))
        Wishlist.objects.get_or_create(user=user, car=car)
        return redirect('show_wishlist')
    return redirect('car_rentals')

def show_wishlist(request):
    email = request.session.get('email')
    if not email:
        return redirect('login')
    user = User.objects.get(email=email)
    wishlist_items = Wishlist.objects.filter(user=user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

def remove_from_wishlist(request, pk):
    email = request.session.get('email')
    if not email:
        return redirect('login')
    user = User.objects.get(email=email)
    try:
        wishlist_item = Wishlist.objects.get(pk=pk, user=user)
        wishlist_item.delete()
    except Wishlist.DoesNotExist:
        pass
    return redirect('show_wishlist')



def payment(request, pk):
    try:
        user = User.objects.get(email=request.session['email'])
    except:
        return redirect('login')
        
    car = Car.objects.get(pk=pk)
    pickup_time_str = request.POST.get('pickup_time', '')
    return_time_str = request.POST.get('return_time', '')
    
    rental_days = 0
    total_amount = 0
    
    if pickup_time_str and return_time_str:
        try:
            pickup_time = datetime.strptime(pickup_time_str, '%Y-%m-%dT%H:%M')
            return_time = datetime.strptime(return_time_str, '%Y-%m-%dT%H:%M')
            
            # Calculate days
            delta = return_time - pickup_time
            rental_days = delta.days
            
            # If hours > 0, consider it another day, or just minimum 1 day
            if delta.seconds > 0 or rental_days == 0:
                rental_days += 1
                
            if rental_days < 1:
                rental_days = 1
                
            total_amount = rental_days * car.price_per_day
            
            # Store in session for process_payment
            request.session['booking_data'] = {
                'car_id': car.pk,
                'pickup_time': pickup_time_str,
                'return_time': return_time_str,
                'rental_days': rental_days,
                'total_amount': total_amount
            }
        except Exception as e:
            pass

    return render(request, 'payment.html', {
        'car': car, 
        'rental_days': rental_days, 
        'total_amount': total_amount, 
        'pickup_time': pickup_time_str, 
        'return_time': return_time_str
    })

def process_payment(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.session['email'])
            booking_data = request.session.get('booking_data')
            if not booking_data:
                return redirect('car_rentals')
                
            car = Car.objects.get(pk=booking_data['car_id'])
            payment_method = request.POST.get('payment_method', 'Card')
            
            # Generate IDs
            booking_id = "BKG" + get_random_string(length=10).upper()
            transaction_id = "TXN" + get_random_string(length=12).upper()
            payment_id = "PAY" + get_random_string(length=12).upper()
            
            # Create Booking
            booking = Booking.objects.create(
                user=user,
                car=car,
                pickup_time=booking_data['pickup_time'],
                return_time=booking_data['return_time'],
                rental_days=booking_data['rental_days'],
                total_amount=booking_data['total_amount'],
                booking_id=booking_id,
                status='CONFIRMED'
            )
            
            # Create Payment
            payment = Payment.objects.create(
                user=user,
                booking=booking,
                amount=booking_data['total_amount'],
                payment_method=payment_method,
                transaction_id=transaction_id,
                payment_id=payment_id,
                status='SUCCESS'
            )
            
            # Clear session
            del request.session['booking_data']
            
            return render(request, 'payment_success.html', {'booking': booking})
            
        except Exception as e:
            print("Error processing payment:", e)
            return redirect('car_rentals')
    return redirect('car_rentals')

def my_orders(request):
    try:
        user = User.objects.get(email=request.session['email'])
        bookings = Booking.objects.filter(user=user).order_by('-booking_date')
        return render(request, 'my_orders.html', {'bookings': bookings})
    except:
        return redirect('login')

def booking_details(request, pk):
    try:
        user = User.objects.get(email=request.session['email'])
        booking = Booking.objects.get(pk=pk, user=user)
        payment = Payment.objects.filter(booking=booking).first()
        return render(request, 'booking_details.html', {'booking': booking, 'payment': payment})
    except:
        return redirect('login')

def cancel_booking(request, pk):
    try:
        user = User.objects.get(email=request.session['email'])
        booking = Booking.objects.get(pk=pk, user=user)
        if booking.status != 'CANCELLED' and booking.status != 'COMPLETED':
            booking.status = 'CANCELLED'
            booking.save()
    except Exception as e:
        pass
    return redirect('my_orders')

def download_invoice(request, pk):
    try:
        user = User.objects.get(email=request.session['email'])
        booking = Booking.objects.get(pk=pk, user=user)
        payment = Payment.objects.filter(booking=booking).first()
        
        template_path = 'invoice.html'
        
        gst = int(booking.total_amount * 0.18) # Dummy 18% GST calculation display if needed, but we'll stick to total as inclusive
        subtotal = booking.total_amount - gst
        
        context = {'booking': booking, 'payment': payment, 'subtotal': subtotal, 'gst': gst}
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Invoice_{booking.booking_id}.pdf"'
        
        template = get_template(template_path)
        html = template.render(context)
        
        pisa_status = pisa.CreatePDF(html, dest=response)
        
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    except Exception as e:
        return HttpResponse('Invoice generation error: ' + str(e))