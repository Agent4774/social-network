from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def image_path(instance, filename):
	return f'{instance.author}/{filename}'


class Post(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	image = models.ImageField(null=True, blank=True, upload_to=image_path)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'