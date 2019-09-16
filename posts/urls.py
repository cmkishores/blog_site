from django.urls import path
from .views import ListingView, DetailedListView

urlpatterns = [
	path('',ListingView.as_view(), name = 'lists' ),
	path('detail/<int:pk>/',DetailedListView.as_view(),name = 'detailed'),
	
]