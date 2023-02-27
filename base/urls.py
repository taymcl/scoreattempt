from django.urls import path
from . import views

urlpatterns = [
    path('', views.basePage, name='basePage'), #url for base page
    path('registerPage/', views.registerPage, name='registerPage'), #url for register page
    path('loginPage/', views.loginPage, name='loginPage'), #url for login page

    #Registration Urls
    path('registerFreemium/', views.registerFreemium, name='registerFreemium'), #url for register freemium page
    path('registerPremium/', views.registerPremium, name='registerPremium'), #url for register premium page
    path('registerUnlimited/', views.registerUnlimited, name='registerUnlimited'), #url for register unlimted page

    #Portal Urls
    path('homePage/', views.homePage, name='homePage'), #url for home page
    path('logout/', views.logoutUser, name='logout'), #url for logout



]