from django.db import models
from django.contrib.auth.models import User

# Model for characters
class Characters(models.Model):
    CHARACTER_CHOICES = (
        ('W', 'Whale'),
        ('D', 'Dolphin'),
        ('T', 'Turtle'),
        ('S', 'Seal'),
        ('G', 'Seagull'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='characters')
    character = models.CharField(max_length=1, choices=CHARACTER_CHOICES)
    character_picture = models.ImageField(upload_to='static/images/profilePictures', null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.get_character_display()}'
    

from django.contrib.auth.models import User
from django.db import models



class Buddies(models.Model):
    BUDDY_CHOICES = (
        ('whale', 'Whale'),
        ('turtle', 'Turtle'),
        ('dolphin', 'Dolphin'),
        ('seal', 'Seal'),
        ('seagull', 'Seagull'),
    )

    name = models.CharField(max_length=50, choices=BUDDY_CHOICES)
    picture = models.ImageField(upload_to='static/images/profilePictures')

    # Many-to-One relationship with User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

