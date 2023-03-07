from django.urls import path, include 
from . import views #this is the path to the views.py file in the base app



urlpatterns = [
    path('profilePage/', views.profilePage, name='profilePage'), 
    path('editProfilePage/', views.editProfilePage, name='editProfilePage'),
]

