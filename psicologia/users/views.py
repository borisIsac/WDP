from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .models import *
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import make_password, check_password
from .forms import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_decode
from .models import *

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site


def activation_sended(request):
    return render(request, 'users/activation_sended.html')

def send_activate_link_by_email(user, request):
    """
    Sends an email with an activation link containing a secure token.
    """

    curent_site = get_current_site(request)
    uid = urlsafe_base64_encode(force_bytes(user.pk))  # Encode user ID
    token = default_token_generator.make_token(user)  # Generate secure token
    activation_link = settings.SITE_DOMAIN + reverse('users:activate_account', kwargs={'uidb64': uid, 'token': token})

    subject = "Activate Your Account"
    html_message = render_to_string('users/account_activation_email.html', {
        'user': user, 
        'domain': curent_site.domain,
        'activation_link': activation_link
        }
    )
    
    plain_message = f"Click the link to activate your account: {activation_link}"
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, plain_message, from_email, [user.email], html_message=html_message)



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form,
            'title': 'Login',
            'title_form': 'User Login',
            'button_submit': 'Login',
            'is_get_method': request.method == 'GET',
        }
        return render(request, 'user_form_template.html', context)

    def post(self, request):
        """
        Post method to registration new user
        """
        print(request.method)
        # Get the posted form
        form = LoginForm(data=request.POST)
        context = {
            'form': form,
            'title': 'Login',
            'title_form': 'User Login',
            'button_submit': 'Login',
        }

        if form.is_valid():
            print(form.is_valid())
            cd = form.cleaned_data
            email = cd['email']
            psw = cd['password']
            print(email)
            print(psw)
            user = authenticate(username=email, password=psw)
            if user is not None:
                if not user.is_active:
                    form.add_error('email', 'User is not active. Please active your account')
                    return render(request, 'user_form_template.html', context)
                login(request, user)
                return redirect('main:index')
            else:
                form.add_error('email', 'Email and password do not match')
        return render(request, 'user_form_template.html', context)

class LogoutView(View):
    def get(self, request):
        # Log out the user
        logout(request)
        # Redirect to the login page or any other page
        return redirect('main:index')  

class RegisterView(View):
    '''
    registration class
    '''

    def password_validation(self, password1, password2):
        '''
        password validation
        :param password1:
        :param password2:
        :return: boolean
        '''
        if password1 != password2:
            return False
        return True

    def get(self, request, uidb64=None, token=None):
        '''
        GET method for rendering registration form and handling activation
        :param request: HTTP request object
        :param uidb64: encoded user ID for activation
        :param token: token for validating activation link
        :return: rendered page with registration form or activation logic
        '''
        # If UID and token are provided, handle account activation
        if uidb64 and token:
            return self.activate_account(request, uidb64, token)

        # Otherwise, display registration form
        form = RegisterFormUser()
        context = {
            'title': 'Registration',
            'title_form': 'Register New User',
            'form': form,
            'button_submit': 'Register'
        }
        return render(request, 'user_form_template.html', context)

    def activate_account(self, request, uidb64, token):
        '''
        Activates user account if token and UID are valid
        :param request: HTTP request object
        :param uidb64: base64 encoded user ID
        :param token: activation token
        :return: redirect to login page or error message
        '''
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_object_or_404(CustomUser, pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('users:login')  # Redirect to login page after activation
        else:
            return HttpResponse("Invalid or expired activation link.", status=400)

    def post(self, request):
        form = RegisterFormUser(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if self.password_validation(cd['password'], cd['confirm_password']):
                try:
                    new_user = CustomUser.objects.create_user(
                        email=cd['email'],
                        password=cd['password'],
                        full_name=cd['full_name'],
                        username=cd['username'],
                        birthday=cd['birthday'],
                        gender=cd['gender'],
                        country=cd['country'],
                        phone=cd['phone']
                    )
                    #send activation email
                    send_activate_link_by_email(new_user, request)
                    return redirect('users:activation_sended')
                except IntegrityError:
                    form.add_error('email', 'A user with that email already exists.')
        context = {
            "error_msg": "something is wrong in your registration",
            'title': 'Registration',
            'title_form': 'Registration new User',
            'form': form,
            'button_submit': 'Register'
        }
        return render(request, 'user_form_template.html', context)

