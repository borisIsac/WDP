from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('books.urls')),
    path('api/v1/', include('wish_list.urls')),
    path('api/v1/', include('cart.urls')),
]
