from .base import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES['default'] = dj_database_url.config(default='https://data.heroku.com/datastores/5c8e289a-5b35-4a65-b7b7-0d603ac95d2e')

ENVIRONMENT = 'production'

DEBUG = False

ALLOWED_HOSTS = ['mycubhub.herokuapp.com']

WSGI_APPLICATION = 'my_cub_hub.wsgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'