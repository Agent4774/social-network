from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(max_length=255, write_only=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'password2']
		extra_kwargs = {'password': {'write_only': True}}

	def validate(self, data):
		psswd = data.get('password')
		psswd2 = data.pop('password2')
		if psswd != psswd2:
			raise serializers.ValidationError('Passwords must match.')
		return data

	def validate_email(self, value):
		if User.objects.filter(email=value).exists():
			raise serializers.ValidationError('A user with that email already exists.')
		if '@' not in value or '.' not in value:
			raise serializers.ValidationError('Please, provide a valid email address.')
		return value

	def create(self, validated_data):
		user = User.objects.create(**validated_data)
		user.set_password(validated_data.get('password'))
		user.save()
		return user