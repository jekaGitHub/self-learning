from django.contrib import admin

from materials.models import Category, Material


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description",)
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "contents", "image",)
    list_filter = ("category",)
    search_fields = ("title",)
