from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'autocomplete': 'email', 'id': 'id_signup_email'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomLoginForm(AuthenticationForm):
    """
    Login Form with autocomplete & unique IDs
    """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'id': 'id_login_username', 'autocomplete': 'username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'id': 'id_login_password', 'autocomplete': 'current-password'}),
        help_text=None
    )


class CustomSignupForm(UserCreationForm):
    """
    Signup Form with autocomplete & unique IDs
    """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'id': 'id_signup_username', 'autocomplete': 'username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'id': 'id_signup_email', 'autocomplete': 'email'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'id': 'id_signup_password1', 'autocomplete': 'new-password'}),
        help_text=None
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'id': 'id_signup_password2', 'autocomplete': 'new-password'}),
        help_text=None
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
