from django.shortcuts import render,redirect
from accounts.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.db.models import Q
from django.http import JsonResponse
import io
from pyqrcode import create
import png 

def index(request):
    users = User.objects.filter(role_id = STUDENT).count()
    return render(request,'admin/index.html',{"users":users})

def Signup(request):
    if request.method=="POST":
        user=User.objects.create(username=request.POST.get("username"),
                            first_name=request.POST.get("firstname"),
                            last_name=request.POST.get('lastname'),
                            full_name = request.POST.get("firstname") + " " +request.POST.get('lastname'),
                            email = request.POST.get('email'),
                            mobile_no = request.POST.get("mobile_no"),
                            role_id = STUDENT,
                            password=make_password(request.POST.get('password')))
        buffer = io.BytesIO()
        embedded_qr = create(user.id)
        embedded_qr.png(buffer,scale=7)
        base_data = buffer.getvalue()
        user.qr_code = base_data
        user.save()
        return redirect("accounts:login")        
    return render(request,"registration/signup.html")

def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user.is_superuser:
            login(request,user)
            return redirect('accounts:index')
        elif not user.is_superuser:
            login(request,user)
            return redirect('accounts:signup')
        return render(request,"registration/signin.html")
    return render(request,"registration/signin.html")

def LogOut(request):
    logout(request)
    return redirect("accounts:signup")


"""
Validate email for existing email
"""
def ValidateEmail(request):
    data = {"is_exist":"false"}
    user = User.objects.filter(email = request.GET.get('email'))
    if user:
        data['is_exist']="true"
    else:
        data['is_exist']="false"
    return JsonResponse(data)

