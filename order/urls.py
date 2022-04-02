from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path('', cart_detail, name='cart_detail_url'),
    path('add/<int:pk>/', cart_add, name='cart_add_url'),
    path('remove/<int:pk>', cart_remove, name='cart_remove_url'),

]