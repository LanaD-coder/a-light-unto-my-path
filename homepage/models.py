from django.db import models
from datetime import date


# Create your models here.
class DailyVerse(models.Model):
    date = models.DateField(auto_now_add=True, unique=True)
    verse_text = models.TextField()
    reference = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.reference} - {self.verse_text[:50]}..."
