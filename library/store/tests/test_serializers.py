from django.test import TestCase

from ..models import Book
from ..serializers import BooksSerializer


class BookSerisalizerTestCase(TestCase):
    def test_ok(self):
        book1 = Book.objects.create(title='1984', price=35, genre='Classic', release=2020, author='Djon', raiting=5)
        book2 = Book.objects.create(title='2012', price=25, genre='Classic', release=2020, author='Alice', raiting=5)

        data = BooksSerializer([book1, book2], many=True).data
        expected_data = [
            {
                'id': book1.id,
                'title': book1.title,
                'price': '35.00',
                'genre': book1.genre,
                'release': book1.release,
                'author': book1.author,
                'raiting': '5.0'
            },
            {
                'id': book2.id,
                'title': book2.title,
                'price': '25.00',
                'genre': book2.genre,
                'release': book2.release,
                'author': book2.author,
                'raiting': '5.0'
            }
        ]

        self.assertEqual(expected_data, data)
