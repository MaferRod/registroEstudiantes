import unittest
from unittest.mock import patch, MagicMock
from routes import app  # Import directo desde routes.py

# Mocks de DB
class MockCursor:
    def __init__(self):
        self.lastrowid = 1
    def execute(self, query, params=None):
        return
    def fetchone(self):
        return {"id": 1, "name": "Test", "age": 20, "email": "test@test.com"}
    def fetchall(self):
        return [{"id": 1, "name": "Test", "age": 20, "email": "test@test.com"}]
    def close(self):
        pass

class MockConnection:
    def cursor(self, dictionary=False):
        return MockCursor()
    def commit(self):
        pass
    def close(self):
        pass

class TestStudentAPI(unittest.TestCase):

    def setUp(self):
        # Parcheamos get_connection para todas las pruebas
        patcher = patch('routes.get_connection', return_value=MockConnection())
        self.mock_get_connection = patcher.start()
        self.addCleanup(patcher.stop)  # Detener el parche al final de cada test
        self.client = app.test_client()
        self.student_data = {
            "name": "Test Student",
            "age": 20,
            "email": "test@student.com"
        }

    def test_create_student(self):
        response = self.client.post('/students', json=self.student_data)
        self.assertEqual(response.status_code, 201)

    def test_get_students(self):
        response = self.client.get('/students')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_update_student(self):
        student_id = 1
        updated_data = {"name": "Updated Name", "age": 21, "email": "updated@test.com"}
        response = self.client.put(f'/students/{student_id}', json=updated_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_student(self):
        student_id = 1
        response = self.client.delete(f'/students/{student_id}')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
