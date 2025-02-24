from django.shortcuts import render, HttpResponse
from users.models import * 
from django.contrib.auth.hashers import make_password, check_password
from .forms import ContactRequestForm
# Create your views here.

def index(request):
    try:
        users = CustomUser.objects.all()
        for user in users:
            print(f"{user}".upper() )
    except:
        print('No one Users')
    return render(request, 'index.html')

def site_under_construction(request):
    return render(request, 'page_under_construction.html')

def contact_request(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contact_form.html", {"form": ContactRequestForm(), "success": True})
    else:
        form = ContactRequestForm()
    
    return render(request, 'contact_form.html', {'form':form})