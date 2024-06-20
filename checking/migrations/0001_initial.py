# Generated by Django 4.2.2 on 2024-06-20 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("materials", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "question",
                    models.CharField(
                        help_text="Укажите вопрос",
                        max_length=255,
                        verbose_name="Вопрос",
                    ),
                ),
                (
                    "answer_right",
                    models.CharField(
                        help_text="Укажите правильный ответ",
                        max_length=50,
                        verbose_name="Правильный ответ",
                    ),
                ),
                (
                    "answer_wrong_1",
                    models.CharField(
                        help_text="Укажите неправильный ответ 1",
                        max_length=50,
                        verbose_name="Неправильный ответ 1",
                    ),
                ),
                (
                    "answer_wrong_2",
                    models.CharField(
                        help_text="Укажите неправильный ответ 2",
                        max_length=50,
                        verbose_name="Неправильный ответ 2",
                    ),
                ),
                (
                    "answer_wrong_3",
                    models.CharField(
                        help_text="Укажите неправильный ответ 3",
                        max_length=50,
                        verbose_name="Неправильный ответ 3",
                    ),
                ),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="materials.material",
                        verbose_name="Материал",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вопрос",
                "verbose_name_plural": "Вопросы",
            },
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "answer",
                    models.CharField(
                        help_text="Укажите ваш ответ",
                        max_length=50,
                        verbose_name="Ответ",
                    ),
                ),
                (
                    "is_right",
                    models.BooleanField(default=False, verbose_name="Ответ верный"),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите владельца ответа",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец ответа",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        blank=True,
                        help_text="Выберите вопрос",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="answers",
                        to="checking.question",
                        verbose_name="Вопрос",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ответ",
                "verbose_name_plural": "Ответы",
            },
        ),
    ]
