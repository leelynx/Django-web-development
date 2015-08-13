"""
Django settings for mysite01 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#__*__ coding:utf-8 __*__
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=e^8szo=!m=1v&m6*7n9hy0#kwtbvq5op-)v_#id)t%boi@fwf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = ('f:/webpro01/mysite01/templates',)
# Application definition

FILE_CHARSET = 'utf-8'
DEFAULT_CHARSET = 'utf-8'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp',
    'calcmd5_app',
    'Calcmd5App',
    'booksapp',
    'FileTransfer',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite01.urls'

WSGI_APPLICATION = 'mysite01.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'admindb',
        'USER': 'root',
        'HOST': '127.0.0.1',
        'PASSWORD': '',
        'PORT': '3306',
        
    },
    'md5_storage': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'md5_storage',
        'USER': 'root',
        'HOST': '127.0.0.1',
        'PASSWORD': '',
        'PORT': '3306',
        
    } ,
    'books': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'books',
        'USER': 'root',
        'HOST': '127.0.0.1',
        'PASSWORD': '',
        'PORT': '3306',
        
    }     
}

DATABASE_ROUTERS = ['mysite01.dbconfig.Mydb',]

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'