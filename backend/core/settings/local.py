import os
from .base import *
from dotenv import load_dotenv, find_dotenv

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

load_dotenv(find_dotenv('.dev.env'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.development.sqlite3',
    }
}

CORS_ORIGIN_WHITELIST = ['http://localhost:3000', 'http://127.0.0.1:8000']
