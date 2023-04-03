from django.db import models
from django.contrib.auth.models import User

# Model for User profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True)
    age = models.IntegerField(null=True)
    profile_picture = models.ImageField(upload_to='static/images', null=True, blank=True)
    


    def __str__(self):
        return str(self.user)