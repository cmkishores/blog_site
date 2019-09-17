from django.urls import path
from .views import ListingView, DetailedListView, AddPostView, PostUpdateView, DeletePostView

urlpatterns = [
	path('',ListingView.as_view(), name = 'lists' ),
	path('detail/<int:pk>/',DetailedListView.as_view(),name = 'detailed'),
	path('post/new/', AddPostView.as_view(),name = 'addpost'),
	path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='update'),
	path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete')
]