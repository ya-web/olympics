import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load secrets from Docker Swarm secret files (production only)
def load_secret(file_path, default_value=None):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except IOError:
        if default_value is not None:
            return default_value
        raise Exception(f"Error reading secret from {file_path}")

# Check if we are in a production environment
ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev')
DEBUG = ENVIRONMENT != 'prod'

if ENVIRONMENT == 'prod':
    # Load the Django SECRET_KEY from Docker Swarm secret
    DJANGO_SECRET_KEY_PATH = '/run/secrets/django_secret_key'
    SECRET_KEY = load_secret(DJANGO_SECRET_KEY_PATH)
    # Production-specific security settings
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_REFERRER_POLICY = 'same-origin'
# Allowed hosts
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
else:
     # Use a default secret key for development (you can generate a random one for example at https://djecrety.ir/ or elsewhere)
    SECRET_KEY = os.getenv('SECRET_KEY', '^czvym22p0_zlt!i04e-ibg!**=(iz+9drb_ttmhn@7+-ehis&')  # Change this to any random value for dev
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# Authentication and JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',  # DRF
    'rest_framework_simplejwt',  # JWT authentication
    'epreuves',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'frontend', 'build')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_backend.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if ENVIRONMENT == 'prod':
    # Load PostgreSQL credentials from individual Docker Swarm secrets
    POSTGRES_USER_PATH = '/run/secrets/postgres_user'
    POSTGRES_PASSWORD_PATH = '/run/secrets/postgres_password'
    POSTGRES_DB_PATH = '/run/secrets/postgres_db'
    # Database configuration using PostgreSQL secrets os.getenv('ENVIRONMENT', 'dev')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': load_secret(POSTGRES_DB_PATH),  # Database name
            'USER': load_secret(POSTGRES_USER_PATH),  # Database user
            'PASSWORD': load_secret(POSTGRES_PASSWORD_PATH),  # User password
            'HOST': 'postgres',  # Host
            'PORT': '5432',  # Port
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB'),  # Database name
            'USER': os.getenv('POSTGRES_USER'),  # Database user
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),  # User password
            'HOST': 'postgres',  # Host
            'PORT': '5432',  # Port
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'build', 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
