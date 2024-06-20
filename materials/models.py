from django.db import models

from users.models import NULLABLE


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Название раздела",
        help_text="Укажите название раздела",
    )
    description = models.TextField(
        verbose_name="Описание раздела", help_text="Укажите описание раздела", **NULLABLE
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"


class Material(models.Model):
    title = models.CharField(
        max_length=150,
        help_text="Укажите название материала",
        verbose_name="Название материала",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="materials",
        help_text="Выберите раздел",
        verbose_name="Раздел",
        **NULLABLE,
    )

    contents = models.TextField(
        verbose_name="Содержание материала", help_text="Укажите содержание материала", **NULLABLE
    )
    image = models.ImageField(
        upload_to="materials/preview",
        verbose_name="Превью",
        help_text="Загрузите фото",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
