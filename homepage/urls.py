"""
URL configuration for the Django app.

Defines route patterns using Django's `path` function.
"""
from django.urls import path
from .views import homepage, get_daily_verse
from . import views

urlpatterns = [
    path("", homepage, name="homepage"),
    path("get_daily_verse/", get_daily_verse, name="get_daily_verse"),
]
