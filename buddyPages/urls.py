from django.urls import path
from . import views

urlpatterns = [
    path('whale/', views.whale, name='whale'),
    path('turtle/', views.turtle, name='turtle'),
    path('seal/', views.seal, name='seal'),
    path('seagull/', views.seagull, name='seagull'),
    path('dolphin/', views.dolphin, name='dolphin'),

    
]
