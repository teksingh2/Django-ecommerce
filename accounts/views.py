from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse 
from core.models import *
from django.contrib import messages
# Create your views here.
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        our_user=authenticate(username=username,password=password)
        if our_user is not None:
            login(request,our_user)
            return redirect('/')
        
        messages.info(request,'Invalid Credentials')
        
        
    return render(request,'accounts/login.html')

def user_register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('user_register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email already exists')
                else:
                    user=User.objects.create_user(username,email,password)
                    user.save()
                    customer=Customer(user=user)
                    customer.save()
                #redirect to dashboard
                our_user=authenticate(username=username,password=password)
                if our_user is not None:
                    login(request,our_user)
                    return redirect('/')
        else:
            messages.info(request,'Password does not match')
            return redirect('user_register')
    return render(request,'accounts/register.html')

def user_logout(request):
    logout(request)
    return redirect('user_login') 