# Imports
from django.shortcuts import render, redirect
from .forms import createPostForm #used for our user creation form
from django.contrib.auth import authenticate, login, logout  #used for User Authentication
from django.contrib.auth.decorators import login_required #this is so we can restrict pages if you are not a logged in user
from django.contrib import messages #used to send a flash message
from django.contrib.auth.models import Group #used to access our groups
from userProfile.models import Profile  #used to access our profile model
from .models import Posts
from django.contrib.auth.models import User








#portal views
def portalPage(request):
    posts = Posts.objects.all().order_by('-date')
    if request.method == 'POST':
        form = createPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            postBody = post.postBody
            post.save()
            return redirect('portalPage')
    else:
        form = createPostForm()

    context = {
        'form': form,
        'posts': posts
    }
    return render(request, 'portal/portalPage.html', context)





