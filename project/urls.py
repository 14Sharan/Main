from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("accounts.urls")),
    path('superuser/',include("superuser.urls")),
    path('course/',include("course.urls")),
    path('api/',include("api.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    