from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    postTitle = models.CharField(max_length=100, null=True)
    postBody = models.TextField(null=True)
    postComment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.user)

