from django.utils import timezone
from .models import Profile


class UserLastActivity:
	def process_view(self, request, view_func, view_args, view_kwargs):
		user = Profile.objects.get(user__pk=request.user.pk)
		user.update(last_activity=timezone.now())