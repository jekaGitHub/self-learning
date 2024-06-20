from django.db import models

from config import settings

from users.models import NULLABLE
from materials.models import Material


# Create your models here.
class Question(models.Model):
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Материал',
    )

    question = models.CharField(
        max_length=255,
        help_text="Укажите вопрос",
        verbose_name="Вопрос",
    )

    answer_right = models.CharField(
        max_length=50,
        help_text="Укажите правильный ответ",
        verbose_name="Правильный ответ",
    )

    answer_wrong_1 = models.CharField(
        max_length=50,
        help_text="Укажите неправильный ответ 1",
        verbose_name="Неправильный ответ 1",
    )

    answer_wrong_2 = models.CharField(
        max_length=50,
        help_text="Укажите неправильный ответ 2",
        verbose_name="Неправильный ответ 2",
    )

    answer_wrong_3 = models.CharField(
        max_length=50,
        help_text="Укажите неправильный ответ 3",
        verbose_name="Неправильный ответ 3",
    )

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец ответа",
        help_text="Укажите владельца ответа",
        **NULLABLE
    )

    answer = models.CharField(
        max_length=50,
        help_text="Укажите ваш ответ",
        verbose_name="Ответ",
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.SET_NULL,
        related_name="answers",
        help_text="Выберите вопрос",
        verbose_name="Вопрос",
        **NULLABLE
    )

    is_right = models.BooleanField(default=False, verbose_name='Ответ верный')

    def __str__(self):
        return f"{self.answer}"

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
