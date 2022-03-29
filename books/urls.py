from django.urls import path
from .views import index, booklist


urlpatterns = [
    path('', index, name='home'),
    path('<str:slug>/', booklist, name='book-list'),
]