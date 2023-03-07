# -------------------------------------------------------------------------------------------------------------------------
# Imports
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm #used for our user creation form
from .forms import CreateUserForm #used for our user creation form
from django.contrib.auth import authenticate, login, logout  #used for User Authentication
from django.contrib.auth.decorators import login_required #this is so we can restrict pages if you are not a logged in user
from django.contrib import messages #used to send a flash message
from django.contrib.auth.models import Group #used to access our groups
from userProfile.models import Profile #used to access our profile model
#-------------------------------------------------------------------------------------------------------------------------


#Base Views
def homePage(request):
    return render(request, 'base/homePage.html')

def portalPage(request):
    return render(request, 'base/portalPage.html')

#-------------------------------------------------------------------------------------------------------------------------


#UserReg Views


#Returns Login Page
def loginPage(request):
    return render(request, 'userReg/loginPage.html')



#Logic For Registration
def registerPage(request):
    if request.user.is_authenticated: #if the user is authenticated
        return redirect('portalPage') 
    else:
        return render(request, 'userReg/registerPage.html') #returns register page


def registerFreemium(request):
    if request.user.is_authenticated: #if the user is authenticated
        return redirect('portalPage') 
    else:
        form = CreateUserForm() #import our form
        if request.method == 'POST': #checking for a post request
            form = CreateUserForm(request.POST) #use our form
            if form.is_valid(): # if the regrestration is successfully filled out
                user = form.save() #save the information and store the created user object in a variable
                group = Group.objects.get(name='Freemium') #retrieve the gold group object
                user.groups.add(group) #add the user to the gold group
                username = user.username #get the username and store in variable username
                messages.success(request, 'Account was created for ' + username ) #sends flash message 
                profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/default.jpg')
                profile.save()
                
                return redirect('loginPage') # redirect user to login page
        context = {'form':form,} #context dictionary
        return render(request, 'userReg/registerFreemium.html', context)
    
def registerPremium(request):

    if request.user.is_authenticated: #if the user is authenticated
        return redirect('portalPage') 
    else:
        form = CreateUserForm() #import our form
        if request.method == 'POST': #checking for a post request
            form = CreateUserForm(request.POST) #use our form
            if form.is_valid(): # if the regrestration is successfully filled out
                user = form.save() #save the information and store the created user object in a variable
                group = Group.objects.get(name='Premium') #retrieve the gold group object
                user.groups.add(group) #add the user to the gold group
                username = user.username #get the username and store in variable username
                messages.success(request, 'Account was created for ' + username ) #sends flash message 
                profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/default.jpg')
                profile.save()
                
                return redirect('loginPage') # redirect user to login page
        context = {'form':form,} #context dictionary
        return render(request, 'userReg/registerPremium.html', context)



def registerUnlimited(request):
    if request.user.is_authenticated: #if the user is authenticated
        return redirect('portalPage') 
    else:
        form = CreateUserForm() #import our form
        if request.method == 'POST': #checking for a post request
            form = CreateUserForm(request.POST) #use our form
            if form.is_valid(): # if the regrestration is successfully filled out
                user = form.save() #save the information and store the created user object in a variable
                group = Group.objects.get(name='Unlimited') #retrieve the gold group object
                user.groups.add(group) #add the user to the gold group
                username = user.username #get the username and store in variable username
                messages.success(request, 'Account was created for ' + username ) #sends flash message 
                #Adds User to Profile Model
                profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/default.jpg')
                profile.save()
                
                return redirect('loginPage') # redirect user to login page
        context = {'form':form,} #context dictionary
        return render(request, 'userReg/registerUnlimited.html', context)


@login_required(login_url='loginPage')
def logoutUser(request):
    logout(request) #logout method from Django import
    return redirect('loginPage') # redirect user to back login page when a user logs out


def loginPage(request):
    if request.user.is_authenticated: #if we get a registered user send them to the portal
        return redirect('portalPage') #portal home page
    else:
        if request.method == 'POST': #check if we get a post request
            username = request.POST.get('username') #send username to username varible
            password = request.POST.get('password') #send password to password varible
            user = authenticate(request, username=username, password=password)
            if user is not None: #If we can see if there is a valid user
                login(request, user) #Django login method from import
                return redirect('portalPage') #sends user to the portal
            else: #if there is not a valid user
                messages.info(request, 'Username OR password is incorrect') #print flash message
        context = {}
        return render(request, 'userReg/loginPage.html', context) #show the login page again so they can re enter the right credentials






