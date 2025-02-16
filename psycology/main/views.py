from django.shortcuts import render, HttpResponse
from users.models import * 
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def index(request):
    return render(request, 'index.html')
