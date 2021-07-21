from .models import Book
from django.test import TestCase
from rest_framework import status
from .serializers import BooksSerializer
from rest_framework.test import APIClient

# Create your tests here.
class BookTest(TestCase):
    
    def setUp(self):
        self.endpoint = '/api/books/'
        self.client = APIClient()
        self.book = {
            'title': 'Title 1',
            'description': 'description 1',
            'author': 'author 1'
        }

        self.response = self.client.post(
            self.endpoint, 
            data = self.book, 
            format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_list(self):
        """Test the api can get all book info"""
        response = self.client.get(
            self.endpoint
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_api_get_a_book(self):
        """Test the api can get a given book info"""
        book = Book.objects.get()
        response = self.client.get(
            self.endpoint,
            kwargs={'pk': book.id}, 
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, book)

    def test_api_update_book(self):
        """Test the api can update a given book info."""
        book = Book.objects.get(id=1)
        change_book = {
            'title': 'Something new',
            'description': 'description 1',
            'author': 'author 1'
        }
        response = self.client.put(
            f'{self.endpoint}{book.id}/',
            change_book, 
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_api_delete_book(self):
        """Test the api can delete a book."""
        book = Book.objects.get()
        response = self.client.delete(
            f'{self.endpoint}{book.id}/',
            format='json'
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_model_str(self):
        title = Book.objects.create(
            title = "Title",
            description = "description",
            author = "author"
        )
        author = Book.objects.create(
            author = "author 1"
        )
        self.assertEqual(str(title),'Title')

    def tearDown(self):
        books = Book.objects.all()
        del books