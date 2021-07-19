"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

from decouple import config, Csv
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .logging import CONFIG as LOG_CONFIG

ENVIRON = config("ENVIRON", default="prod")

sentry_sdk.init(
    dsn="https://ad9a9f987fa949a899c3b890ef4cd112"
    "@o354850.ingest.sentry.io/5868398",
    integrations=[DjangoIntegration()],
    environment=ENVIRON,
    traces_sample_rate=1.0,
    send_default_pii=True,
    release="tda@0.1.0",  # change in poetry as well
)

LOGGING = LOG_CONFIG

PROJECT_NAME = "The Doe Agency"
PROJECT_SLUG = "the-doe-agency"
PROJECT_CODE = "TDA"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default=[], cast=Csv())

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configuring-internal-ips
INTERNAL_IPS = config("INTERNAL_IPS", default=[], cast=Csv())


# Application definition ---------------------------------------------------- #

INSTALLED_APPS = [
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
    # 3rd party apps
    "django_filters",
    "rest_framework",
    "rest_framework_simplejwt",
    # health_check
    "health_check",
    "health_check.db",
    "health_check.cache",
    "health_check.storage",
    "health_check.contrib.migrations",
    # 'health_check.contrib.celery',
    # 'health_check.contrib.celery_ping',
    "health_check.contrib.psutil",
    # 'health_check.contrib.s3boto3_storage',
    # 'health_check.contrib.rabbitmq',
    # 'health_check.contrib.redis',
    # project apps
    "core",
    "scraper",
]

SITE_ID = 1  # Sites framework

if ENVIRON == "dev":
    INSTALLED_APPS.append("debug_toolbar")

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

AUTH_USER_MODEL = "core.User"

WSGI_APPLICATION = "project.wsgi.application"


# Database ------------------------------------------------------------------ #
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.postgresql"),
        "HOST": config("DB_HOST", default="127.0.0.1"),
        "PORT": config("DB_PORT", default=5432, cast=int),
        "NAME": config("DB_NAME", default="tda_db"),
        "USER": config("DB_USER", default="tda_user"),
        "PASSWORD": config("DB_PASS", default="tda_pass"),
    }
}


# Password validation ------------------------------------------------------- #
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation"
        ".UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        ".MinimumLengthValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        ".CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        ".NumericPasswordValidator"
    },
]


# Internationalization ------------------------------------------------------ #
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = config("TIME_ZONE", default="UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) ------------------------------------ #
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = (
    BASE_DIR / "static"
)  # production, don't forget to run collectstatic
STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",
]  # development environment

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Django REST Framework -------------------------------------------------------
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        # "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"
    ],
    "DEFAULT_FILTER_BACKENDS": [
        # django-filters
        # https://www.django-rest-framework.org/api-guide/filtering/
        # https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html
        "django_filters.rest_framework.DjangoFilterBackend",
        # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
        "rest_framework.filters.SearchFilter",
        # https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination"
    ".PageNumberPagination",
    "PAGE_SIZE": 100,
}


# DRF SimpleJWT ---------------------------------------------------------------
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("JWT",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication"
    ".default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=15),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}
