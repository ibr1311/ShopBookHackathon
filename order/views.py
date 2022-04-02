from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from books.models import Book
from order.cart import Cart
from order.forms import CartAddBookForm
from django.views.decorators.http import require_POST


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    book = get_object_or_404(Book, id=pk)
    form = CartAddBookForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=book, quantity=cd['quantity'], overrride_quantity=cd['override'])
    return redirect(reverse('order:cart_detail_url'))

def cart_remove(request, pk):
    cart = Cart(request)
    book = get_object_or_404(Book, id=pk)
    cart.remove(book)
    return redirect(reverse('books_detail_url'))
def cart_detail(request):
    cart = Cart(request)
    books = []
    for item in cart:
        item = CartAddBookForm(initial={'quantity': item['quantity']})
    context = {'cart': cart}
    context['books'] = books
    return render(request, 'order/detail.html', context)





