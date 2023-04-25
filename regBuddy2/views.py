from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from portal.models import Posts
from django.contrib.auth.models import User
from django.db import models
from userReg.models import Buddies
from django.contrib import messages
from django.shortcuts import get_object_or_404
from userReg.forms import registerAnotherBuddy


# Create your views here.
@login_required # Add a login_required decorator if you require authentication
def registerDolphin2(request):
    form = registerAnotherBuddy()
    if request.method == 'POST':
        form = registerAnotherBuddy(request.POST)
        if form.is_valid():
            registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
            if registration_code != 'dolphin': # check if the registration code is correct
                messages.error(request, 'Invalid registration code.') # send an error message
                return redirect('registerDolphin2') # redirect back to the same page
            else:
                buddy = Buddies(name='dolphin', picture='static/images/characters/dolphin.png', user=request.user) # set the user field with the current user
                buddy.save() # save the new Buddies instance

                messages.success(request, 'Another buddy was registered.')
                return redirect('portalPage')
    context = {'form': form}
    return render(request, 'regBuddy2/registerDolphin2.html', context)


@login_required # Add a login_required decorator if you require authentication
def registerWhale2(request):
    form = registerAnotherBuddy()
    if request.method == 'POST':
        form = registerAnotherBuddy(request.POST)
        if form.is_valid():
            registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
            if registration_code != 'whale': # check if the registration code is correct
                messages.error(request, 'Invalid registration code.') # send an error message
                return redirect('registerWhale2') # redirect back to the same page
            else:
                buddy = Buddies(name='whale', picture='static/images/characters/whale.png', user=request.user) # set the user field with the current user
                buddy.save() # save the new Buddies instance

                messages.success(request, 'Another buddy was registered.')
                return redirect('portalPage')
    context = {'form': form}
    return render(request, 'regBuddy2/registerWhale2.html', context)


@login_required # Add a login_required decorator if you require authentication
def registerSeagull2(request):
    form = registerAnotherBuddy()
    if request.method == 'POST':
        form = registerAnotherBuddy(request.POST)
        if form.is_valid():
            registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
            if registration_code != 'seagull': # check if the registration code is correct
                messages.error(request, 'Invalid registration code.') # send an error message
                return redirect('registerSeagull2') # redirect back to the same page
            else:
                buddy = Buddies(name='seagull', picture='static/images/characters/seagull.png', user=request.user) # set the user field with the current user
                buddy.save() # save the new Buddies instance

                messages.success(request, 'Another buddy was registered.')
                return redirect('portalPage')
    context = {'form': form}
    return render(request, 'regBuddy2/registerSeagull2.html', context)


@login_required # Add a login_required decorator if you require authentication
def registerSeal2(request):
    form = registerAnotherBuddy()
    if request.method == 'POST':
        form = registerAnotherBuddy(request.POST)
        if form.is_valid():
            registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
            if registration_code != 'seal': # check if the registration code is correct
                messages.error(request, 'Invalid registration code.') # send an error message
                return redirect('registerSeal2') # redirect back to the same page
            else:
                buddy = Buddies(name='seal', picture='static/images/characters/seal.png', user=request.user) # set the user field with the current user
                buddy.save() # save the new Buddies instance

                messages.success(request, 'Another buddy was registered.')
                return redirect('portalPage')
    context = {'form': form}
    return render(request, 'regBuddy2/registerSeal2.html', context)

@login_required # Add a login_required decorator if you require authentication
def registerTurtle2(request):
    form = registerAnotherBuddy()
    if request.method == 'POST':
        form = registerAnotherBuddy(request.POST)
        if form.is_valid():
            registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
            if registration_code != 'turtle': # check if the registration code is correct
                messages.error(request, 'Invalid registration code.') # send an error message
                return redirect('registerTurtle2') # redirect back to the same page
            else:
                buddy = Buddies(name='turtle', picture='static/images/characters/turtle.png', user=request.user) # set the user field with the current user
                buddy.save() # save the new Buddies instance

                messages.success(request, 'Another buddy was registered.')
                return redirect('portalPage')
    context = {'form': form}
    return render(request, 'regBuddy2/registerTurtle2.html', context)








