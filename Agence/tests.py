from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccessControlTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='client', password='test-password-123')

    def test_anonymous_user_is_redirected_from_reservations(self):
        response = self.client.get(reverse('reservations_lists'))
        self.assertEqual(response.status_code, 302)

    def test_regular_user_cannot_create_voyage(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('voyage_ajouter'))
        self.assertEqual(response.status_code, 403)
