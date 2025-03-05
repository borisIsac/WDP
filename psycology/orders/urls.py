from django.urls import path, include
from .views import OrderViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

app_name = 'orders'
router = DefaultRouter()
router.register(r'orders', OrderViewSet , basename='orders')

urlpatterns = [
    path('', include(router.urls)),
]