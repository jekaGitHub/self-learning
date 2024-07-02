from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from materials.models import Material
from checking.models import Question, Answer
from django.views.generic import View


class QuestionsView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        material = Material.objects.get(pk=pk)
        questions = Question.objects.filter(material=material)
        for question in questions:
            question.answers_list = Answer.objects.filter(owner=self.request.user, question=question).last()
        context = {
            "questions": questions,
            "material": material,
        }
        return render(request, 'checking/questions.html', context)

    def post(self, *args, **kwargs):
        question_id = self.request.POST.get('id')
        question = Question.objects.get(id=question_id)
        answer = self.request.POST.get('answer')
        if answer == question.answer_right:
            Answer.objects.create(owner=self.request.user, answer=answer, question=question, is_right=True)
        else:
            Answer.objects.create(owner=self.request.user, answer=answer, question=question, is_right=False)
        return redirect(self.request.META['HTTP_REFERER'])
