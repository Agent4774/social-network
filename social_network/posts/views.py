from django.shortcuts import render
from rest_framework.generics import CreateAPIView 
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer


class CreatePostAPIView(CreateAPIView):
	queryset = Post.objects.all()
	permission_classes = [IsAuthenticated]
	serializer_class = PostSerializer

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)