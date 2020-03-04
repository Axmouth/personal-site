"""
Django settings for mybiosite project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '8wf)sdd!33ckz6fk=nijskg!dp%@tru#yti7kg^!grr-_8n%xd'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '8wf)sdd!33ckz6fk=nijskg!dp%@tru#yti7kg^!grr-_8n%xd')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

SITE_ID = int(os.environ.get('DJANGO_SITE_ID', '8'))

ALLOWED_HOSTS = [
    os.environ.get('SERVER_IP', '194.5.159.62'),
    'localhost:8000',
    'localhost',
    'giorgosnikolop.info'
]

X_FRAME_OPTIONS = 'SAMEORIGIN'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mybiosite',
    'projects',
    'blog',
    'home_page',
    'django_summernote',
    'django.contrib.sites',
    'django_comments_xtd',
    'django_comments',
    'debug_toolbar',
    'django.contrib.flatpages',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'mybiosite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["mybiosite/templates/"],
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

WSGI_APPLICATION = 'mybiosite.wsgi.application'
COMMENTS_APP = 'django_comments_xtd'

# Either enable sending mail messages to the console:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST', 'localhost')
EMAIL_PORT = 25
EMAIL_HOST_USER = 'noreply'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = "Helpdesk <helpdesk@giorgosnikolop.info>"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DJANGO_POSTGRES_DB', 'my_bio_site'),
        'USER': os.environ.get('DJANGO_POSTGRES_USER', 'my_bio_site_user'),
        'HOST': os.environ.get('DJANGO_POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('DJANGO_POSTGRES_PORT', 5432),
        'PASSWORD': os.environ.get('DJANGO_POSTGRES_PASSWORD', 'my_bio_site'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

print(BASE_DIR)
print(STATIC_ROOT)

# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static'),
# ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

#DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000000000000000

SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    #'iframe': True,

    # Or, you can set it as False to use SummernoteInplaceWidget by default - no iframe mode
    # In this case, you have to load Bootstrap/jQuery stuff by manually.
    # Use this when you're already using Bootstraip/jQuery based themes.
    #'iframe': False,

    # You can put custom Summernote settings
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,

        # Change editor size
        'width': '75%%',
        #'height': '480',

        # Use proper language setting automatically (default)
        #'lang': None,

        # You can also add custom settings for external plugins
        #'print': {
        #    'stylesheetUrl': '/some_static_folder/printable.css',
        #},
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            # You have to include theme file in 'css' or 'css_for_inplace' before using it.
            'theme': 'monokai',
        },
    },

    # Need authentication while uploading attachments.
    'attachment_require_authentication': True,

    # Set `upload_to` function for attachments.
    #'attachment_upload_to': my_custom_upload_to_func(),

    # Set custom storage class for attachments.
    #'attachment_storage_class': 'my.custom.storage.class.name',

    # Set custom model for attachments (default: 'django_summernote.Attachment')
    #'attachment_model': 'my.custom.attachment.model', # must inherit 'django_summernote.AbstractAttachment'

    # You can disable attachment feature.
    #'disable_attachment': False,

    # Set `True` to return attachment paths in absolute URIs.
    #'attachment_absolute_uri': False,

    # test_func in summernote upload view. (Allow upload images only when user passes the test)
    # https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin

    #def example_test_func(request):
    #    return request.user.groups.filter(name='group_name').exists()

    #'test_func_upload_view': example_test_func,

    # You can add custom css/js for SummernoteWidget.
    'css': (
    ),
    'js': (
    ),

    # You can also add custom css/js for SummernoteInplaceWidget.
    # !!! Be sure to put {{ form.media }} in template before initiate summernote.
    'css_for_inplace': (
    ),
    'js_for_inplace': (
    ),

    # Codemirror as codeview
    # If any codemirror settings are defined, it will include codemirror files automatically.
    'css': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/theme/monokai.min.css',
    ),

    # Lazy initialize
    # If you want to initialize summernote at the bottom of page, set this as True
    # and call `initSummernote()` on your page.
    #'lazy': True,

    # To use external plugins,
    # Include them within `css` and `js`.
    #'js': {
        #'/some_static_folder/summernote-ext-print.js',
        #'//somewhere_in_internet/summernote-plugin-name.js',
    #},
}

# CSRF_COOKIE_SECURE = os.environ.get('DJANGO_CSRF_COOKIE_SECURE', 'True') == 'True'
# SESSION_COOKIE_SECURE = os.environ.get('DJANGO_SESSION_COOKIE_SECURE', 'True') == 'True'
# SECURE_SSL_REDIRECT = True
# SECURE_REFERRER_POLICY
# SECURE_HSTS_SECONDS
CONN_MAX_AGE = int(os.environ.get('DJANGO_CONN_MAX_AGE', '5'))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
