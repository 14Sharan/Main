from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.constants import *

class User(AbstractUser):
    username = models.CharField(max_length=255,null=True,blank=True,unique=True)
    full_name = models.CharField(max_length=255,null =True,blank =True)
    first_name=models.CharField(max_length=255,null=True,blank=True)
    last_name=models.CharField(max_length=255,null=True,blank=True)
    role_id =models.PositiveIntegerField(default = 1,choices = USER_ROLE,null=True,blank=True)
    user_status = models.PositiveIntegerField(default=ACTIVE,choices=USER_STATUS,null =True,blank =True)
    profile_status = models.BooleanField(default=False,null=True,blank=True)
    email=models.EmailField(max_length=255,null=True,blank=True)
    mobile_no=models.CharField(max_length=255,null=True,blank=True)
    address=models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null = True,blank =True)
    country = models.CharField(max_length=255,null = True,blank =True)
    postal_code = models.CharField(max_length=255,null = True,blank =True)
    profile_pic=models.FileField(upload_to='profile',null=True,blank=True)
    about = models.TextField(null = True,blank = True)
    created_on = models.DateTimeField(auto_now_add=True,null =True,blank=True)
    updated_on = models.DateTimeField(auto_now=True,null =True,blank=True)
    qr_code = models.TextField(null=True,blank=True)

    class Meta:
        managed = True
        db_table = "tb_user"


    