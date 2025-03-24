from django.contrib import admin
from .models import Question, Answer


class AnswerInLine(admin.TabularInline):
    """
    Register your models here.
    """
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
