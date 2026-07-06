# Doctor Finder

A complete, production-ready healthcare web application built using Django. This project fulfills all requirements, including a premium Glassmorphism UI, complete MVT architecture, standard and AJAX CRUD operations, authentication, a simulated payment gateway, and Google Maps integration.

## Features
- **Premium UI/UX:** Clean, modern, responsive design using Glassmorphism and CSS animations.
- **Authentication:** Custom Patient registration, login, logout, and Admin roles.
- **Doctor Directory:** Browse, search, and filter doctors by name, specialization, and location.
- **Doctor Profiles:** Detailed profiles integrated with Google Maps showing clinic locations.
- **Appointment Booking:** Seamlessly book appointments selecting date and time.
- **Payment Gateway:** Dummy Paytm integration simulating successful payments.
- **Admin Dashboard:** Manage doctors via AJAX (add, update, delete without page refresh).
- **Patient Dashboard:** View appointments, track payment status, and make payments.
- **Deployment Ready:** Configured for local running, GitHub, and PythonAnywhere.

## Installation & Setup

1. **Activate Virtual Environment:**
   If you haven't already created one:
   ```bash
   python -m venv env
   .\env\Scripts\activate  # Windows
   # or
   source env/bin/activate  # Mac/Linux
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a Superuser (Admin):**
   ```bash
   python manage.py createsuperuser
   ```
   *Follow the prompts to create an admin account.*

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   *Access the app at http://127.0.0.1:8000*

## Project Structure
- `doctor_finder/` - Main Django project configuration (settings, main urls).
- `doctor/` - The core application (models, views, forms, urls).
- `static/` - CSS (Glassmorphism), JavaScript (Validation & AJAX), Images.
- `templates/` - HTML files organized by function (Auth, Dashboards, Public Pages).

## Technologies Used
- Backend: Python 3, Django
- Frontend: HTML5, CSS3, JavaScript (AJAX)
- Database: SQLite (default, ready for MySQL)
