from django.urls import path
from . import views

urlpatterns = [

    #base urls
    path('', views.landingPage, name='landingPage'), #this will be the default page
    path('logout/', views.logoutUser, name='logout'),

  
  
  

    #userReg urls
    path('registerPage/', views.registerPage, name='registerPage'),
    path('registerTurtle/', views.registerTurtle, name='registerTurtle'),
    path('registerWhale/', views.registerWhale, name='registerWhale'),
    path('registerSeal/', views.registerSeal, name='registerSeal'),
    path('registerSeagull/', views.registerSeagull, name='registerSeagull'),
    path('registerDolphin/', views.registerDolphin, name='registerDolphin'),
    path('registerFreemium/', views.registerFreemium, name='registerFreemium'),

    

    #userProfile urls
    path('userProfilePage/', views.userProfilePage, name='userProfilePage'),



    #portal urls
    path('portalPage/', views.portalPage, name='portalPage'),
    path('addPostPage/', views.addPostPage, name='addPostPage'),


    #community urls
    path('communityPage/', views.communityPage, name='communityPage'),







    
]
