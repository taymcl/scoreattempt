from django.forms import ModelForm
from django import forms 
from django.contrib.auth.models import User #uses the default django User model




class registerAnotherBuddyForm(forms.ModelForm):
    registration_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['registration_code']



