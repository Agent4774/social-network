from django.utils import timezone
from .models import Profile
from django.utils.deprecation import MiddlewareMixin


class UserLastActivityMiddleware(MiddlewareMixin):
	def process_view(self, request, view_func, view_args, view_kwargs):
		if request.user.is_authenticated:
			user_profile = Profile.objects.get(user=request.user)
			user_profile.last_activity = timezone.now()
			user_profile.save()