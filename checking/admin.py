from django.contrib import admin

from checking.models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "material", "question", "answer_right", "answer_wrong_1", "answer_wrong_2", "answer_wrong_3",)
    list_filter = ("material",)
    search_fields = ("question",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "is_right", "owner", "question", "answer",)
    list_filter = ("owner", "is_right",)
    search_fields = ("question",)
