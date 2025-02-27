from django.shortcuts import render
# Views for handling about-related requests.
from django.http import HttpResponse


# Create your views here.
def about_me(request):
    # Handles requests to the about page.
    return HttpResponse('About me...')
    # Returns an HTTP response with a message.
