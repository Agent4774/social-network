from django.urls import path
from . import views


urlpatterns = [
	path('create/', views.CreatePostAPIView.as_view(), name='create_post'),
]