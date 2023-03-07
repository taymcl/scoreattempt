from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileUpdateForm


# Create your views here.
def profilePage(request):
    return render(request, 'userProfile/profilePage.html')


def editProfilePage(request):
    form = ProfileUpdateForm()
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
            return redirect('profilePage')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'form': form
    }
    return render(request, 'userProfile/editProfilePage.html', context)



       
 






    
   

