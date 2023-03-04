from django.shortcuts import render,redirect
from accounts.models import *
from accounts.constants import *

def subjects(request):
    return render(request,"subjects/subjects-list.html")

def All_users(request):
    all_users = User.objects.all().exclude(role_id = 1 )
    return render(request,"admin/users/all-users.html",{"users":all_users})