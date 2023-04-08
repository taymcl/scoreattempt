from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #used for admin panal
    path('', include('base.urls')), #used for base urls
    path('userReg/', include('userReg.urls')), #user for userReg urls
    path('userProfile/', include('userProfile.urls')), #used for userProfile urls
    path('portal/', include('portal.urls')), #used for userProfile urls
    path('video/', include('video.urls')), #used for userProfile urls

    

]
