from django.urls import path
from . import views
"""
URL configuration for the Django app.

Defines route patterns using Django's `path` function.
"""


# URLConfigurations
urlpatterns = [
    path('chat/', views.contact, name='contact'),
]
