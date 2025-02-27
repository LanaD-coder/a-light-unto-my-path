from django.shortcuts import render
# Views for handling contact-related requests.
from django.http import HttpResponse


# Create your views here.
def contact(request):
    # Handles requests to the contact page.
    return HttpResponse('Let´s chat.')
    # Returns an HTTP response with a message.
