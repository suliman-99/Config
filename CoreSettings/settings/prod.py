from .common import *

DEBUG = False

ALLOWED_HOSTS = [
    'suliman99.pythonanywhere.com'
    ]



SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DATABASE_NAME'),
        'HOST': config('DATABASE_HOST'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
    }
}

