from django import forms

import django_filters
from .models import Book, Category


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter(lookup_expr='lte')
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),
                                                    widget=forms.CheckboxSelectMultiple)
    created = django_filters.NumberFilter(lookup_expr='year')

    class Meta:
        model = Book
        fields = ('owner', 'title', 'price', 'category', 'created',)
