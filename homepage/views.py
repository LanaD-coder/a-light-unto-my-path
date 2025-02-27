from django.shortcuts import render
# Views for handling homepage-related requests.
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    # Handles requests to the about page.
    return HttpResponse('Welcome to my blog!')
    # Returns an HTTP response with a message.
