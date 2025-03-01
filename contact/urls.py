"""
URL configuration for the Django app.

Defines route patterns using Django's `path` function.
"""
from django.urls import path
from .views import contact

urlpatterns = [
    path("", contact, name="contact"),
]