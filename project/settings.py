import os
from dotenv import load_dotenv
from environs import Env
load_dotenv(dotenv_path='.env', verbose=True)
env = Env()
env.read_env()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env('HOST'),
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': env('USER'),
        'PASSWORD': env('DB_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SITE_SECRET_KEY')

DEBUG = env.bool('DEBUG_TRUE')

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'datacenter/templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
