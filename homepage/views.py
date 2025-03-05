from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.urls import reverse

def homepage(request):
    return render(request, 'homepage/homepage.html/')
