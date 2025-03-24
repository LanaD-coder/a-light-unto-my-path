from django.db import models
from datetime import date


class DailyVerse(models.Model):
    """
    Create your models here.
    """
    date = models.DateField(auto_now_add=True, unique=True)
    verse_text = models.TextField()
    reference = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.reference} - {self.verse_text[:50]}..."
