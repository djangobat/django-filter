from django.shortcuts import render

from .models import Book
from .filters import BookFilter


def books_list(request):
    query = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=query)

    context = {
        'filter': book_filter,
        'books': book_filter.qs,
    }

    return render(request, 'books/list.html', context)