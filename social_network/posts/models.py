from django.db import models
from django.utils import timezone
from users.models import CustomUser


def image_path(instance, filename):
		return f'{instance.author}/{filename}'


class Post(models.Model):
		title = models.CharField(max_length=100)
		text = models.TextField()
		image = models.ImageField(null=True, blank=True, upload_to=image_path)
		author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
		created = models.DateTimeField(auto_now_add=True, null=True, blank=True, db_index=True)
		updated = models.DateTimeField(auto_now=True, null=True, blank=True)

		def __str__(self):
				return self.title

		class Meta:
				verbose_name = 'Post'
				verbose_name_plural = 'Posts'


class Like(models.Model):
		post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
		user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
		created = models.DateField(auto_now_add=True, db_index=True)

		def __str__(self):
				return self.post.title

		class Meta:
				verbose_name = 'Like'
				verbose_name_plural = 'Likes'