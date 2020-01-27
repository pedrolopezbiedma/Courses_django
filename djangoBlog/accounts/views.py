from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.

def handle_SignUp_Page(request):
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def handle_Login_Page(request):
    return render(request, 'accounts/login.html')