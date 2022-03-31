from django import forms

from .models import Book, Genre, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'image', 'status', 'author', 'genre', 'price', 'description']




