import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = os.environ.get("DJANGO_SECRET")

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "192.168.0.46"]

JWT_ACCESS_LIFETIME = timedelta(days=123)
JWT_REFRESH_LIFETIME = timedelta(days=123)
CORS_ALLOWED_ORIGINS = ["http://127.0.0.1:3000", "http://127.0.0.1:5173", "http://192.168.0.46:5173"]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = ["http://127.0.0.1:3000", "http://127.0.0.1:5173", "http://192.168.0.46:5173"]

MAX_TAGS_PER_ENTITY = 10

X_FRAME_OPTIONS = 'SAMEORIGIN'

AUTH_USER_MODEL = "user.User"

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'core.utils.searching.paginator.Paginator',
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
    'SEARCH_PARAM': 'q',
    'ORDERING_PARAM': 'ordered_by',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        "middlewares.auth.AuthenticationSystem",
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter'
    ],
    'EXCEPTION_HANDLER': 'core.exception_receiver.err_handler'
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'modules.user',
    'modules.document',
    'modules.tags',
    'modules.reactions',
    'modules.commentaries',
    'modules.questions',
    'modules.files',
    'modules.structure'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fist3_prototype_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'fist3_prototype_api.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [

]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False

EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

FILE_UPLOAD_MAX_MEMORY_SIZE = 8388608
FIRST_DAY_OF_WEEK = 1

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = "files/"
MEDIA_ROOT = BASE_DIR / 'files'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
