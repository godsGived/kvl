from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.split),
    path('app_name/', include('app_name.urls')), 
]