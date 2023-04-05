from django.forms import ModelForm
from django import forms #imports django forms
from .models import Profile



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'age', 'bio', 'profile_picture']
