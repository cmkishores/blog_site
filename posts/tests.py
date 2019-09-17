from django.test import TestCase
from .models import Post
from django.urls import reverse


class PostTest(TestCase):
	def setUp(self):
		'''This function inserts 
		dummy data into database
		to check during testing'''
		self.post = Post.objects.create(title='Test', content='abcd', author='testauthor@testing.test')



	def test_post_content(self):
		post_object = Post.objects.get(pk=1)
		expected_object_title = f'{post_object.title}'
		expected_object_content = f'{post_object.content}'
		expected_object_author = f'{post_object.author}'
		self.assertEqual(expected_object_title,'Test')
		self.assertEqual(expected_object_content, 'abcd')
		return self.assertEqual(expected_object_author, 'testauthor@testing.test')

	def test_post_list_view(self):
		response = self.client.get(reverse('lists'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Test')
		self.assertTemplateUsed(response, 'index.html')

	def test_post_details(self):
		response = self.client.get('/detail/1/')
		no_response = self.client.get('/detail/100/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'abcd')
		self.assertTemplateUsed(response, 'detailed.html')
		
	def test_newpost_view(self):
		response = self.client.post(reverse('addpost'),{
			'title' : 'New title',
			'content' : 'New Content',
			'author' : 'self.user' ,


			})
		self.assertEqual(response.status_code,200)
		self.assertContains(response,'New Content')

	def test_post_update_view(self):
		response = self.client.post(reverse('update' , args='1'),{
			'title': 'Updated title',
			'content' : 'Updated content',

			})
		self.assertEqual(response.status_code, 200)

	def test_postdelete_view(self):
		response = self.client.get(reverse('delete',args='1'))
		self.assertEqual(response.status_code,200)




# Create your tests here.
