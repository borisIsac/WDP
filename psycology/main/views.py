from django.shortcuts import render, HttpResponse
from users.models import * 
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def index(request):
    try:
        users = CustomUser.objects.all()
        for user in users:
            print(f"{user}".upper() )
    except:
        print('No one Users')
    return render(request, 'index.html')
