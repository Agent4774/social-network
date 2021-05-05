from django.urls import path
from . import views


urlpatterns = [
	path('create/', views.CreatePostAPIView.as_view(), name='create_post'),
	path('like-unlike/<int:pk>/', views.LikeUnlikeAPIView.as_view(), name='like_unlike'),
	path('likes-analytics/<int:pk>/', views.LikesAnalyticsDetailAPIView.as_view(), name='post_likes_analytics'),
	path('all-likes-analytics/', views.LikesAnalyticsListAPIView.as_view(), name='all_likes_analytics'),
]