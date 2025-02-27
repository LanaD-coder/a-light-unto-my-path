from django.urls import path
from . import views  # Import views


# URLConfigurations
urlpatterns = [
    path('me/', views.about_me, name='about'),
]
