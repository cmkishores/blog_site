from django.urls import path
from .views import ListingView, DetailedListView, AddPostView

urlpatterns = [
	path('',ListingView.as_view(), name = 'lists' ),
	path('detail/<int:pk>/',DetailedListView.as_view(),name = 'detailed'),
	path('post/new/', AddPostView.as_view(),name = 'addpost')
	
]