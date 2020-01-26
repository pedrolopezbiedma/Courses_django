from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def handle_SignUp_Page(request):
    return render(request, 'accounts/signup.html')

def handle_Login_Page(request):
    return render(request, 'accounts/login.html')