# Generated by Django 4.1.7 on 2023-03-03 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0003_profile_age_profile_firstname_profile_lastname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profilePic',
        ),
    ]
