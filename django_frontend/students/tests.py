from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch

class StudentViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        # Siempre incluimos 'id' para que los templates con {% url 'edit_student' student.id %} no fallen
        self.student_data = {
            'id': 1,
            'name': 'Test Student',
            'age': 20,
            'email': 'test@student.com'
        }

    @patch('students.views.requests.get')
    def test_student_list_view(self, mock_get):
        # Mock de la API GET para listar estudiantes
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [self.student_data]

        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Student')
        self.assertContains(response, 'edit/1')  # Verificamos que el enlace de edición exista

    @patch('students.views.requests.post')
    def test_add_student_view_post(self, mock_post):
        # Mock de la API POST para agregar estudiante
        mock_post.return_value.status_code = 201

        response = self.client.post(reverse('add_student'), self.student_data)
        self.assertEqual(response.status_code, 302)  # Redirige a la lista

    @patch('students.views.requests.put')
    @patch('students.views.requests.get')
    def test_edit_student_view_post(self, mock_get, mock_put):
        # Mock GET para traer datos existentes
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = self.student_data

        # Mock PUT para actualizar estudiante
        mock_put.return_value.status_code = 200

        updated_data = {
            'id': 1,
            'name': 'Updated Student',
            'age': 21,
            'email': 'updated@student.com'
        }

        response = self.client.post(reverse('edit_student', args=[1]), updated_data)
        self.assertEqual(response.status_code, 302)  # Redirige a la lista

    @patch('students.views.requests.delete')
    def test_delete_student_view(self, mock_delete):
        # Mock DELETE para eliminar estudiante
        mock_delete.return_value.status_code = 204

        response = self.client.post(reverse('delete_student', args=[1]))
        self.assertEqual(response.status_code, 302)  # Redirige a la lista
