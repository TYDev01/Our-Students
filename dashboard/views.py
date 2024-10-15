from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *


# Create your views here.
# @login_required
def dashboard_view(request):
    return render(request, 'dashboard/index.html')


def login_view(request):
    return render(request, 'dashboard/login.html')

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        user_details_have_error = False

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            user_details_have_error = True
            messages.error(request, "user with this email already exists")

        # Check if the passwords match
        if password != password2:
            user_details_have_error = True
            messages.error(request, "password doesn't match")

        if len(password) < 8:
            user_details_have_error = True
            messages.error(request, "password must not be less than 8 characters")
        
        else:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                gender=gender,
                password=password
            )
            messages.success(request, "Account created successfully")
            return redirect('loginUser')

    return render(request, 'dashboard/signup.html')