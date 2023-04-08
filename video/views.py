from django.shortcuts import render

# Create your views here.
def videoPage(request):
    return render(request, 'video/videoPage.html', {})