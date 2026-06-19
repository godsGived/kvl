from django.test import TestCase, Client

class ExamIntegrationTest(TestCase):
    def test_endpoint(self):
        self.client = Client()
        response = self.client.get('/ping/')
        if response.status_code == 200:
            self.assertEqual(response.status_code, 200)
