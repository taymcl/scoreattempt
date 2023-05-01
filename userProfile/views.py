from urllib.request import Request

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import csrf_token
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.middleware.csrf import get_token
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from .models import Profile, HighScores
from .forms import ProfileUpdateForm
from portal.models import Posts
from django.contrib.auth.models import User
from django.db import models
from userReg.models import Buddies
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.utils.functional import SimpleLazyObject
from django.contrib.auth import authenticate, get_user_model

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


def save_high_score(request):
    if request.method == 'POST':
        user = request.user
        score = int(request.POST.get('score'))
        if HighScores.objects.filter(user=user).exists():
            high_score = user.highscore
            if score > high_score.score:
                high_score.score = score
            high_score.save()
        else:
            HighScores.objects.create(user=user, score=score)

        # Generate a new CSRF token
        csrf_token = get_token(request)

        # Add the Access-Control-Allow-Origin and CSRF headers to the response
        response = JsonResponse({'csrf_token': csrf_token})
        response['Access-Control-Allow-Origin'] = 'http://localhost:8002/'
        response['Access-Control-Allow-Credentials'] = True
        response['X-CSRFToken'] = csrf_token

        return response
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed.'})
