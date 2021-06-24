from .base import *

# Seguridad
DEBUG = False
hosts=config('ALLOWED_HOSTS', default='*')
ALLOWED_HOSTS = [hosts]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DATABASE_ENGINE'),
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST', default='localhost'),
        'PORT': config('PORT'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

STATIC_URL = config('STATIC_URL', default="/static/")
STATIC_ROOT = config('STATIC_ROOT', default="./static/")
MEDIA_URL = config('MEDIA_URL', default="/uploads/")
MEDIA_ROOT = config('MEDIA_ROOT', default="./uploads/")


# Email
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'

EMAIL_HOST = config('EMAIL_HOST', default='mail.booster.com.mx')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='billy@booster.com.mx')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='billy123!')
EMAIL_PORT = config('EMAIL_PORT', default=465)