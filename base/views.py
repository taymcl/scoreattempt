from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  #used for User Authentication
from django.contrib.auth.decorators import login_required #this is so we can restrict pages if you are not a logged in user
from django.contrib import messages #used to send a flash message



# base views

#logic for logging in
def landingPage(request):
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
                messages.error(request, 'Username OR password is incorrect') #print flash message
        context = {}
        return render(request, 'base/landingPage.html', context) #show the login page again so they can re enter the right credentials


#logout view
@login_required(login_url='landingPage')
def logoutUser(request):
    logout(request) #logout method from Django import
    return redirect('landingPage') # redirect user to back login page when a user logs out



#userReg Views
def registerPage(request):
    return render(request, 'userReg/registerPage.html')

def registerWhale(request):
    return render(request, 'userReg/registerWhale.html')

def registerTurtle(request):
    return render(request, 'userReg/registerTurtle.html')


def registerSeal(request):
    return render(request, 'userReg/registerSeal.html')


def registerSeagull(request):
    return render(request, 'userReg/registerSeagull.html')


def registerDolphin(request):
    return render(request, 'userReg/registerDolphin.html')


def registerFreemium(request):
    return render(request, 'userReg/registerFreemium.html')



# userProfile views
def userProfilePage(request):
    return render(request, 'userProfile/userProfilePage.html')


#community views
def communityPage(request):
    return render(request, 'community/communityPage.html')

#portal views

def game(request):
    return render(request, 'portal/game.html')



def portalPage(request):
    return render(request, 'portal/portalPage.html')

def addPostPage(request):
    return render(request, 'portal/addPostPage.html')

def regAnotherBuddy(request):
    return render(request, 'portal/regAnotherBuddy.html')

def freemiumPortal(request):
    return render(request, 'portal/freemiumPortal.html')

#video views
def videoPage(request):
    return render(request, 'video/videoPage.html', {})

def video_detail(request):
    return render(request, 'video/video_detail.html', {})





#buddyPages views
def whale(request):
    return render(request, 'buddyPages/whale.html')

def turtle(request):
    return render(request, 'buddyPages/turtle.html')

def seal(request):
    return render(request, 'buddyPages/seal.html')

def seagull(request):
    return render(request, 'buddyPages/seagull.html')

def dolphin(request):
    return render(request, 'buddyPages/dolphin.html')



#regBuddy2 views
def registerDolphin2(request):
    return render(request, 'regBuddy2/registerDolphin2.html')

def registerSeagull2(request):
    return render(request, 'regBuddy2/registerSeagull2.html')

def registerSeal2(request):
    return render(request, 'regBuddy2/registerSeal2.html')

def registerTurtle2(request):
    return render(request, 'regBuddy2/registerTurtle2.html')

def registerWhale2(request):
    return render(request, 'regBuddy2/registerWhale2.html')


def user_buddies(request):
    return render(request, 'portal/user_buddies.html')





