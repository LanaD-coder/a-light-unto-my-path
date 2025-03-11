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
                    # Redirect to homepage after login
                    return redirect('homepage')
                else:
                    messages.error(request, "Invalid username or password.")

        # Handle signup
        elif 'signup' in request.POST:
            signup_form = CustomUserCreationForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request, "Account created! You can now log in.")
                # Redirect to login after successful signup
                return redirect('login_signup')
            else:
                messages.error(request, "Signup failed. Please check the details.")
    else:
        # If GET request, initialize empty forms
        login_form = AuthenticationForm()
        signup_form = CustomUserCreationForm()

    return render(
        request,
        'accounts/login_signup.html',
        {'login_form': login_form, 'signup_form': signup_form}
    )
