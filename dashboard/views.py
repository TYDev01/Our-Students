from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
    return render(request, 'dashboard/signup.html')