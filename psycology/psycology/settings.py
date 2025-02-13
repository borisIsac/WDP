from pathlib import Path
from secret_files.secret_data import *
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#SITE_DOMAIN = insert a domain here
SITE_DOMAIN = 'http://localhost:8000'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Framework
    'rest_framework',

    #Libraries
    'django_recaptcha',

    #my_apps
    'users',
    'main',
    'books',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'psycology.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'psycology.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': PSQL_DB,              
        'USER': PSQL_USER,          
        'PASSWORD': PSQL_USER_PASSWORD, 
        'HOST': '127.0.0.1',          
        'PORT': '5432',               
    }
}'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': PSQL_DB,              
        'USER': PSQL_USER,          
        'PASSWORD': PSQL_USER_PASSWORD, 
        'HOST': 'database',          
        'PORT': '5432',               
    }
}




# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/'

MEDIA_URL = '/media/'  # URL prefix for media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Directory to store uploaded files

STATIC_URL = '/static/'  # URL for static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Static files directory

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

AUTHENTICATION_BACKENDS = ['users.authentication_backend_email.EmailAuthBackend']

#email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = EMAIL_SENDER
EMAIL_HOST_PASSWORD = EMAIL_SENDER_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'         

#recaptcha

RECAPTCHA_PUBLIC_KEY = RECAPTCHA_PUBLIC_KEY
RECAPTCHA_PRIVATE_KEY = RECAPTCHA_PRIVATE_KEY
