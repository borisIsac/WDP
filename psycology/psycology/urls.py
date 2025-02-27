from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/api/v1/', include('users.urls')),
    path('api/v1/', include('books.urls')),

]
