from django.contrib import admin

from checking.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "material", "question", "answer_right", "answer_wrong_1", "answer_wrong_2", "answer_wrong_3",)
    list_filter = ("material",)
    search_fields = ("question",)
