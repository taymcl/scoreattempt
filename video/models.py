from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()
    # Add any other fields you need for your videos