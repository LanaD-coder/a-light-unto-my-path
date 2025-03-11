# accounts/urls.py
from django.urls import path
from .views import login_signup_view

urlpatterns = [
    path('accounts/', login_signup_view, name='login_signup'),  # Registration page
    path('accounts/login/', login_signup_view, name='login')
]
