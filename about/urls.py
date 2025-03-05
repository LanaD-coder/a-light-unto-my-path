"""
URL configuration for the Django app.

Defines route patterns using Django's `path` function.
"""
from django.urls import path
from . import views  # Import views


# URLConfigurations
urlpatterns = [
    path('', views.about, name='about'),
]


