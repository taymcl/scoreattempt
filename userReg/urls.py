from django.urls import path
from . import views

urlpatterns = [
    
    #userReg urls
    path('registerPage/', views.registerPage, name='registerPage'),

    path('registerTurtle/', views.registerTurtle, name='registerTurtle'),
    path('registerWhale/', views.registerWhale, name='registerWhale'),
    path('registerSeal/', views.registerSeal, name='registerSeal'),
    path('registerSeagull/', views.registerSeagull, name='registerSeagull'),
    path('registerDolphin/', views.registerDolphin, name='registerDolphin'),
    path('registerFreemium/', views.registerFreemium, name='registerFreemium'),

   







    
]
