"""
URL configuration for the Django app.

Defines route patterns using Django's `path` function.
"""
from django.urls import path
from .views import homepage

urlpatterns = [
    path("", homepage, name="homepage"),
]
