from django.urls import path,include
from .views import *
app_name='superuser'
urlpatterns = [
    path('all-users/',All_users,name='all_users'),
    path('subjects/',subjects,name='subjects'),
    path('delete-user/<int:id>',DeleteUser,name='delete_user'),
    path('user-profile/<int:id>',userProfile,name='user_profile'),
] 