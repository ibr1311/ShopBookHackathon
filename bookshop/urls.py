from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from books.views import *
from bookshop import views
from .views import redirect_blog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('#/', include('books.urls')),
    path('home/', genre_view, name='main_page_url'),
    path('accounts/', include('account.urls')),
    path('home/createbook/', create_book, name='create_book_url'),
    path('search/', views.post_search, name='books_search'),
    path('', redirect_blog),
    path('cart/', include('order.urls', namespace='order')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

