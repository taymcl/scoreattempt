from django.shortcuts import render, redirect
from .models import Posts
from .forms import createPostForm
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
            postComment = post.postComment
            post.save()
            return redirect('communityPage')
    else:
        form = createPostForm()

    context = {
        'form': form
    }
    return render(request, 'community/addPost.html', context)
   







def addComment(request):
    return render(request, 'community/addComment.html')

def postDetails(request):
    return render(request, 'community/postDetails.html')

