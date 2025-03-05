"""
URL configuration for the Django app.

Defines route patterns using Django's `path` function.
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
]
