from django.urls import path
from . import views
from .views import save_high_score

urlpatterns = [

    # userProfile urls
    path('userProfilePage/', views.userProfilePage, name='userProfilePage'),
    path('scores/', save_high_score, name='save_high_score'),

]
