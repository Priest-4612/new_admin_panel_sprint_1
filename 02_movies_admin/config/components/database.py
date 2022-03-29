import os

default_engine = 'django.db.backends.postgresql'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', default=default_engine),
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('DB_HOST', default='127.0.0.1'),
        'PORT': os.getenv('DB_PORT', default='5432'),
        'OPTIONS': {
           'options': '-c search_path=public,content',
        },
    },
}
