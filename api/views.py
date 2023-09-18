from django.shortcuts import render
from rest_framework.views import APIView 
from accounts.models import *
from api.serializer import *
from rest_framework import  permissions,status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import make_password


class Signup(APIView):
    permission_classes = [permissions.AllowAny,]
    parser_classes = [MultiPartParser]
    @swagger_auto_schema(
        tags=['Authentication'],
        operation_id = "Signup",
        operation_description = "Signup",
        manual_parameters = [
            openapi.Parameter('email',openapi.IN_FORM,type=openapi.TYPE_STRING),
            openapi.Parameter('password',openapi.IN_FORM,description="password",type=openapi.TYPE_STRING)
        ]
    )
    def post(self,request,*args,**kwargs):
        User.objects.create(email=request.data.get('email'),
                            password = make_password(request.data.get('password')))
        data = UserSerializer(context={"request":request}).data
        return Response({"data":data,"messages":"Signup Successfully","status":status.HTTP_200_OK},status=status.HTTP_200_OK)




    