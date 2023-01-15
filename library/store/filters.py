import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.AllValuesFilter(field_name='title')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Book
        fields = [
            'title',
            'min_price',
            'max_price',
            'raiting',
        ]
