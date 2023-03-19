from django.urls import path, include
from . import views  # this is the path to the views.py file in the base app

urlpatterns = [
    path('communityPage/', views.communityPage, name='communityPage'),
    path('addPost/', views.addPost, name='addPost'),
    path('post/<int:pk>/comment/', views.addComment, name='addComment'),
    path('postDetails/', views.postDetails, name='postDetails'),
]
