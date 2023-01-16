from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions

from .models import Book
from .serializers import BooksSerializer
from .filters import BookFilter


class BookViewSet(ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_class = BookFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = ['author', 'genre', 'price', 'release', 'title']
    ordering_fields = ['price', 'release']

def oauth(request):
    return render(request, 'oAuth.html')
