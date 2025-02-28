from django.shortcuts import render
# Views for handling blog-related requests.
from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "post_list.html"

