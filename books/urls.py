from django.urls import path
from .views import *


urlpatterns = [
    path('<str:slug>/', books_list, name='books_list_url'),
    path('/<int:pk>/', BooksDetailView.as_view(), name='books_detail_url'),
    path('update/<int:pk>', UpdateBookView.as_view(), name='update_book_url')

]