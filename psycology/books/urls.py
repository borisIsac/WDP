from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

#app_name = 'books'
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),
    path('books/<int:book_id>/comments/', CommentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='book_comments'),
    path('books/<int:book_id>/comments/<int:pk>/', CommentsViewSet.as_view({
        'get':'retrieve', 
        'put': 'update', 
        'patch': 'partial_update', 
        'delete': 'destroy'
        }), name='detale_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
