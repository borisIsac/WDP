from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from  .models import *
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import make_password, check_password
from .forms import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from .forms import *

from .models import *

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
            print(user)
            if user is not None:
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

    def get(self, request):
        '''
        get method for printing form
        :param requests:
        :return rendered page with a form for registration:
        '''
        form = RegisterFormUser()
        if form:
            context = {
                'title': 'Registration',
                'title_form': 'Registration new User',
                'form': form,
                'button_submit': 'Register'
            }
            return render(request, 'user_form_template.html', context)

    def post(self, request):
        form = RegisterFormUser(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print((cd['password'] == cd['confirm_password']) and (cd['phone'].isdigit()))
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
                    new_user.save()
                    return redirect('users:login')
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

