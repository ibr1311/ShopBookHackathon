from django.urls import path
from .views import *


urlpatterns = [
    path('<str:slug>/', books_list, name='books_list_url'),
    # path('<str:slug>/', books_detail, name='books_detail_url'),

]