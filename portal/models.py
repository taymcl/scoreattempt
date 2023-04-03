from django.db import models
from django.contrib.auth.models import User


# Model for user Posts
class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    postBody = models.TextField(null=True)
    
    #Date and time fields
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)
