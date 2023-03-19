from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts, Comments
from .forms import createPostForm, createCommentForm
from django.views import generic


# Create your views here.

def communityPage(request):
    posts = Posts.objects.all()
    return render(request, 'community/communityPage.html', {'posts': posts})


def addPost(request):
    form = createPostForm()
    if request.method == 'POST':
        form = createPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            postTitle = post.postTitle
            postBody = post.postBody
            post.save()
            return redirect('communityPage')
    else:
        form = createPostForm()

    context = {
        'form': form
    }
    return render(request, 'community/addPost.html', context)


def addComment(request, pk):
    post = Posts.objects.get(pk=pk)
    form = createCommentForm()
    if request.method == 'POST':
        form = createCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('communityPage')
    else:
        form = createCommentForm()

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'community/addComment.html', context)


def postDetails(request):
    return render(request, 'community/postDetails.html')
