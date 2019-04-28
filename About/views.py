from django.shortcuts import render

def myAbout(request):

    return render(request, 'About/about.html')

# Create your views here.
