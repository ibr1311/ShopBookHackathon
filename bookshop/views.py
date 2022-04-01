from django.contrib.postgres.search import SearchVector

from books.models import Book
from .forms import SearchForm

from django.shortcuts import render, redirect


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Book.objects.annotate(
            search=SearchVector('title', 'description', 'author__name', 'author__last_name'),
        ).filter(search=query)
    return render(request, 'books/search.html', {'form': form, 'query': query,
                                        'results': results})


def redirect_blog(request):
    return redirect('main_page_url', permanent=True)