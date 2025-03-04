from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import DetailView
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 6


#View a single post with comments
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']

        # Add approved comments
        context['comment'] = post.comment.filter(approved=True)

        # Add context to comments if user is logged in
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm()

        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()

        # Add comments only when user is auth.
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                # Save comment links to post
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()

                # Redirect to same page after save
                return self.get(request, *args, ** kwargs)

        else:
            return HttpResponseForbidden("You need to be logged in to comment.")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})