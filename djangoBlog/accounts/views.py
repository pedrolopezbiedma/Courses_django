from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
# Create your views here.

def handle_SignUp_Page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user
            login(request, user)
            return redirect('articleList')
        else:
            return render(request, 'accounts/signup.html', {'form': form })
            
    elif request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form })

def handle_Login_Page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in the user
            user = form.get_user()
            login(request, user)

            # Redirect the user where needed
            # If we have where we come from, we go back there. If not, to the article list 
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articleList')
        else:
            return render(request, 'accounts/login.html', { 'form': form })

    elif request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', { 'form': form })

def handle_Logout_Page(request):
    if request.method == 'POST':
        logout(request)
    return redirect('articleList')