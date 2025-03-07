# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def login_signup_view(request):
    """
    Handles both login and signup logic.
    """
    if request.method == 'POST':
        # Handle login
        if 'login' in request.POST:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                # User authentication
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('homepage')  # Redirect to homepage after login
        # Handle signup
        elif 'signup' in request.POST:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')  # Redirect to login after successful signup
    else:
        # If GET request, initialize empty forms
        login_form = AuthenticationForm()
        signup_form = CustomUserCreationForm()

    return render(
        request,
        'accounts/login_signup.html',
        {'login_form': login_form, 'signup_form': signup_form}
    )