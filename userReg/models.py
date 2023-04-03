from django.db import models
from django.contrib.auth.models import User

#model for characters
class Characters(models.Model):
    CHARACTER_CHOICES = (
        ('W', 'Whale'),
        ('D', 'Dolphin'),
        ('T', 'Turtle'),
        ('S', 'Seal'),
        ('G', 'Seagull'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    character = models.CharField(max_length=1, choices=CHARACTER_CHOICES)
    character_picture = models.ImageField(upload_to='static/images/profilePictures', null=True, blank=True)


    def __str__(self):
        return f'{self.user} - {self.get_character_display()}'
    

