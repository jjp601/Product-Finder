from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/register.html', {'error': 'Username has already been taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], request.POST['email'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'accounts/register.html', {'error': 'Passwords must match.'})
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password.'})
    else:    
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
