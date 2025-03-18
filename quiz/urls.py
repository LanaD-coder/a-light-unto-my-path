# urls.py
from django.urls import path
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
)

app_name = 'quiz'

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz_main'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
]