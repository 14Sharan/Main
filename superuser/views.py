from django.shortcuts import render, redirect
from accounts.models import *
from accounts.constants import *
from django.contrib.auth.decorators import login_required
import qrcode
import qrcode.image.svg
from io import BytesIO

@login_required
def All_users(request):
    all_users = User.objects.all().exclude(role_id=1).order_by("-created_on")
    return render(request, "admin/users/all-users.html", {"users": all_users})

@login_required
def DeleteUser(request, id):
    user = User.objects.get(id=id)
    user.user_status = DELETED
    user.save()
    return redirect('superuser:all_users')

@login_required
def userProfile(request, id):
    if request.method  == "GET":
        user = User.objects.get(id=id)
        return render(request, "admin/users/user-profile.html", {"user": user})
    if request.method == "POST":
        user = User.objects.get(id=id)
        if request.POST.get('firstname'):
            user.first_name = request.POST.get('firstname')
        if  request.POST.get('last_name'):
            user.last_name = request.POST.get('last_name')
        if request.POST.get('email'):
            user.email = request.POST.get('email')
        if request.FILES.get('profile_pic'):
            user.profile_pic = request.FILES.get('profile_pic')
        if request.POST.get('city'):
            user.city = request.POST.get('city')
        if request.POST.get('country'):
            user.country = request.POST.get('country')
        if request.POST.get('address'):
            user.address = request.POST.get('address')
        if request.POST.get('postal_code'):
            user.postal_code = request.POST.get('postal_code')
        if request.POST.get("about"):
            user.about = request.POST.get("about")
        user.save()
        return redirect('superuser:user_profile',id = id)

"""
Activate User
"""
@login_required
def Activate_user(request,id):
    user=User.objects.get(id=id)
    user.user_status = ACTIVE
    user.save()
    return redirect('superuser:user_profile',id = id)

"""
In-activate User
"""
@login_required
def Inactive_user(request,id):
    user=User.objects.get(id=id)
    user.user_status = INACTIVE
    user.save()
    return redirect('superuser:user_profile',id = id)


