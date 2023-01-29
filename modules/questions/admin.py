from django.contrib import admin
from .models import QuestionType, QuestionAndAnswers


@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ("question_type", "description")


@admin.register(QuestionAndAnswers)
class QuestionAndAnswersAdmin(admin.ModelAdmin):
    list_display = ("id", "user_email", "is_answered", "is_for_publication", "create_dt")
    ordering = ("-is_answered", "id")
