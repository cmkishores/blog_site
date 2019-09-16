from django.test import TestCase
from .models import Post

class PostTest(TestCase):
	def setUp(self):
		'''This function inserts 
		dummy data into database
		to check during testing'''
		Post.objects.create(title='Test', content='This is test content. ', author='testauthor@testing.test')



	def test_post_content(self):
		post_object = Post.objects.get(pk=1)
		expected_object_title = f'{post_object.title}'
		expected_object_content = f'{post_object.content}'
		expected_object_author = f'{post_object.author}'
		self.assertEqual(expected_object_title,'Test')
		self.assertEqual(expected_object_content, 'This is test content. ')
		return self.assertEqual(expected_object_author, 'testauthor@testing.test')
# Create your tests here.
