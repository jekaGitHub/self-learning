from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from materials.models import Category, Material
from django.views.generic import View, ListView, DetailView


class HomeListView(ListView):
    model = Category
    template_name = 'materials/index.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Category.objects.all()


class MaterialsView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        category = Category.objects.get(pk=pk)
        materials = Material.objects.filter(category=category)
        context = {
            "materials": materials,
        }
        return render(request, 'materials/materials.html', context)


class MaterialDetailView(DetailView):
    model = Material
