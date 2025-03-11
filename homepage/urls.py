"""
URL configuration for the Django app.

Defines route patterns using Django's `path` function.
"""
from django.urls import path
from .views import homepage, fetch_daily_verse
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("get_daily_verse/", fetch_daily_verse, name="fetch_daily_verse"),
]
