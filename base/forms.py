from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  # imports default user creation form
from django import forms  # imports django forms
from django.contrib.auth.models import User  # uses the default django User model
from .models import Profile


# Form For User Registration
class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))  # takes in username
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))  # takes in first name
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))  # takes in last name
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))  # takes in email
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))  # takes in password
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))  # confirmation password
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))  # takes age
    guardian_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    guardian_email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User  # based off django default User model
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    class Profile:
        model = Profile
        fields = ['age', 'guardian_name', 'guardian_email']
