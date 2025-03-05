from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully signed up, Welcome!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

