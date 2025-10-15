from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse
from unittest.mock import patch

class StudentViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.student_data = {
            'name': 'Test Student',
            'age': 20,
            'email': 'test@student.com'
        }

    @patch('students.views.requests.get')
    def test_student_list_view(self, mock_get):
        # Mockeamos la respuesta de la API
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [self.student_data]

        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Student')

    @patch('students.views.requests.post')
    def test_add_student_view_post(self, mock_post):
        mock_post.return_value.status_code = 201
        response = self.client.post(reverse('add_student'), self.student_data)
        self.assertEqual(response.status_code, 302)  # Redirige a la lista
