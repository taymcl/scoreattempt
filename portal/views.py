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

#imports for delete post:
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseForbidden

#test case
from userReg.models import Buddies









#portal views
def portalPage(request):
    posts = Posts.objects.all().order_by('-date')
    if request.method == 'POST':
        # Check if the "delete_post" parameter is present in the POST request
        if 'delete_post' in request.POST:
            post_id = request.POST.get('delete_post')
            try:
                post = Posts.objects.get(id=post_id)
                # Check if the current user is the owner of the post
                if request.user == post.user:
                    post.delete()
                else:
                    return HttpResponseForbidden()
            except Posts.DoesNotExist:
                pass
        else:
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


def delete_post(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.user == post.user:
        post.delete()
        messages.success(request, 'Post has been deleted successfully!')
    else:
        messages.warning(request, 'You are not authorized to delete this post.')
    return redirect('portalPage')


def regAnotherBuddy(request):
    return render(request, 'portal/regAnotherBuddy.html')




# test case 
def user_buddies(request):
    user = request.user  # assuming the user is logged in
    buddies = Buddies.objects.filter(user=user)
    return render(request, 'portal/user_buddies.html', {'buddies': buddies})

def game(request):
    return render(request, 'portal/game.html')


def freemiumPortal(request):
    return render(request, 'portal/freemiumPortal.html')








