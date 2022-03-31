from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from books.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('#/', include('books.urls')),
    path('home/', genre_view, name='main_page_url'),
    path('accounts/', include('account.urls')),
    path('home/createbook/', CreateBookView.as_view(), name='create_book_url'),
    # path('home/update/b/', UpdateBookView.as_view(), name='update_book_url'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
