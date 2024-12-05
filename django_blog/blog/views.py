from django.shortcuts import render, redirect
from .forms import SignupForm, loginForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = loginForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST , instance = user)
        if form.is_valid():
            form.save()
            messages.success(request , 'profile updated successfully')
            return redirect('profile')
    else:
        form = ProfileForm(instance = user)
    return render(request , 'blog/profile.html' , {'form':form})

# Create your views here.
