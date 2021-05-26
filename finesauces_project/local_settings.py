# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tov0+h__p5#d+mn1qrztk773gg)ghk)fq$#27=uutm+e!+b!!i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'finesauces',
        'USER': 'finesaucesadmin',
        'PASSWORD': 'Killzone2',
        'HOST': 'localhost'
    }
}
