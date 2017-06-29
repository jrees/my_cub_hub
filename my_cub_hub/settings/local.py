from .base import *

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mch',
        'USER': 'mchadmin',
        'PASSWORD': 'p1n3appl3mch',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DEBUG = True

WSGI_APPLICATION = 'my_cub_hub.wsgi.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sjg*t5l69f8js6r#b5vh#d89nih5(r&3%i=2&ds=tczeft7g#q'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'