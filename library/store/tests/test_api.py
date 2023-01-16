import json
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

from store.serializers import BooksSerializer
from store.models import Book


class BooksAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='test_user')
        
        self.book1 = Book.objects.create(title='1984', price=25, author='Author1', genre='Classic', release=2020, raiting=5)
        self.book2 = Book.objects.create(title='Book 2', price=25, author='Author2', genre='Classic', release=2020, raiting=5)
        self.book3 = Book.objects.create(title='2012 Author1', price=35, author='Author3', genre='Classic', release=2020, raiting=4) 

    def test_get(self):
        
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BooksSerializer([self.book1, self.book2, self.book3], many=True).data
        
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
    
    def test_get_filter(self):
        
        url = reverse('book-list')
        response = self.client.get(url, data={'raiting': 5})
        serializer_data = BooksSerializer([self.book1, self.book2, self.book3], many=True).data

        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_search(self):

        url = reverse('book-list')
        response = self.client.get(url, data={'search':'Author1'})
        serializer_data = BooksSerializer([self.book1, self.book3], many=True).data
        
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_create(self):
        url = reverse('book-list')
        data = {
           "title": "Рассказы учеников богатого папы",
           "price": 35,
           "author": "Роберт Кийосаки",
           "genre": "Biography",
           "raiting": 4,
           "release": 2012
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_update(self):
        url = reverse('book-detail', args=(self.book1.id, ))
        data = {
           "title": self.book1.title,
           "price": 45,
           "author": "Роберт Кийосаки",
           "genre": "Biography",
           "raiting": 4,
           "release": 2012
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data,
                                    content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.book1.refresh_from_db()
        self.assertEqual(45, self.book1.price)
