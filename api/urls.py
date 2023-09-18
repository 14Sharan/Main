from django.urls import path,include
from .views import *
from drf_yasg import openapi
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg.utils import swagger_auto_schema

from drf_yasg.generators import OpenAPISchemaGenerator
import os
app_name='api'

class SchemaGenrator(OpenAPISchemaGenerator):
    def get_schema(self,request=None,public=False):
        schema=super(SchemaGenrator,self).get_schema(request,public)
        schema.basepath= os.path.join(schema.basePath,'api/')
        schema.schemes=["http","https"]
        return schema
schema_view = get_schema_view(
    openapi.Info(
        title="Corsec Api's",
        description="Api documentation for Corsec Project",
        default_version="1.0.0",
        terms_of_service="",
        contact=openapi.Contact(email = ""),
        license=openapi.License(name = "Corsec")

    ),
    public = True,
    permission_classes=(permissions.AllowAny,),

)



urlpatterns = [
    re_path(r'^swagger-schema/$',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    re_path(r'^documentaion/$',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),


    re_path(r'^signup/$',Signup.as_view(),name="signup"),



] 