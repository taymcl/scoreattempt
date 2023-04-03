from django.urls import path
from . import views

urlpatterns = [




    #userProfile urls
    path('userProfilePage/', views.userProfilePage, name='userProfilePage'),


    
]
