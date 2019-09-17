from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse,reverse_lazy


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

class PostUpdateView(UpdateView): 
    model = Post
    template_name = 'update.html'
    fields = ['title', 'author', 'content']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'deleteview.html'
	success_url = reverse_lazy('lists')



