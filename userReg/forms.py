from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm #imports default user creation formn
from django import forms #imports django forms
from django.contrib.auth.models import User #uses the default django User model


#Form For User Registration
class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    registration_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'registration_code']






class registerAnotherBuddy(forms.Form):
    registration_code = forms.CharField(max_length=10)
