from datetime import date
from django.db import models


# Create your models here.
class DailyVerse(models.Model):
    date = models.DateField(auto_now_add=True, unique=True)
    verse_text = models.TextField()
    reference = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.reference} - {self.date}"
