"""Проектное задание панель администратора."""

import os
from pathlib import Path

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('APP_KEY', None)

DEBUG = os.environ.get('APP_DEBUG', False) == 'True'

ALLOWED_HOSTS = os.environ.get('APP_URL', '127.0.0.1').split(', ')

include(
    'components/apps.py',
    'components/database.py',
    'components/middleware.py',
    'components/localization.py',
    'components/password_validators.py',
    'components/templates.py',
)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
