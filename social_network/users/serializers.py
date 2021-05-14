from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
		password2 = serializers.CharField(max_length=255, write_only=True)

		class Meta:
				model = CustomUser
				fields = ['username', 'email', 'password', 'password2']
				extra_kwargs = {'password': {'write_only': True}}

		def validate(self, data):
				psswd = data.get('password')
				psswd2 = data.pop('password2')
				if psswd != psswd2:
						raise serializers.ValidationError('Passwords must match.')
				return data

		def validate_email(self, value):
				if CustomUser.objects.filter(email=value).exists():
						raise serializers.ValidationError('A user with that email already exists.')
				if '@' not in value or '.' not in value:
						raise serializers.ValidationError('Please, provide a valid email address.')
				return value