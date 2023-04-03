from django.urls import path
from . import views

urlpatterns = [

    #portal urls
    path('portalPage/', views.portalPage, name='portalPage'),
    path('addPostPage/', views.addPostPage, name='addPostPage'),



    
]
