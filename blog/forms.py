# blog/forms.py
from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'comment-textarea',
                'rows': 4,  # Adjust the height
                'placeholder': 'Write your comment here...',
            })
        }

class PostForm(forms.ModelForm):
    class Mata:
        model = Post
        fields = ['title', 'content']