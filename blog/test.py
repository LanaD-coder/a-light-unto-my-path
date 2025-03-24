from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from django.utils import timezone
from datetime import timedelta


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=self.user,
            content="This is a test post",
            status=0,
            scheduled_publish_date=timezone.now() + timedelta(days=1)
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.status, 0)

    def test_post_str_method(self):
        self.assertEqual(str(self.post), "Test Post | written by testuser")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.post.get_absolute_url(), f"/blog/{self.post.slug}/")

    def test_is_scheduled_to_publish(self):
        self.assertFalse(self.post.is_scheduled_to_publish())
        self.post.scheduled_publish_date = timezone.now() - timedelta(days=1)
        self.assertTrue(self.post.is_scheduled_to_publish())


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='commentuser', password='testpass')
        self.post = Post.objects.create(
            title="Another Test Post",
            slug="another-test-post",
            author=self.user,
            content="This is another test post",
            status=1
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body="This is a test comment",
            approved=False
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.body, "This is a test comment")
        self.assertEqual(
            self.comment.post.title, "Another Test Post")
        self.assertFalse(self.comment.approved)

    def test_comment_str_method(self):
        self.assertEqual(
            str(self.comment), "Comment This is a test comment by commentuser")
