# Imports
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm #used for our user creation form
from .forms import CreateUserForm  #used for our user creation form
from django.contrib.auth import authenticate, login, logout  #used for User Authentication
from django.contrib.auth.decorators import login_required #this is so we can restrict pages if you are not a logged in user
from django.contrib import messages #used to send a flash message
from django.contrib.auth.models import Group #used to access our groups
from userProfile.models import Profile  #used to access our profile model
from django.contrib.auth.models import User
from .models import Characters #import our characters model
from .models import Buddies #import our buddies model
from .forms import registerAnotherBuddy #import our form for registering another buddy



#userReg Views
def registerPage(request):
    return render(request, 'userReg/registerPage.html')

def registerWhale(request):
    if request.user.is_authenticated:
        return redirect('portalPage') 
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'whale': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerWhale') # redirect back to the same page
                else:
                    user = form.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profilePictures/default.jpg')
                    profile.save()

                    buddy = 'whale'
                    Buddies.objects.create(user=user, name=buddy, picture='static/images/characters/whale.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('landingPage')
        context = {'form':form,}
        return render(request, 'userReg/registerWhale.html', context)


def registerTurtle(request):
    if request.user.is_authenticated:
        return redirect('portalPage') 
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'turtle': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerTurtle') # redirect back to the same page
                else:
                    user = form.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profilePictures/default.jpg')
                    profile.save()

                    buddy = 'turtle'
                    Buddies.objects.create(user=user, name=buddy, picture='static/images/characters/turtle.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('landingPage')
        context = {'form':form,}
        return render(request, 'userReg/registerTurtle.html', context)
    


def registerSeal(request):
    if request.user.is_authenticated:
        return redirect('portalPage') 
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'seal': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerSeal') # redirect back to the same page
                else:
                    user = form.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profilePictures/default.jpg')
                    profile.save()

                    buddy = 'seal'
                    Buddies.objects.create(user=user, name=buddy, picture='static/images/characters/seal.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('landingPage')
        context = {'form':form,}
        return render(request, 'userReg/registerSeal.html', context)

def registerSeagull(request):
    if request.user.is_authenticated:
        return redirect('portalPage') 
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'seagull': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerSeagull') # redirect back to the same page
                else:
                    user = form.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profilePictures/default.jpg')
                    profile.save()

                    buddy = 'seagull'
                    Buddies.objects.create(user=user, name=buddy, picture='static/images/characters/seagull.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('landingPage')
        context = {'form':form,}
        return render(request, 'userReg/registerSeagull.html', context)

def registerDolphin(request):
    if request.user.is_authenticated:
        return redirect('portalPage') 
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'dolphin': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerDolphin') # redirect back to the same page
                else:
                    user = form.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profilePictures/default.jpg')
                    profile.save()

                    buddy = 'dolphin'
                    Buddies.objects.create(user=user, name=buddy, picture='static/images/characters/dolphin.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('landingPage')
        context = {'form':form,}
        return render(request, 'userReg/registerDolphin.html', context)



def registerFreemium(request):
    if request.user.is_authenticated: #if the user is authenticated
        return redirect('freemiumPortal') 
    else:
        form = CreateUserForm() #import our form
        if request.method == 'POST': #checking for a post request
            form = CreateUserForm(request.POST) #use our form
            if form.is_valid(): # if the regrestration is successfully filled out
                user = form.save() #save the information and store the created user object in a variable
                group = Group.objects.get(name='freemium') #retrieve the gold group object
                user.groups.add(group) #add the user to the gold group
                username = user.username #get the username and store in variable username
                messages.success(request, 'Account was created for ' + username ) #sends flash message 
                return redirect('landingPage') # redirect user to login page
        context = {'form':form,} #context dictionary
        return render(request, 'userReg/registerFreemium.html', context)
    


#Register another buddy 


                  





