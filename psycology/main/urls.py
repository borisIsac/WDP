from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path('site_under_construction/', views.site_under_construction, name="site_under_construction"),
    path('contact_request/', views.contact_request, name='contact_request')
]