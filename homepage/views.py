from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.urls import reverse

def homepage(request):
    API_URL = 'https://api.scripture.api.bible/v1/swagger.json'

    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = respons.json()
    except requests.exceptions.RequestException as e:
        data = {'error': 'Failed to fetch data'}

    return render(request, 'homepage/homepage.html', {"api_data": data})

