from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('register/', views.register, name='register'),
]