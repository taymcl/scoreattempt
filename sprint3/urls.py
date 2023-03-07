
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #this is the path to the admin panel
    path('', include('base.urls')), #this is the path to the base app
    path('userReg/', include('userReg.urls')), #this is the path to the userReg app
    path('userProfile/', include('userProfile.urls')), #this is the path to the userProfile app
    path('community/', include('community.urls')), #this is the path to the community app
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
