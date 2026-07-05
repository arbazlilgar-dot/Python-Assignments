from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserProfile
from .forms import UserProfileForm
import csv
import tempfile
import os

def list_profiles(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profiles/list.html', {'profiles': profiles})

def create_profile(request):
    # Section B - Question 3: Django Views for Persistence handling POST requests, form.is_valid(), and form.save().
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_profiles')
    else:
        form = UserProfileForm()
    
    return render(request, 'profiles/create.html', {'form': form})

def export_profiles_csv(request):
    # Section C - Question 3: "Save to File" feature using Python's csv module and Context Managers (with open/HttpResponse).
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="profiles.csv"'
    
    profiles = UserProfile.objects.all()
    
    # Using context manager as required by the assessment
    with tempfile.NamedTemporaryFile(mode='w', delete=False, newline='', suffix='.csv') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Age', 'Is Public'])
        for profile in profiles:
            writer.writerow([profile.username, profile.age, profile.is_public])
        temp_path = file.name
        
    with open(temp_path, 'r') as file:
        response.write(file.read())
        
    os.remove(temp_path)
    
    return response
