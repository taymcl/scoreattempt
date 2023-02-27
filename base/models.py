from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    age = models.IntegerField()
    guardian_name = models.CharField(max_length=20)
    guardian_email = models.EmailField()

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
