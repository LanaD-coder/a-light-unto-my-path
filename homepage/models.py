from django.db import models
import random

# Create your models here.
class BibleVerse(models.Model):
    verse_text = models.TextField()
    reference = models.CharField(max_length=255)

    def __str__(self):
        return self.reference

    def get_random_verse():
        verses = list(BibleVerse.objects.all())
        return random.choice(verses) if verses else None