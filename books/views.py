from django.shortcuts import render

from books.models import Book, Genre

def genre_view(request):
    genres = Genre.objects.all()
    return render(request, 'books/main_page.html', {'genres': genres})
def books_list(request, slug):
    books = Book.objects.filter(genre__slug=slug)
    return render(request, 'books/books_detail.html', {'books': books})