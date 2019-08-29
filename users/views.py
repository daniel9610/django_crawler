from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from users.models import Profile


# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username'];
        password = request.POST['password'];
        password_confirmation = request.POST['password_confirmation']
        if password != password_confirmation:
            return render(request, 'user/signup.html', {'error':'password confirmation does not match'})
        user = User.objects.create_user(username=username, password=password)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name'] 
        user.email = request.POST['email'] 
        profile = Profile(user=user)
        profile.save()
        return redirect('login')
    return render(request, 'user/signup.html')

def login_view(request):
    if request.method == "POST":
        print ('*' * 10)
        username = request.POST['username']
        password = request.POST['password']
        user =   authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'user/login.html', {'error':'Invalid username and password'})
    return render(request, 'user/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



