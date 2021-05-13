from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
		user = models.OneToOneField(User, on_delete=models.CASCADE)
		last_activity = models.DateTimeField(auto_now=True)

		def __str__(self):
				return self.user.username

		class Meta:
				verbose_name = 'Profile'
				verbose_name_plural = 'Profiles'