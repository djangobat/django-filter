from django import forms

import django_filters
from .models import Book, Category


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ('owner', 'title', 'price', 'category', 'created',)
