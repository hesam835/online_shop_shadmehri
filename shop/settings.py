"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import environ
env = environ.Env()
environ.Env.read_env()
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1=1j76v@($3z=5755@47^kh1q!fe^64&j-$%o-tjfcpg2zejx1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'debug_toolbar',
    "drf_spectacular",
    'rest_framework',
    'djoser',
    'rest_framework.authtoken',
    'widget_tweaks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'core',
    'order',
    'product',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]


if DEBUG:
    INTERNAL_IPS = [
        '127.0.0.1',
    ]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'order.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cycle_shop',
        'USER': 'hesam835',
        'PASSWORD': 'Hes@m835sh',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

def show_toolbar(request):
    return True
SHOW_TOOLBAR_CALLBACK = show_toolbar

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
import os

STATIC_URL = 'static/'
STATICFILES_DIRS = [

BASE_DIR / "static",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "accounts.User"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]



REDIS_HOST = 'localhost' # Replace with your Redis server host
REDIS_PORT = 6379 # Replace with your Redis server port
REDIS_DB = 0
# cache
CACHES = {
"default": {
"BACKEND": "django.core.cache.backends.redis.RedisCache",
"LOCATION": env.str("REDIS_URL", "redis://localhost:6379/"),
"KEY_PREFIX": "shop",
"TIMEOUT": 60 * 15, # in seconds: 60 * 15 (15 minutes)
}
}


SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

from datetime import timedelta
SIMPLE_JWT = {
'AUTH_HEADER_TYPES': ('JWT',),
'ACCESS_TOKEN_LIFETIME': timedelta(days=3)
}
DJOSER = {
'SERIALIZERS': {
'user_create': 'accounts.serializers.UserCreateSerializer'
},
}


REST_FRAMEWORK = {
'COERCE_DECIMAL_TO_STRING': False,
'DEFAULT_AUTHENTICATION_CLASSES': (
'rest_framework_simplejwt.authentication.JWTAuthentication',
),
'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

}
SPECTACULAR_SETTINGS = {
'TITLE': 'cycle_shop',
'DESCRIPTION': 'Your project description',
'VERSION': '1.0.0',
}

MERCHANT = "00000000-0000-0000-0000-000000000000"

SANDBOX = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True  # or False if your SMTP server doesn't use TLS
EMAIL_HOST_USER = 'shadmehrihesam@gmail.com'
EMAIL_HOST_PASSWORD = 'qdbm lals ymcw tjqf'
