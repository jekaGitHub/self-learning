from django.test import TestCase, Client
from django.urls import reverse
from materials.models import Category, Material
from users.models import User


# Тесты для моделей
class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Тестовая категория",
            description="Это Тестовая категория"
        )

    def test_category_creation(self):
        self.assertIsInstance(self.category, Category)
        self.assertEqual(self.category.name, "Тестовая категория")
        self.assertEqual(self.category.description, "Это Тестовая категория")

    def test_category_str_method(self):
        self.assertEqual(str(self.category), "Тестовая категория")


class MaterialModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Тестовая категория",
            description="Это Тестовая категория"
        )
        self.material = Material.objects.create(
            title="Тестовый материал",
            category=self.category,
            contents="Это контент для тестового материала",
        )

    def test_material_creation(self):
        self.assertIsInstance(self.material, Material)
        self.assertEqual(self.material.title, "Тестовый материал")
        self.assertEqual(self.material.category, self.category)
        self.assertEqual(self.material.contents, "Это контент для тестового материала")

    def test_material_str_method(self):
        self.assertEqual(str(self.material), "Тестовый материал")


# Тесты для контроллеров
class HomeListViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name="Тестовая категория",
            description="Это Тестовая категория"
        )

    def test_home_list_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_list_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'materials/index.html')

    def test_home_list_view_context(self):
        response = self.client.get(reverse('home'))
        self.assertIn('object_list', response.context)
        self.assertEqual(len(response.context['object_list']), 1)
        self.assertEqual(response.context['object_list'][0], self.category)


class MaterialsViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(email='testuser@mail.ru', password='12345')
        self.category = Category.objects.create(
            name="Тестовая категория",
            description="Это Тестовая категория"
        )
        self.material = Material.objects.create(
            title="Тестовый материал",
            category=self.category,
            contents="Это контент для тестового материала",
        )

    def test_materials_view_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('materials', args=[self.category.pk]))
        self.assertRedirects(response, f'/accounts/login/?next=/chapters{self.category.pk}/materials/')

    def test_materials_view_logged_in(self):
        self.client.login(email='testuser@mail.ru', password='12345')
        response = self.client.get(reverse('materials', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'materials/materials.html')
        self.assertContains(response, self.material.title)

    def test_materials_view_status_code(self):
        self.client.login(email='testuser@mail.ru', password='12345')
        response = self.client.get(reverse('materials', args=[self.category.pk]))
        self.assertEqual(response.status_code, 200)

    def test_materials_view_template(self):
        self.client.login(email='testuser@mail.ru', password='12345')
        response = self.client.get(reverse('materials', args=[self.category.pk]))
        self.assertTemplateUsed(response, 'materials/materials.html')


class MaterialDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name="Тестовая категория",
            description="Это Тестовая категория"
        )
        self.material = Material.objects.create(
            title="Тестовый материал",
            category=self.category,
            contents="Это контент для тестового материала",
        )

    def test_material_detail_view(self):
        response = self.client.get(reverse('material-detail', args=[self.material.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'materials/material_detail.html')
        self.assertContains(response, self.material.title)
        self.assertContains(response, self.material.contents)
