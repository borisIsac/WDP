from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'books'

urlpatterns = [
    path('api/v1/book_list', BookViewSet.as_view(), name='book_list'),
    path('api/v1/book_add', NewBookRegisterView.as_view(), name='book_add'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)