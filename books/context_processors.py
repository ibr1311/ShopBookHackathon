from books.models import Genre


def get_genres(request):
    genres = Genre.objects.all()
    return {'genres': genres}