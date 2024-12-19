import unittest
import json
from app import app

class LibraryAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.headers = {'Content-Type': 'application/json'}

    def test_create_and_get_books(self):
        # Create a book
        book_data = {'title': 'Test Book', 'author': 'Test Author', 'published': '2023-09-19'}
        response = self.client.post('/books', data=json.dumps(book_data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

        # Get all books
        response = self.client.get('/books', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        books = response.get_json().get('books', [])
        self.assertTrue(len(books) > 0)

        # Get a specific book
        book_id = books[0]['id']
        response = self.client.get(f'/books/{book_id}', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        book = response.get_json()
        self.assertEqual(book['title'], 'Test Book')

    def test_update_book(self):
        # Create a new book
        book_data = {'title': 'Update Test', 'author': 'Update Author', 'published': '2021-08-19'}
        response = self.client.post('/books', data=json.dumps(book_data), headers=self.headers)
        book_id = response.get_json().get('id', 0)

        # Update the book
        updated_data = {'title': 'Updated Title', 'author': 'Updated Author', 'published': '2019-10-20'}
        response = self.client.put(f'/books/{book_id}', data=json.dumps(updated_data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

    def test_delete_book(self):
        # Create a new book
        book_data = {'title': 'Delete Me', 'author': 'Delete Author', 'published': '2020-10-20'}
        response = self.client.post('/books', data=json.dumps(book_data), headers=self.headers)
        book_id = response.get_json().get('id', 0)

        # Delete the book
        response = self.client.delete(f'/books/{book_id}', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

    def test_create_and_get_members(self):
        # Create a new member
        member_data = {'name': 'Test Member', 'email': 'testmember@example.com'}
        response = self.client.post('/members', data=json.dumps(member_data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

        # Get all members
        response = self.client.get('/members', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        members = response.get_json().get('members', [])
        self.assertTrue(len(members) > 0)

        # Get single member by ID
        member_id = members[0]['id']
        response = self.client.get(f'/members/{member_id}', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        member = response.get_json()
        self.assertEqual(member['name'], 'Test Member')

    def test_update_member(self):
        # Create a new member
        member_data = {'name': 'Update Member', 'email': 'updatemember@example.com'}
        response = self.client.post('/members', data=json.dumps(member_data), headers=self.headers)
        member_id = response.get_json().get('id', 0)

        # Update the member
        updated_data = {'name': 'Updated Name', 'email': 'updatedemail@example.com'}
        response = self.client.put(f'/members/{member_id}', data=json.dumps(updated_data), headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

    def test_delete_member(self):
        # Create a new member
        member_data = {'name': 'Delete Member', 'email': 'deletemember@example.com'}
        response = self.client.post('/members', data=json.dumps(member_data), headers=self.headers)
        member_id = response.get_json().get('id', 0)

        # Delete the member
        response = self.client.delete(f'/members/{member_id}', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

if __name__ == '__main__':
    unittest.main()
