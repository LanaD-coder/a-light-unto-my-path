# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomLoginForm

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def login_signup_view(request):
    """
    Handles both login and signup.
    """
    login_form = CustomLoginForm()  # Use your custom form
    signup_form = CustomUserCreationForm()

    if request.method == 'POST':
        # Handle login
        if 'login' in request.POST:
            login_form = CustomLoginForm(data=request.POST)  # Use custom form
            if login_form.is_valid():
                # Authenticate user
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('homepage')
                else:
                    messages.error(request, "Invalid username or password.")

        # Handle signup
        elif 'signup' in request.POST:
            signup_form = CustomUserCreationForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request, "Account created! You can now log in.")
                return redirect('login_signup')
            else:
                messages.error(request, "Signup failed. Please check the details.")

    return render(
        request,
        'accounts/login_signup.html',
        {'login_form': login_form, 'signup_form': signup_form}
    )

def custom_logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')

