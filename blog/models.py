from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.utils import timezone

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    # image = models.ImageField(upload_to='blog_images/', default='default.jpg')
    image = CloudinaryField('image', blank=True, null=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    scheduled_publish_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug':self.slug})

    def is_scheduled_to_publish(self):
        return (
            self.scheduled_publish_date
            and self.status == 0
            and self.scheduled_publish_date <= timezone.now()
    )


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
         User, on_delete=models.CASCADE)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
