from django.forms import ModelForm
from django import forms  # imports django forms
from .models import Posts, Comments


class createPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['postTitle', 'postBody']


class createCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
