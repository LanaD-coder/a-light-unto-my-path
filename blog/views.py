from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Post List View
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html"
    paginate_by = 8


# View for a single post with comments
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object  # The current post instance

        # Fetch previous and next posts based on created date
        context['previous_post'] = Post.objects.filter(created_on__lt=post.created_on).order_by('-created_on').first()
        context['next_post'] = Post.objects.filter(created_on__gt=post.created_on).order_by('created_on').first()

        # Fetch comments and paginate them
        comments = post.comments.filter(approved=True).order_by('-created_on')
        paginator = Paginator(comments, 5)
        page_number = self.request.GET.get('page')
        context['comments'] = paginator.get_page(page_number)

        # If the user is logged in, provide a comment form
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
                return redirect('blog:post_detail', slug=post.slug)

        return HttpResponseForbidden \
                ("You need to be logged in to comment.")

@login_required
def comment_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been added.")
            return redirect('blog:post_detail', slug=post.slug)

    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', {'form': form, 'post': post})

# Update existing Comment
class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['body']
    template_name = 'blog/edit_comment.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'slug': self.object.post.slug})

    def get_queryset(self):
        # Ensure users can only edit their own comments
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

# Delete a comment
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'slug': self.object.post.slug})

    def get_queryset(self):
        # Ensure users can only delete their own comments
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

# Handle user sign-up
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('blog:post_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})