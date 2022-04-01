from django import forms

from .models import Book, Genre, Author, Comment


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'image', 'status', 'author', 'genre', 'price', 'description']

        widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control'}),
                    'image': forms.FileInput(attrs={'class': 'form-control'}),
                    'price': forms.TextInput(attrs={'class': 'form-control'}),
                    'description': forms.TextInput(attrs={'class': 'form-control'}),

                }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }


