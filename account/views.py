from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from .models import User

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'patient':
                    return redirect('patient_dashboard')
                elif user.user_type == 'doctor':
                    return redirect('doctor_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def patient_dashboard(request):
    if request.user.user_type != 'patient':
        messages.error(request, 'Access denied. Patients only.')
        return redirect('login')
    return render(request, 'accounts/patient_dashboard.html', {'user': request.user})

@login_required
def doctor_dashboard(request):
    if request.user.user_type != 'doctor':
        messages.error(request, 'Access denied. Doctors only.')
        return redirect('login')
    return render(request, 'accounts/doctor_dashboard.html', {'user': request.user})


