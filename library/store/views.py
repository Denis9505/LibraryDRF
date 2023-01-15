from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from .serializers import BooksSerializer
from .filters import BookFilter


class BookViewSet(ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_class = BookFilter
    # search_fields = ['author', 'title']
    # ordering_fields = ['price', 'author']
