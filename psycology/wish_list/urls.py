from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

#app_name = 'wish_list'
router = DefaultRouter()
router.register(r'wishlist', WishListViewSet , basename='wishlist')

urlpatterns = [
    path('', include(router.urls)),
    path('wishlist/add_book/<int:book_id>/',BookToWishlist.as_view(), name='add_book_to_wishlist'),
    path('wishlist/delete_book/<int:book_id>/',BookToWishlist.as_view(), name='delete_book_from_wishlist'),
]
