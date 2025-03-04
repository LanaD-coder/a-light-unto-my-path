"""
URL configuration for the Django app.

Defines route patterns using Django's `path` function.
"""
from django.urls import path
from .views import contact_view

urlpatterns = [
    path("", contact_view, name="contact"),
]