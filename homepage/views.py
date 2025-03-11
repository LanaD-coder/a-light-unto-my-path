import requests
import random
from datetime import date
from django.shortcuts import render
from .models import DailyVerse

API_KEY = 'b3094e0c60a213765a11153a7c25b0c6'
BIBLE_ID = "https://api.scripture.api.bible/v1/bibles?language=ENG&abbreviation=NKJ&name=New%20King%20James"
VERSES = [ "JER.29.11", "PSA.23", "1COR.4.4-8", "PHP.4.13", "JHN.3.16",
    "ROM.8.28", "ISA.41.10", "PSA.46.1", "GAL.5.22-23", "HEB.11.1",
    "2TI.1.7", "1COR.10.13", "PRO.22.6", "ISA.40.31", "JOS.1.9",
    "HEB.12.2", "MAT.11.28", "ROM.10.9-10", "PHP.2.3-4", "MAT.5.43-44",

]

# Create your views here
def fetch_daily_verse():
    """ Fetches daily verse and stores it in db"""
    today = date.today()

    if DailyVerse.objects.filter(date=today).exists():
        print("Verse for today already exists.")
        return DailyVerse.objects.get(date=today)

    verse_id = random.choice(VERSES)
    url = f"https://api.scripture.api.bible/v1/bibles?language=ENG&abbreviation=NKJ&name=New%20King%20James{BIBLE_ID}/search?query={verse_id}"
    headers = {"api-key": API_KEY}

    response = requests.get(url, headers=headers)
    print(f"API Status code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        passage = data.get("data", {})
        verse_text = passage.get("content", "No verse avalable")
        reference = passage.get("reference", "Unknown")

        # Save to db
        verse_entry = DailyVerse.objects.create(
            date=today, verse_text=verse_text, reference=reference)

        return verse_entry
    return None

def homepage(request):

    daily_verse = fetch_daily_verse()
    return render(request, 'homepage/homepage.html',
                  { "daily_verse": daily_verse})
