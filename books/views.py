from django.shortcuts import render
from .models import Book, Genre


# def index(request):
#     genres = Genre.objects.all()
#     return render(request, 'books/index.html', {'genres': genres})
# def booklist(request, slug):
#     books = Book.objects.filter(genre__slug=slug)
#     return render(request, 'books/booklist.html', {'books': books})
