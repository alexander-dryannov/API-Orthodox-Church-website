import os
from .base import *
from dotenv import load_dotenv, find_dotenv

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

load_dotenv(find_dotenv('.prod.env'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.production.sqlite3',
    }
}

CORS_ORIGIN_WHITELIST = []

admin_username = os.getenv('EMAIL_USERNAME')
admin_email = os.getenv('EMAIL')

ADMINS = (
    (admin_username, admin_email),
)

if os.getenv('EMAIL_USE_TLS') is not None:
    EMAIL_USE_TLS = bool(os.getenv('EMAIL_USE_TLS'))
if os.getenv('EMAIL_USE_SSL') is not None:
    EMAIL_USE_SSL = bool(os.getenv('EMAIL_USE_SSL'))
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT'))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
SERVER_EMAIL = os.getenv('SERVER_EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')