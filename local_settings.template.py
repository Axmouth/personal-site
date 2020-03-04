import os

CSRF_COOKIE_SECURE = os.environ.get('DJANGO_CSRF_COOKIE_SECURE', 'True') != 'True'
SESSION_COOKIE_SECURE = os.environ.get('DJANGO_SESSION_COOKIE_SECURE', 'True') != 'True'
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') != 'False'
CONN_MAX_AGE = int(os.environ.get('DJANGO_CONN_MAX_AGE', '5'))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'mybiosite/mybiosite/db.sqlite3'),
    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_POSTGRES_DB', 'my_bio_site'),
        'USER': os.environ.get('DJANGO_POSTGRES_USER', 'my_bio_site_user'),
        'HOST': os.environ.get('DJANGO_POSTGRES_HOST', 'host.docker.internal'),
        'PORT': os.environ.get('DJANGO_POSTGRES_PORT', 5432),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'my_bio_site'),
    }
}