
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #url for admin
    path('', include('base.urls')),
]

