from django.test import TestCase
from .models import Cake, Category


class CreateSweetsTestCase(TestCase):
    def setUp(self):
        self.test_category = Category.objects.create(title='TestCategoryTitle')
        self.test_cake = Cake.objects.create(name='TestCakeName', description='TestCakeDesc', text='TestCakeText', category=self.test_category)

    def test_create_category(self):
        self.assertEqual(self.test_category.title, 'TestCategoryTitle')
        self.assertEqual(self.test_category.cake_set.count(), 1)

    def test_create_cake(self):
        self.assertEqual(self.test_cake.name, 'TestCakeName')
        self.assertEqual(self.test_cake.category.title, 'TestCategoryTitle')
