from django.urls import path, include 
from . import views #this is the path to the views.py file in the base app




urlpatterns = [
    path('', views.homePage, name='homePage'), #url for the home page
    
    #Paths for userReg app
    path('registerPage/', views.registerPage, name='registerPage'), #url for the register page
    path('loginPage/', views.loginPage, name='loginPage'), #url for the login page
    path('portalPage/', views.portalPage, name='portalPage'), #url for the portal page
    
    #Paths for userReg app
    path('profilePage/', views.profilePage, name='profilePage'),
    path('editProfilePage/', views.editProfilePage, name='editProfilePage'),

    #Paths for community app
    path ('communityPage/', views.communityPage, name='communityPage'),
    path ('addPost/', views.addPost, name='addPost'),
    path ('addComment/', views.addComment, name='addComment'),
    path ('postDetails/', views.postDetails, name='postDetails'),

    ]

