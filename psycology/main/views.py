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
        context = {
            'form': form,
            'success': 'Contact request sent successfully'
        }
        if form.is_valid():
            cd = form.cleaned_data
            request.form.full_name = cd['full_name']
            request.form.email = cd['email']
            form.save()
            return render(request, "contact_form.html", context)
    else:
        form = ContactRequestForm()
    
    return render(request, 'contact_form.html', {'form': form})