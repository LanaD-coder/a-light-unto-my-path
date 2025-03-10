"""
URL configuration for the Django app.

Defines route patterns using Django's `path` function.
"""
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Blog - Homepage
    path('', views.PostList.as_view(), name='post_list'),
    # Post detail page
    path('post/<slug:slug>/',
         views.PostDetailView.as_view(), name='post_detail'),
    # New path for comment_view
    path('post/<slug:slug>/comment/', views.comment_view, name='comment_view'),
]
