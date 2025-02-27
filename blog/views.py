from django.shortcuts import render
# Views for handling blog-related requests.
from django.http import HttpResponse


# Create your views here.
def blog(request):  # Handles requests to the blog page.
    return HttpResponse('I have something to tell you...')
    # Returns an HTTP response with a message.
