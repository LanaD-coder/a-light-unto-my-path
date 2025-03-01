"""
URL configuration for the Django app.

Defines route patterns using Django's `path` function.
"""
from django.urls import path
from .views import PostList

# URLConfigurations
urlpatterns = [
    path('my_blog/', PostList.as_view(), name='blog_home'),
    ]
