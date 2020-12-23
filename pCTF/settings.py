"""
Django settings for pCTF project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "<replace>"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "gameserver",
    "martor",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.humanize',
    'crispy_forms',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "gameserver.middleware.TimezoneMiddleware",
]

ROOT_URLCONF = "pCTF.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
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

WSGI_APPLICATION = "pCTF.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"


# Auth settings

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

AUTH_USER_MODEL = "gameserver.User"

LOGIN_REDIRECT_URL = "/accounts/profile"

LOGOUT_REDIRECT_URL = "/"

# ACCOUNT_ACTIVATION_DAYS = 7
# REGISTRATION_OPEN = True
# REGISTRATION_SALT = '<registration salt here>'

ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_FORMS = {"signup": "gameserver.forms.PCTFSignupForm"}

TOS_URL = "/tos"


# Email settings

EMAIL_BACKEND = "<your email backend>"


# S3 STORAGE CONFIGURATION
# FOLLOW https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
DEFAULT_FILE_STORAGE = ""
AWS_S3_REGION_NAME = ""
AWS_S3_ENDPOINT_URL = ""
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_STORAGE_BUCKET_NAME = ""
AWS_S3_FILE_OVERWRITE = False

STATICFILES_STORAGE = ""


# reCAPTCHA settings

RECAPTCHA_PUBLIC_KEY = "<your recaptcha public key>"
RECAPTCHA_PRIVATE_KEY = "<your recaptcha private key>"


# Google Analytics settings

GOOGLE_ANALYTICS_ON_ALL_VIEWS = False
GOOGLE_ANALYTICS_TRACKING_ID = None


# NavBar settings

NAVBAR = {
    "Problems": "/problems/",
    "Submissions": "/submissions/",
    "Users": "/users/",
    "Organizations": "/organizations/",
}


# Meta tag settings

DESCRIPTION = "pCTF is a open-source online platform for people to host or participate in CTF contests."
KEYWORDS = [
    "pCTF",
    "PNOJ",
    "ctf",
    "open source",
    "online judge",
    "online platform",
    "cybersecurity",
]
SCHEME = "https"
PAYMENT_POINTERS = []  # Your Interledger Payment Pointers for Web Monetization


# Martor settings

MARTOR_THEME = 'semantic'

# Other settings

SITE_ID = 1

CRISPY_TEMPLATE_PACK = "bootstrap4"

SILENCED_SYSTEM_CHECKS = ["urls.W002"]

DEFAULT_TIMEZONE = 'UTC'

try:
    from pCTF.config import *
except ImportError:
    print("Please create a config file to override values in settings.py")