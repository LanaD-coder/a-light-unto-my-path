from django.test import TestCase
from .models import Contact


class ContactModelTest(TestCase):

    def setUp(self):
        # Create a Contact object for use in the tests
        self.contact = Contact.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            subject="Inquiry",
            message="This is a test message"
        )

    def test_contact_creation(self):
        # Test that the Contact object is created correctly
        self.assertEqual(self.contact.name, "John Doe")
        self.assertEqual(self.contact.email, "john.doe@example.com")
        self.assertEqual(self.contact.subject, "Inquiry")
        self.assertEqual(self.contact.message, "This is a test message")

    def test_contact_str_method(self):
        # Test the __str__ method of the Contact model
        self.assertEqual(str(self.contact), "John Doe")

    def test_contact_created_at(self):
        # Test that created_at is set automatically
        self.assertIsNotNone(self.contact.created_at)
