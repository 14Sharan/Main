from django.shortcuts import render,redirect
from accounts.models import *
from accounts.constants import *

def subjects(request):
    return render(request,"subjects/subjects-list.html")

def All_users(request):
    all_users = User.objects.all().exclude(role_id = 1 ).order_by("-created_on")
    return render(request,"admin/users/all-users.html",{"users":all_users})

def DeleteUser(request,id):
    User.objects.get(id=id).delete()
    return redirect('superuser:all_users')

def userProfile(request,id):
    user = User.objects.get(id = id)
    return render(request,"admin/users/user-profile.html",{"user":user})