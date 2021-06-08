from django.test import TestCase
from .models import Comment
from django.contrib.auth.models import User


class CreateCommentTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(username='TestUser', email='test@test.com', password='qwerty12345678')
        self.test_comment = Comment.objects.create(text='TestText', author=self.test_user)

    def test_create_user(self):
        self.assertEqual(self.test_user.email, 'test@test.com')

    def test_create_comment(self):
        self.assertEqual(self.test_comment.text, 'TestText')
        self.assertEqual(self.test_comment.author.username, 'TestUser')
