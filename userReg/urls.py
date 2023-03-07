from django.urls import path, include
from . import views #this is the path to the views.py file in the base app



urlpatterns = [
    #base urls
    path('', views.homePage, name='homePage'), #url path for the home page
    path('portalPage/', views.portalPage, name='portalPage'), #url for the portal page



    #userReg urls
    path('registerPage/', views.registerPage, name='registerPage'), #url path for the register page
    path('loginPage/', views.loginPage, name='loginPage'), #url path for the login page
    path('registerUnlimited/', views.registerUnlimited, name='registerUnlimited'), #url path for the registerUnlimited page
    path('registerPremium/', views.registerPremium, name='registerPremium'), #url path for the registerPremium page
    path('registerFreemium/', views.registerFreemium, name='registerFreemium'), #url path for the registerFreemium page
    path('logout/', views.logoutUser, name='logout'), #url for logout

    ]

