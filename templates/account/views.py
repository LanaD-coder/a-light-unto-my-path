
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})