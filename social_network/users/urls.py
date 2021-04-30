from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.UserRegisterAPIView.as_view(), name='register'),
	path('login/', views.UserLoginAPIView.as_view(), name='login'),
	path('activity/', views.get_user_activity, name='get_activity'),
]