from django.shortcuts import render

# Create your views here.
def whale(request):
    return render(request, 'buddyPages/whale.html')

def turtle(request):
    return render(request, 'buddyPages/turtle.html')

def seal(request):
    return render(request, 'buddyPages/seal.html')

def seagull(request):
    return render(request, 'buddyPages/seagull.html')

def dolphin(request):
    return render(request, 'buddyPages/dolphin.html')

