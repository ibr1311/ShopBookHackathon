from django.db import models
from django.shortcuts import reverse
from account.models import User

class Author(models.Model):
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=85, blank=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Genre(models.Model):
    slug = models.SlugField(max_length=55, primary_key=True)
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name
class Book(models.Model):
    CHOICES = (
        ('in stock', 'In stock'),
        ('out of stock', 'Out of stock')
    )

    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='books_img')
    status = models.CharField(choices=CHOICES, max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.ManyToManyField(Genre)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('books_list_url', kwargs={'slug': self.genre})

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    class Meta:
        ordering = ['title']


class Comment(models.Model):
    book = models.ForeignKey(Book, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.book.name, self.commenter_name)


