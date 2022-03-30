# from django.core import paginator
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.shortcuts import render
#
# from books.models import Book
#
#
# def post_list(request):
#     object_list = Book.published.all()
#     paginator = Paginator(object_list, 5) # По 5 книг на каждой странице.
#     page = request.GET.get('page')
#     try:
#         books = paginator.page(page)
#     exceptPageNotAnInteger:
#         books = paginator.page(1)
#     except EmptyPage:
#         # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
#         posts = paginator.page(paginator.num_pages)
#
#     return render(request,'bookshop/books/books_list.html', {'page': page, 'books': books})