from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import CustomUserCreationForm

class CustomUserCreationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_missing_email(self):
        form_data = {
            'username': 'testuser',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_password_mismatch(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'StrongPass123!',
            'password2': 'WrongPass123!'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_duplicate_username(self):
        User.objects.create_user(username='testuser', email='testuser@example.com', password='StrongPass123!')
        form_data = {
            'username': 'testuser',
            'email': 'newemail@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)