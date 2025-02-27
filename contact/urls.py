from django.urls import path
from . import views


# URLConfigurations
urlpatterns = [
    path('chat/', views.contact)
]
