from django.contrib import admin
from .models import Profile, HighScores

# Register your models here.
admin.site.register(Profile)
admin.site.register(HighScores)