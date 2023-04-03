
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  #used for User Authentication
from django.contrib.auth.decorators import login_required #this is so we can restrict pages if you are not a logged in user
from django.contrib import messages #used to send a flash message

# userProfile views
def userProfilePage(request):
    return render(request, 'userProfile/userProfilePage.html')

