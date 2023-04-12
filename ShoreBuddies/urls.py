from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #used for admin panal
    path('', include('base.urls')), #used for base urls
    path('userReg/', include('userReg.urls')), #user for userReg urls
    path('userProfile/', include('userProfile.urls')), #used for userProfile urls
    path('portal/', include('portal.urls')), #used for userProfile urls
    path('video/', include('video.urls')), #used for userProfile urls
    path('buddyPages/', include('buddyPages.urls')), #used for userProfile urls
    path('regBuddy2/', include('regBuddy2.urls')), #used for regBuddy2 urls

    

] 
