from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def image_path(instance, filename):
		return f'{instance.author}/{filename}'


class Post(models.Model):
		title = models.CharField(max_length=100)
		text = models.TextField()
		image = models.ImageField(null=True, blank=True, upload_to=image_path)
		like = models.ManyToManyField(
			User,
			blank=True,
			through='LikeDetail', 
			through_fields=('post', 'user'),
			related_name='likes'
		)
		author = models.ForeignKey(
			User, 
			on_delete=models.CASCADE, 
			related_name='authors'
		)
		created = models.DateTimeField(auto_now_add=True, null=True, blank=True, db_index=True)
		updated = models.DateTimeField(auto_now=True, null=True, blank=True)

		def __str__(self):
				return self.title

		class Meta:
				verbose_name = 'Post'
				verbose_name_plural = 'Posts'


class LikeDetail(models.Model):
		post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
		user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
		created = models.DateField(auto_now_add=True, db_index=True)

		def __str__(self):
				return self.post.title

		class Meta:
				verbose_name = 'Like'
				verbose_name_plural = 'Likes'
				db_table = 'like_detail'