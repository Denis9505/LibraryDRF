from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from store.serializers import BooksSerializer
from store.models import Book


class BooksAPITestCase(APITestCase):
    def test_get(self):
        
        books1 = Book.objects.create(title='1984', price=35)
        books2 = Book.objects.create(title='2012', price=25)
        
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BooksSerializer([books1, books2], many=True).data
        
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        