from django.shortcuts import render


#Returns Register Page
def registerPage(request):
    return render(request, 'userReg/registerPage.html')

#Returns Login Page
def loginPage(request):
    return render(request, 'userReg/loginPage.html')

#this is the view for the home page
def homePage(request):
    return render(request, 'base/homePage.html')    


def portalPage(request):
    return render(request, 'base/portalPage.html')

def profilePage(request):
    return render(request, 'userProfile/profilePage.html')

def editProfilePage(request):
    return render(request, 'userProfile/editProfilePage.html')


#Views for community app
def communityPage(request):
    return render(request, 'community/communityPage.html')

def addPost(request):
    return render(request, 'community/addPost.html')

def addComment(request):
    return render(request, 'community/addComment.html')

def postDetails(request):
    return render(request, 'community/postDetails.html')

