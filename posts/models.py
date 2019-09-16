from django.db import models
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	author = models.EmailField()

	def __str__(self):
		return self.title[:30]

	def get_absolute_url(self):
		return reverse('detailed', args=[str(self.id)])


# Create your models here.
