from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.

def handle_SignUp_Page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Log the user
            return redirect('articleList')
        else:
            return render(request, 'accounts/signup.html', {'form': form })
            
    elif request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form })

def handle_Login_Page(request):
    return render(request, 'accounts/login.html')
