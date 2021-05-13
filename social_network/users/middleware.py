from django.utils import timezone
from .models import Profile
from django.utils.deprecation import MiddlewareMixin


class UserLastActivityMiddleware(MiddlewareMixin):
		def process_view(self, request, view_func, view_args, view_kwargs):
				if request.user.is_authenticated:
						request.user.profile.last_activity = timezone.now()
						request.user.profile.save()