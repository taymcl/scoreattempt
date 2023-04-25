
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileUpdateForm
from portal.models import Posts
from django.contrib.auth.models import User
from django.db import models
from userReg.models import Buddies
from django.contrib import messages
from django.shortcuts import get_object_or_404





# Create your views here.



@login_required
def userProfilePage(request):
    # Get the current user's posts
    user_posts = Posts.objects.filter(user=request.user).order_by('-date')
    user = request.user
    buddies = Buddies.objects.filter(user=user)
    # Get the form for updating the user's profile
    form = ProfileUpdateForm(instance=request.user.profile)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            firstName = profile.firstName
            lastName = profile.lastName
            age = profile.age
            bio = profile.bio
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            return redirect('userProfilePage')

    context = {
        'form': form,
        'user_posts': user_posts,
        'buddies': buddies,
    }
    
    return render(request, 'userProfile/userProfilePage.html', context)











