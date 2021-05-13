from .serializers import UserSerializer
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework.views import APIView
from rest_framework import status


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class UserRegisterAPIView(CreateAPIView):
		queryset = User.objects.all()
		serializer_class = UserSerializer


class UserLoginAPIView(APIView):
		def post(self, request, *args, **kwargs):
				username = request.data.get('username')
				password = request.data.get('password')
				user = authenticate(username=username, password=password)
				if user is not None:
						if user.is_active:
								login(request, user)
								payload = jwt_payload_handler(user)
								token = jwt_encode_handler(payload)
								response = jwt_response_payload_handler(token, user, request)
								return Response(response)
						return Response({'detail': 'Your account is deactivated.'})
				return Response(
					{'detail': 'Invalid credentials.'}, 
					status=status.HTTP_400_BAD_REQUEST
				)


class GetUserActivityAPIView(APIView):
		permission_classes = [IsAuthenticated]

		def get(self, request, *args, **kwargs):
				last_login = request.user.last_login.strftime('%Y-%m-%d %H:%M:%S')
				last_activity = request.user.profile.last_activity.strftime('%Y-%m-%d %H:%M:%S')
				return Response({'last_login': last_login, 'last_activity': last_activity})