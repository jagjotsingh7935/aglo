from rest_framework.test import APITestCase
from rest_framework import status
from ..models import ToDoItem

class ToDoItemAPITest(APITestCase):
    def test_create_todo(self):
        response = self.client.post('/api/todos/', {
            'title': 'New Task',
            'description': 'Details of the task',
            'status': 'OPEN',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
