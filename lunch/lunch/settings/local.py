from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7o=ju_=+p8h%+!%c1=t03l$$8qd-afu&=5e2=^7ffl3tv9p)83'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}

