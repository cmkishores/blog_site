from django.db import models

class Post(models.Models):
	title = models.CharField(max_length=50)
	comment = models.TextField()
	author = models.EmailField()

# Create your models here.
