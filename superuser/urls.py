from django.urls import path,include
from .views import *
app_name='superuser'
urlpatterns = [
    path('all-users/',All_users,name='all_users'),
    path('delete-user/<int:id>',DeleteUser,name='delete_user'),
    path('user-profile/<int:id>',userProfile,name='user_profile'),
    path('activate-user/<int:id>',Activate_user,name='activate_user'),
    path('inactive-user/<int:id>',Inactive_user,name='inactive_user'),
] 