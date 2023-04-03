from django.forms import ModelForm
from django import forms #imports django forms
from django.contrib.auth.models import User  #uses the default django User model
from .models import Posts



class createPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['postBody']




