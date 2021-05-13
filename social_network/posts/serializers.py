from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
		class Meta:
				model = Post
				fields = ['title', 'text', 'image', 'author']
				extra_kwargs = {'author': {'read_only': True}}

		def validate_image(self, value):
				image_info = value.name.rsplit('.')
				if image_info[1] not in ['jpg', 'jpeg', 'png']:
						raise serializers.ValidationError('Wrong image format.')
				return value