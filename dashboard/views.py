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
from .form import RegisterForm
from .models import newUser


# Create your views here.
# @login_required
def dashboard_view(request):
    return render(request, 'dashboard/index.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        print(user)
        print("Hello User")

        if user is not None:
            login(request, user)
            return redirect('dashboard-home')
        else:
            messages.error(request, "username or password incorrect")
            return redirect('dashboard:loginUser')


    return render(request, 'dashboard/login.html')


def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful!")
            return redirect('dashboard:loginUser')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, 'dashboard/signup.html', {'form': form})
