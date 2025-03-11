# accounts/urls.py
from django.urls import path, include
from .views import login_signup_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Registration page
    path('', login_signup_view, name='login_signup'),
    path('login/', login_signup_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view
        (template_name='accounts/logout.html'), name='logout'),
    path('', include('django.contrib.auth.urls')),
]
