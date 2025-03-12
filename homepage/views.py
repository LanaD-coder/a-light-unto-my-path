import requests
import random
from datetime import date
from django.shortcuts import render
from .models import DailyVerse

API_KEY = 'b3094e0c60a213765a11153a7c25b0c6'
BIBLE_ID = "de4e12af7f28f599-02"

VERSES = [ "JER.29.11", "PSA.23", "1COR.4.4-8", "PHP.4.13", "JHN.3.16",
    "ROM.8.28", "ISA.41.10", "PSA.46.1", "GAL.5.22-23", "HEB.11.1",
    "2TI.1.7", "1COR.10.13", "PRO.22.6", "ISA.40.31", "JOS.1.9",
    "HEB.12.2", "MAT.11.28", "ROM.10.9-10", "PHP.2.3-4", "MAT.5.43-44",

]

# Create your views here
def get_daily_verse():
    """ Fetches the daily verse and stores it in the database """
    today = date.today()

    # Check if today's verse already exists
    if DailyVerse.objects.filter(date=today).exists():
        return DailyVerse.objects.get(date=today)

    # Pick a random verse
    verse_id = random.choice(VERSES)
    url = f"https://api.scripture.api.bible/v1/bibles/{BIBLE_ID}/passages/{verse_id}"
    headers = {"api-key": API_KEY}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get("data", {})
        verse_text = data.get("content", "No verse available")
        reference = data.get("reference", "Unknown")

        # Save to database
        verse_entry = DailyVerse.objects.create(
            date=today, verse_text=verse_text, reference=reference
        )
        return verse_entry
    return None

def homepage(request):
    """ View function for homepage """
    daily_verse = get_daily_verse()
    return render(request, 'homepage/homepage.html', {"daily_verse": daily_verse})
