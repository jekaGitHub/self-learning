from django.shortcuts import render

from materials.models import Category, Material
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView


class HomeListView(ListView):
    model = Category
    template_name = 'materials/index.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Category.objects.all()
