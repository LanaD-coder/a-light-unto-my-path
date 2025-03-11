from django.contrib import admin
from .models import DailyVerse

# Register your models here.
@admin.register(DailyVerse)

class DailyVerseAdmin(admin.ModelAdmin):
    list_display = ('reference', 'date')
    ordering = ['-date']
