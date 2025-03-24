from django.urls import path, include
from django.shortcuts import redirect
from .views import login_signup_view, custom_logout_view
from . import views

urlpatterns = [
    # Redirect `accounts/` to `accounts/login_signup/`
    path('', lambda request: redirect(
        'login_signup'), name='accounts_redirect'),

    # Custom login/signup view
    path('login_signup/', login_signup_view, name='login_signup'),

    # Logout view
    path('logout/', views.custom_logout_view, name='logout_page'),

    path('', include('django.contrib.auth.urls')),

]
