

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2x42krwl_du15#kbir7#!uh*i659n9d3che6e_e7*!pkg!ej#0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'ckeditor',
    'ckeditor_uploader',
    'django.contrib.humanize',
    'apps.main.apps.MainConfig',
    'django_render_partial',
    'apps.company.apps.CompanyConfig',
    'apps.about.apps.AboutConfig',
    'apps.whyUs.apps.WhyusConfig',
    'apps.service.apps.ServiceConfig',
    'apps.sample.apps.SampleConfig',
    'apps.call.apps.CallConfig',
    'apps.search.apps.SearchConfig',
    'apps.mag.apps.MagConfig',
    'apps.chat.apps.ChatConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],'DIRS': [os.path.join(BASE_DIR,'template/'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.main.views.media_admin',
            ],
        },
    },
]

WSGI_APPLICATION = 'web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME':'rank0',
        'USER':'root',
        'PASSWORD':'sadra1383@gmail.com',
        'HOST':'localhost',
        'PORT':'3306'


    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static/'),)


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# جلوگیری از بلاک شدن کوکی در برخی مرورگرها
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'

# به Django بگو که به این دامنه اعتماد کند
CSRF_TRUSTED_ORIGINS = [

    'https://rank0.ir',
    'https://www.rank0.ir',  # در صورت وجود
]

CKEDITOR_UPLOAD_PATH = 'images/cheditor/upload_files/'
CKEDITOR_STORAGE_BACKEND = 'django.core.files.storage.FileSystemStorage'
CKEDITOR_CONFIGS = {
    'default':{
        'toolbar':'Custom',
        'toolbar_Custom':[
            ['Bold','Link','Unlink','Image'],
        ],
    },

    'special':{
        'toolbar':'Special','height':500,
        'toolbar':'full',
        'toolbar_Special':
            [
                ['Bold','Link','Unlink','Image'],
                ['CodeSnippet'],

            ],'extraPlugins':','.join(['codesnippet','clipboard',])
    },
    'special_an':
        {

            'toolbar':'Special','height':500,
            'toolbar_Special':
                [
                    ['Bold'],
                    ['CodeSnippet']

                ],'extraPlugins':','.join(['codesnippet',])
         }
}