"""
URL configuration for the Django app.

Defines route patterns using Django's `path` function.
"""
from . import views
from django.urls import path



# URLConfigurations
urlpatterns = [
    path('my_blog/', views.PostList.as_view(), name='about'),
]
