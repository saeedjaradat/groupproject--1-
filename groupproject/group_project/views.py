from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')

# login page
def login_page(request):
    return render(request,'login.html')

# register page
def register_page(request):
    return render(request,'register.html')

# register method
def register(request):
    print("***** 1 ")
    error = members.objects.member_validator(request.POST)
    if len(error) > 0:
        print("***** 2 ")
        for key, value in error.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/register_page')
    else:
        if request.method == "POST":
            print("***** 3 ")
            Register(request)
            print("***** 4 ")
        return redirect('/')

# admin dashboard
def admin_dash(request):
    return render(request,'admin_dashboard.html')