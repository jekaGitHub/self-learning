from django.shortcuts import render

from materials.models import Material
from checking.models import Question
from django.views.generic import View


class QuestionsView(View):
    def get(self, request, pk, *args, **kwargs):
        material = Material.objects.get(pk=pk)
        questions = Question.objects.filter(material=material)
        context = {
            "questions": questions,
        }
        return render(request, 'checking/questions.html', context)
