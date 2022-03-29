from django.shortcuts import render

from books.models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})
# def booklist(request, slug):
#     books = Book.objects.filter(genre__slug=slug)
#     return render(request, 'main/booklist.html', {'books': books})