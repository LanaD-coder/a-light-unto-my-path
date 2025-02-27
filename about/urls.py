from django.urls import path
from . import views


# URLConfigurations
urlpatterns = [
    path('me/', views.about_me)
]
