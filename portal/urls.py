from django.urls import path
from . import views

urlpatterns = [

    #portal urls
    path('portalPage/', views.portalPage, name='portalPage'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('regAnotherBuddy/', views.regAnotherBuddy, name='regAnotherBuddy'),
    path('user_buddies/', views.user_buddies, name='user_buddies'),
    path('game/', views.game, name='game'),
    path('freemiumPortal/', views.freemiumPortal, name='freemiumPortal'),

    # path('addPostPage/', views.addPostPage, name='addPostPage'),



    
]
