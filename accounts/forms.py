from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Change the id attribute, two forms clash
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_login_username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'id_login_password'}))

class CustomSignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_signup_username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'id_signup_email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'id_signup_password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'id_signup_password2'}))