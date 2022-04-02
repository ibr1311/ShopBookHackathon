from books.models import Genre
from order.forms import CartAddBookForm

def get_genres(request):
    genres = Genre.objects.all()
    return {'genres': genres}
def get_cart_form(request):
    cart_book_form = CartAddBookForm()
    return {'cart_book_form': cart_book_form}