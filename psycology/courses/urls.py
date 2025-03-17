from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

app_name = 'courses'
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls)),
    path('courses/<int:course_id>/comments/', CommentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='course_comments'),
    path('courses/<int:course_id>/comments/<int:pk>/', CommentsViewSet.as_view({
        'get':'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
        }), name='detale_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
