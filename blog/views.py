from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from .models import Post
from .forms import CommentForm
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Post List View
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html"
    paginate_by = 6


# View for a single post with comments
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']

        # Add approved comments
        context['comment'] = post.comment.filter(approved=True)

        # Add context for the comment form if user is logged in
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm()

        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()

        # Handle comment submission only for authenticated users
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                # Save the comment and link it to the post
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()

                # Redirect to the same page after saving the comment
                return self.get(request, *args, **kwargs)

        else:
            return HttpResponseForbidden("You need to be logged in to comment.")

# Comment view for handling comment submission
def comment_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Only allow comments from authenticated users
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You need to be logged in to comment.")

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create and save the comment
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            # Redirect back to the post detail page after commenting
            return redirect('blog:post_detail', slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', {'form': form, 'post': post})

# Handle user sign-up
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('blog:post_list')  # Redirect
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
