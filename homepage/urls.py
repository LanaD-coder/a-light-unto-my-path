from django.urls import path
from . import views


# URLConfigurations
urlpatterns = [
    path('home/', views.home_page)
]