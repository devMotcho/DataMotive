from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('dashboard:home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User Not Found.")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Something is Wrong, Try Again!")
        else:
            login(request, user)
            return redirect('dashboard:home') 
        
    return render(request, 'authentic/login.html', {})

def logoutUser(request):
    logout(request)
    return redirect('authentic:login')