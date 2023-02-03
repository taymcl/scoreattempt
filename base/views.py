from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'base/homePage.html')


def loginPage(request):
    return render(request, 'base/loginPage.html')
