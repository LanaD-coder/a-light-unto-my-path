from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    """
    Handles requests to the homepage.

    Returns an HTTP response with a welcome message.
    """
    return HttpResponse('Welcome to my blog!')