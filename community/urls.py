from django.urls import path
from . import views

urlpatterns = [


    #community urls
    path('communityPage/', views.communityPage, name='communityPage'),



    
]
