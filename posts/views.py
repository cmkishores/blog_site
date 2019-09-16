from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


from .models import Post

class ListingView(ListView):
	model = Post
	template_name = 'index.html'
	context_object_name = 'list_of_posts'

class DetailedListView(DetailView):
	model = Post
	template_name = 'detailed.html'

class AddPostView(CreateView):
	model = Post
	template_name = 'addpost.html'
	fields = ['title','author', 'content']


