from django.urls import path
from .views import *



urlpatterns = [
    path('<str:slug>/', books_list, name='books_list_url'),
    path('/<int:pk>/', BooksDetailView.as_view(), name='books_detail_url'),
    path('updatebook/<int:pk>/', update_book, name='update_book_url'),
    path('deletebook/<int:pk>/', delete_book, name='delete_book_url'),
    path('/<int:pk>/add_comment/', add_comment, name='add_comment_url'),
    path('/<int:pk>/delete_comment/', delete_comment, name='delete_comment_url'),

]
