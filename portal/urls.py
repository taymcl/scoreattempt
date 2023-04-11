from django.urls import path
from . import views

urlpatterns = [

    #portal urls
    path('portalPage/', views.portalPage, name='portalPage'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('regAnotherBuddy/', views.regAnotherBuddy, name='regAnotherBuddy'),


    # path('addPostPage/', views.addPostPage, name='addPostPage'),



    
]
