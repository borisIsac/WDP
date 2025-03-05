from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

app_name = ''
router = DefaultRouter()
router.register(r'cartlist', CartListViewSet , basename='cartlist')

urlpatterns = [
    path('', include(router.urls)),
    path('cartlist/add_book/<int:book_id>/',BookToCartlist.as_view(), name='add_book_to_cartlist'),
    path('cartlist/delete_book/<int:book_id>/',BookToCartlist.as_view(), name='delete_book_from_cartlist'),
]
