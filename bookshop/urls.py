
from django.contrib import admin
from django.urls import path, include

from books.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('#/', include('books.urls')),
    path('home/', genre_view, name='main_page_url'),
    path('accounts/', include('account.urls')),

]

    # path('books/', include('bookshop.urls')),
    # path('', include('order.urls')),


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
