from django.shortcuts import render, HttpResponse, redirect
from users.models import * 
from django.contrib.auth.hashers import make_password, check_password
from .forms import ContactRequestForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from secret_files.secret_data import *
import logging

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
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        context = {
            'form': form,
            'success': 'Mensagem enviada com sucesso.'
        }
        if form.is_valid():
            cd = form.cleaned_data
            full_name = cd['full_name']
            email = cd['email']
            subject = cd['subject']
            message = cd['message']

            email_subject = f'Novo Contacto Sobre: {subject}'

            email_body = render_to_string('emails/contact_email.html', {
                'full_name': full_name,
                'email': email,
                'subject': subject,
                'message': message
            })  
            
            logger = logging.getLogger(__name__)
            
            try:
                email_msg = EmailMultiAlternatives(
                    subject=email_subject,
                    body=email_body,
                    from_email=EMAIL_SENDER,
                    to=[EMAIL_SENDER],
                    reply_to=[email]
                )

                email_msg.attach_alternative(email_body, "text/html")
                email_msg.send(fail_silently=False)
            
                return render(request, "page_under_construction.html", context)

            # Raise error if email not sent because fail_silently=False
            except Exception as e:
                logger.error(f"Email sending failed: {e}")
                return render(request, "page_under_construction.html", context)

    else:
        form = ContactRequestForm()
        context = {
            'form': form,
            'submit': 'Enviar Mensagem'
        }
    return render(request, 'page_under_construction.html', context)
