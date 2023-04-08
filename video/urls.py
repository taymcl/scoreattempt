from django.urls import path
from . import views

urlpatterns = [

    path('videoPage/', views.videoPage, name='videoPage'),

    
]
