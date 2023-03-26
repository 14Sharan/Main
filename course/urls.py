from django.urls import path,include
from .views import *
app_name='course'
urlpatterns = [
    path('subjects/',Subjects,name='subjects'),
] 