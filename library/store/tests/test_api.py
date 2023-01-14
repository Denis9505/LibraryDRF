from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from store.serializers import BooksSerializer
from store.models import Book


class BooksAPITestCase(APITestCase):

    def setUp(self) -> None:
        
        self.book1 = Book.objects.create(title='1984', price=35, author='Author1')
        self.book2 = Book.objects.create(title='Book 2', price=25, author='Author2')
        self.book3 = Book.objects.create(title='2012 Author1', price=35, author='Author3') 

    def test_get(self):
        
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BooksSerializer([self.book1, self.book2, self.book3], many=True).data
        
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
    
    def test_get_filter(self):
        
        url = reverse('book-list')
        response = self.client.get(url, data={'price': 35})
        serializer_data = BooksSerializer([self.book1, self.book3], many=True).data
        
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_search(self):

        url = reverse('book-list')
        response = self.client.get(url, data={'search':'Author1'})
        serializer_data = BooksSerializer([self.book1, self.book3], many=True).data
        
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_order(self):

        url = reverse('book-list')
        response = self.client.get(url, data={'ordering': 'price'})
        serializer_data = BooksSerializer([self.book1, self.book2, self.book3], many=True).data
        print(response.data)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
