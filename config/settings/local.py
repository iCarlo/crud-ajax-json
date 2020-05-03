from .base import *

DEBUG = True

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_database',
        'USER': 'postgres',
        'PASSWORD': 'CARLYN2128',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
"""

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


EMAIL_HOST: 'localhost'
EMAIL_PORT: 1025
EMAIL_HOST_USER: ''
EMAIL_HOST_PASSWORD: ''
EMAIL_USE_TLS: ''
EMAIL_USE_SSL: ''


"""
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
"""

"""
DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}
"""
