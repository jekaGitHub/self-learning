from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from django.conf import settings
from materials.models import Material, Category
from checking.models import Question, Answer


# Тесты для моделей
class QuestionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='testuser@mail.ru', password='12345')
        self.category = Category.objects.create(name='Тестовая категория', description='Описание тестовой категории')
        self.material = Material.objects.create(title='Тестовый материал', category=self.category, contents='Тестовый контент')
        self.question = Question.objects.create(
            material=self.material,
            question='Какая столица Франции?',
            answer_right='Париж',
            answer_wrong_1='Берлин',
            answer_wrong_2='Лондон',
            answer_wrong_3='Мадрид'
        )

    def test_question_creation(self):
        self.assertIsInstance(self.question, Question)
        self.assertEqual(self.question.material, self.material)
        self.assertEqual(self.question.question, 'Какая столица Франции?')
        self.assertEqual(self.question.answer_right, 'Париж')
        self.assertEqual(self.question.answer_wrong_1, 'Берлин')
        self.assertEqual(self.question.answer_wrong_2, 'Лондон')
        self.assertEqual(self.question.answer_wrong_3, 'Мадрид')

    def test_question_str_method(self):
        self.assertEqual(str(self.question), 'Какая столица Франции?')


class AnswerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='testuser@mail.ru', password='12345')
        self.category = Category.objects.create(name='Тестовая категория', description='Описание тестовой категории')
        self.material = Material.objects.create(title='Тестовый материал', category=self.category, contents='Тестовый контент')
        self.question = Question.objects.create(
            material=self.material,
            question='Какая столица Франции?',
            answer_right='Париж',
            answer_wrong_1='Берлин',
            answer_wrong_2='Лондон',
            answer_wrong_3='Мадрид'
        )
        self.answer = Answer.objects.create(
            owner=self.user,
            answer='Париж',
            question=self.question,
            is_right=True
        )

    def test_answer_creation(self):
        self.assertIsInstance(self.answer, Answer)
        self.assertEqual(self.answer.owner, self.user)
        self.assertEqual(self.answer.answer, 'Париж')
        self.assertEqual(self.answer.question, self.question)
        self.assertTrue(self.answer.is_right)

    def test_answer_str_method(self):
        self.assertEqual(str(self.answer), 'Париж')


# Тесты для контроллера
class QuestionsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(email='testuser@mail.ru', password='12345')
        self.material = Material.objects.create(title='Тестовый материал')

        # Создаем несколько тестовых вопросов для материала
        self.question1 = Question.objects.create(
            material=self.material,
            question='Вопрос 1',
            answer_right='Ответ 1'
        )
        self.question2 = Question.objects.create(
            material=self.material,
            question='Вопрос 2',
            answer_right='Ответ 2'
        )

    def test_questions_view_get(self):
        self.client.login(email='testuser@mail.ru', password='12345')
        url = reverse('questions', args=[self.material.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checking/questions.html')
        self.assertIn('questions', response.context)
        self.assertIn('material', response.context)
        self.assertEqual(len(response.context['questions']), 2)  # Проверяем количество вопросов

    def test_questions_view_post_correct_answer(self):
        self.client.login(email='testuser@mail.ru', password='12345')
        url = reverse('questions', args=[self.material.pk])
        data = {'id': self.question1.id, 'answer': 'Ответ 1'}
        response = self.client.post(url, data, HTTP_REFERER='/')
        self.assertEqual(response.status_code, 302)  # Проверяем редирект после POST-запроса
        self.assertTrue(Answer.objects.filter(owner=self.user, question=self.question1, is_right=True).exists())

    def test_questions_view_post_incorrect_answer(self):
        self.client.login(email='testuser@mail.ru', password='12345')
        url = reverse('questions', args=[self.material.pk])
        data = {'id': self.question1.id, 'answer': 'Неверный ответ'}
        response = self.client.post(url, data, HTTP_REFERER='/')
        self.assertEqual(response.status_code, 302)  # Проверяем редирект после POST-запроса
        self.assertTrue(Answer.objects.filter(owner=self.user, question=self.question1, is_right=False).exists())
