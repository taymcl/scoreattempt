from django.forms import ModelForm
from django import forms #imports django forms
from .models import Posts



class createPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['postTitle', 'postBody', 'postComment']