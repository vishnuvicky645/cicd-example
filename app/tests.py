from django.test import TestCase


class BasicTests(TestCase):
    def test_homepage_status(self):
        """Test that the admin page returns a redirect (login)."""
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)

    def test_app_is_running(self):
        """Basic sanity check."""
        self.assertTrue(True)
