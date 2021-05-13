from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.reverse import reverse
from users.models import Profile


class UserTest(TestCase):
		def setUp(self):
				user = User.objects.create(username='Logan', email='logan@logan.com')
				user.set_password('Uytrewq123')
				user.save()

		def test_user_register(self):
				url = reverse('register')
				data = {
					'username': 'hello',
					'email': 'world@world.com',
					'password': 'Uytrewq123',
					'password2': 'Uytrewq123'
				}
				result = self.client.post(url, data=data)
				self.assertEqual(result.status_code, status.HTTP_201_CREATED)

		def test_user_login(self):
				url = reverse('login')
				data = {
					'username': 'Logan',
					'password': 'Uytrewq123'
				}
				response = self.client.post(url, data=data)
				self.assertEqual(response.status_code, status.HTTP_200_OK)

		def test_token_response(self):
				url = reverse('login')
				data = {
					'username': 'Logan',
					'password': 'Uytrewq123'
				}
				response = self.client.post(url, data=data)
				token_length = len(response.data.get('token', 0))
				self.assertGreater(token_length, 0)		

		def test_activity(self):
				login_url = reverse('login')
				data = {
					'username': 'Logan',
					'password': 'Uytrewq123'
				}
				login_response = self.client.post(login_url, data=data)
				token = login_response.data.get('token')
				activity_url = reverse('get_activity')
				headers = {
					'Authorization': f'JWT {token}'
				}
				activity_response = self.client.get(activity_url, headers=headers)
				self.assertEqual(activity_response.status_code, status.HTTP_200_OK)