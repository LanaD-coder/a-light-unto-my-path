"""
URL configuration for the Django app.

Defines route patterns using Django's `path` function.
"""
from django.urls import path
from .views import PostList
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),  # List of all posts
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('register/', views.register, name='register'),
]
