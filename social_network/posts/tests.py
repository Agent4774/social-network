from django.test import TestCase
from users.models import CustomUser
from rest_framework.reverse import reverse
from rest_framework import status


class PostTestCase(TestCase):
		def setUp(self):
				user = CustomUser.objects.create(username='Logan')
				user.set_password('Uytrewq123')
				user.save()

		def test_post_create(self):
				login_url = reverse('login')
				data = {
					'username': 'Logan',
					'password': 'Uytrewq123'
				}
				response = self.client.post(login_url, data=data)
				token = response.data.get('token')
				post_create_url = reverse('create_post')
				data = {
					'title': 'hello',
					'text': 'world'
				}
				headers = {
					'Authorization': f'JWT {token}'
				}
				response = self.client.post(post_create_url, data=data, headers=headers)
				self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		def test_post_like(self):
				login_url = reverse('login')
				data = {
					'username': 'Logan',
					'password': 'Uytrewq123'
				}
				response = self.client.post(login_url, data=data)
				token = response.data.get('token')
				post_create_url = reverse('create_post')
				data = {
					'title': 'hello',
					'text': 'world'
				}
				headers = {
					'Authorization': f'JWT {token}'
				}
				response = self.client.post(post_create_url, data=data, headers=headers)
				post_like_url = reverse('like_unlike', kwargs={'pk': 1})
				response = self.client.post(post_like_url, data, headers=headers)
				self.assertEqual(response.status_code, status.HTTP_200_OK)

		def test_post_unlike(self):
				login_url = reverse('login')
				data = {
					'username': 'Logan',
					'password': 'Uytrewq123'
				}
				response = self.client.post(login_url, data=data)
				token = response.data.get('token')
				post_create_url = reverse('create_post')
				data = {
					'title': 'hello',
					'text': 'world'
				}				
				headers = {
					'Authorization': f'JWT {token}'
				}
				response = self.client.post(post_create_url, data=data, headers=headers)
				post_like_url = reverse('like_unlike', kwargs={'pk': 1})
				response = self.client.post(post_like_url, data)
				post_like_url = reverse('like_unlike', kwargs={'pk': 1})
				response = self.client.delete(post_like_url, headers=headers)
				self.assertEqual(response.status_code, status.HTTP_200_OK)

		def test_likes_analytics(self):
				login_url = reverse('login')
				data = {
					'username': 'Logan',
					'password': 'Uytrewq123'
				}
				response = self.client.post(login_url, data=data)
				token = response.data.get('token')
				post_create_url = reverse('create_post')
				data = {
					'title': 'hello',
					'text': 'world'
				}
				headers = {
					'Authorization': f'JWT {token}'
				}
				response = self.client.post(post_create_url, data=data, headers=headers)
				post_like_url = reverse('like_unlike', kwargs={'pk': 1})
				response = self.client.post(post_like_url, data, headers=headers)
				all_likes_list_url = reverse('analytics') + '?date_from=2021-05-01&date_to=2021-05-05'
				response = self.client.get(all_likes_list_url, headers=headers)
				self.assertEqual(response.status_code, status.HTTP_200_OK)