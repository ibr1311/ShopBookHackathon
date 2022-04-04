from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, ListView

import books
from books.models import Book, Genre, Author, Comment
from .forms import BookForm, CommentForm
from datetime import datetime
from order.forms import CartAddBookForm


def genre_view(request):
    genres = Genre.objects.all()
    paginate_by = 2
    return render(request, 'books/main_page.html', {'genres': genres})
def books_list(request, slug):
    books = Book.objects.filter(genre__slug=slug)
    page_num = request.GET.get("page")
    paginator = Paginator(books, 2)
    try:
        books = paginator.page(page_num)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)


    context = {
        'books': books,
    }

    return render(request, 'books/books_list.html', context)




class BooksDetailView(DetailView):
    queryset = Book.objects.all()
    cart_book_form = CartAddBookForm()
    template_name = 'books/books_detail.html'




def create_book(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('main_page_url'))

    else:
        form = BookForm()
    context = {
        "form": form
    }

    return render(request, 'books/create_book.html', context)

def update_book(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse('books_detail_url', args=[book.id]))

    context = {
        'form': form
    }
    return render(request, 'books/update_book.html', context)

def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect(reverse('main_page_url'))

def add_comment(request, pk):
    book = Book.objects.get(id=pk)

    form = CommentForm(instance=book)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=book)
        if form.is_valid():
            name = request.user.first_name
            body = form.cleaned_data['comment_body']
            c = Comment(book=book, commenter_name=name, comment_body=body, date_added=datetime.now())
            c.save()
            return redirect(reverse('books_detail_url', args=[book.id]))
        else:
            print('form is invalid')
    else:
        form = CommentForm()

    context = {
        'form': form
    }

    return render(request, 'books/add_comment.html', context)

def delete_comment(request, pk):
    comment = Comment.objects.filter(book=pk).last()
    book_id = comment.book.id
    comment.delete()
    return redirect(reverse('books_detail_url', args=[book_id]))

class AboutListView(ListView):
    model = Book
    paginate_by = 3
    template_name = 'books/about.html'






