from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView

from books.models import Book, Genre, Author
from .forms import BookForm
from .utils import ObjectCreateMixin


def genre_view(request):
    genres = Genre.objects.all()
    return render(request, 'books/main_page.html', {'genres': genres})
def books_list(request, slug):
    books = Book.objects.filter(genre__slug=slug)
    return render(request, 'books/books_list.html', {'books': books})


class BooksDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = 'books/books_detail.html'

class CreateBookView(ObjectCreateMixin, View):
    model_form = BookForm
    template = 'books/create_book.html'
    raise_exception = True


class UpdateBookView(UpdateView):
    queryset = Book.objects.all()
    template_name = 'books/update_book.html'
    form_class = BookForm
    def get_success_url(self):
        book_id = self.kwargs.get('pk')
        return redirect(reverse_lazy('books_detail_url'))




