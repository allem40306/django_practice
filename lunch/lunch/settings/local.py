from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7o=ju_=+p8h%+!%c1=t03l$$8qd-afu&=5e2=^7ffl3tv9p)83'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'POST': 3306,
          'OPTIONS': {
              "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",                                                              
          }

    }
}
