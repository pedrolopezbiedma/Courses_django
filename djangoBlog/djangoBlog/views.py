#from django.http import HttpResponse
from django.shortcuts import render 

def handle_Home_Page(request):
    #return HttpResponse('About page')
    return render(request, 'homepage.html')    


def handle_About_Page(request):
    #return HttpResponse('About page')
    return render(request, 'about.html')
