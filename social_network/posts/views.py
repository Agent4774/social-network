from .models import Post, Like
from .serializers import PostSerializer
from datetime import datetime, timedelta
from django.db.models import Count
from django.shortcuts import render
from rest_framework.generics import CreateAPIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CreatePostAPIView(CreateAPIView):
	queryset = Post.objects.all()
	permission_classes = [IsAuthenticated]
	serializer_class = PostSerializer

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class LikeUnlikeAPIView(APIView):
	permission_classes = [IsAuthenticated]
	post = None

	def get_object(self, pk):
		try:
			self.post = Post.objects.get(pk=pk)
		except Post.DoesNotExist:
			return Response(
				{'detail': 'Post not found.'}, 
				status=status.HTTP_400_BAD_REQUEST
			)

	def post(self, request, *args, **kwargs):
		like, created = Like.objects.get_or_create(
			post=self.post, 
			user=request.user
		)
		if created:
			return Response({'detail': 'Like added.'})
		like.delete()
		return Response({'detail': 'Like deleted.'})


class LikesAnalyticsListAPIView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request, *args, **kwargs):
		date_from = request.GET.get('date_from', None)
		date_to = request.GET.get('date_to', None)
		if date_from == None or date_to == None:
			return Response(
				{'detail': 'Please provide both date_from and date_to parameters.'},
				status=status.HTTP_400_BAD_REQUEST
			)
		if date_to > str(datetime.now().date()):
			return Response(
				{'detail': 'date_to must be today or earlier date'},
				status=status.HTTP_400_BAD_REQUEST
			)
		date_from = datetime.strptime(date_from, '%Y-%m-%d').date()
		date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
		data = Like.objects.filter(
			created__gte=date_from, 
			created__lte=date_to
		).values('created').annotate(Count('created')).order_by('created')
		response_data = {}
		for item in data:
			response_data.update({
				str(item['created']): item['created__count'] 
			})
		while date_from <= date_to:
			if not str(date_from) in response_data:
				response_data[str(date_from)] = 0
			date_from += timedelta(days=1)
		return Response(dict(sorted(response_data.items()))) # Sorted by keys dict
		