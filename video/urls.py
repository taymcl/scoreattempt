from django.urls import path
from .views import videoPage, video_detail

urlpatterns = [
    # URL pattern for videoPage view
    path('', videoPage, name='video_page'),
    # URL pattern for video_detail view with video_id parameter
    path('video_detail/<int:video_id>/', video_detail, name='video_detail'),
]
