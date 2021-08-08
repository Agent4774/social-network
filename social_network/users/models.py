from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	last_activity = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = 'Custom user'
		verbose_name_plural = 'Custom users'