"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import sys
from datetime import timedelta
from pathlib import Path

import environ

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.base")

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "$34o$kxr79mypgt6#%6+^)n%s@5$t$m19#-mj@sc#o^qii83=q"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
]
# Application definition

THIRT_PARTY_APPS = [
    "import_export",
    "parler",
    "easy_thumbnails",
    "filer",
    "mptt",
    "rest_framework",
    "ckeditor",
    "ckeditor_uploader",
    "drf_yasg",
    "clickuz",
    "corsheaders",
    "oauth2_provider",
    "social_django",
    "rest_framework_social_oauth2",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "rest_framework_swagger",
    "channels",
    "storages",
    "django_grpc_framework",
    "debug_toolbar",
]
CUSTOM_CREATED_APPS = [
    "apps.app",
    "apps.account_account",
    "apps.custom_endpoint_app",
]

INSTALLED_APPS = (
    [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
    ]
    + THIRT_PARTY_APPS
    + CUSTOM_CREATED_APPS
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale/"),)

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "project.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {"default": env.db()}
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'taxi_driver',
        'USER': 'cwc',
        'PASSWORD': 'cwc',
        'HOST': 'localhost',
        'PORT': 5432

    }
}
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase',
#     }
# }

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

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        # 'rest_framework.authentication.SessionAuthentication',
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "rest_framework_social_oauth2.authentication.SocialAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "apps.utils.utils.PageNumberPaginationWithTotalPages",
    "PAGE_SIZE": 30,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FileUploadParser",
    ),
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
        "rest_framework.renderers.TemplateHTMLRenderer",
    ),
}

JWT_AUTH = {
    "JWT_RESPONSE_PAYLOAD_HANDLER": "apps.account_account.utils.my_jwt_response_handler"
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "uz"

LANGUAGES = (
    ("en", "English"),
    ("uz", "Uzbek"),
    ("ru", "Russian"),
)

PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE

PARLER_LANGUAGES = {
    None: (
        {"code": "uz"},
        {"code": "en"},
        {"code": "ru"},
    ),
    "default": {
        "fallback": LANGUAGE_CODE,
        "hide_untranslated": False,
    },
}

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

# STATIC_URL = '/assets/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = "/assets/"
STATIC_ROOT = os.path.join(BASE_DIR, "assets")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


CKEDITOR_UPLOAD_PATH = "content/ckeditor/"

AUTH_USER_MODEL = "account_account.CustomUser"

TESTING = "test" in sys.argv[1:]

if TESTING:

    class DisableMigrations(object):
        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()

CORS_ORIGIN_ALLOW_ALL = True

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
# CORS_ORIGIN_WHITELIST = (
#     'http://edumanager.uz',
#     'edumanager.uz',
#     'https://edumanager.uz',
#     'https://localhost:8017',
#     'http://localhost:8017',
#     'localhost:8017',
#     '0.0.0.0:8017',
#     'http://0.0.0.0:8017',
#     'https://0.0.0.0:8017',
# )
# CORS_ALLOWED_ORIGINS = [
#         'http://dozolab-edupro.uz',
#         'http://dozolab-edupro.uz',
#         'http://edumanager.uz',
#         'https://edumanager.uz',
#         'https://localhost:3117',
#         'http://localhost:3117',
#         'http://127.0.0.1:3117'
#
# ]

SITE_ID = 1
LOGIN_REDIRECT_URL = "/"
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=365),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}

CKEDITOR_CONFIGS = {
    "default": {
        "skin": "moono",
        # 'skin': 'office2013',
        "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
        "toolbar_YourCustomToolbarConfig": [
            {
                "name": "document",
                "items": [
                    "Source",
                    "-",
                    "Save",
                    "NewPage",
                    "Preview",
                    "Print",
                    "-",
                    "Templates",
                ],
            },
            {
                "name": "clipboard",
                "items": [
                    "Cut",
                    "Copy",
                    "Paste",
                    "PasteText",
                    "PasteFromWord",
                    "-",
                    "Undo",
                    "Redo",
                ],
            },
            {"name": "editing", "items": ["Find", "Replace", "-", "SelectAll"]},
            {
                "name": "forms",
                "items": [
                    "Form",
                    "Checkbox",
                    "Radio",
                    "TextField",
                    "Textarea",
                    "Select",
                    "Button",
                    "ImageButton",
                    "HiddenField",
                ],
            },
            "/",
            {
                "name": "basicstyles",
                "items": [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Strike",
                    "Subscript",
                    "Superscript",
                    "-",
                    "RemoveFormat",
                ],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Outdent",
                    "Indent",
                    "-",
                    "Blockquote",
                    "CreateDiv",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                    "-",
                    "BidiLtr",
                    "BidiRtl",
                    "Language",
                ],
            },
            {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
            {
                "name": "insert",
                "items": [
                    "Image",
                    "Flash",
                    "Table",
                    "HorizontalRule",
                    "Smiley",
                    "SpecialChar",
                    "PageBreak",
                    "Iframe",
                ],
            },
            "/",
            {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            {"name": "tools", "items": ["Maximize", "ShowBlocks"]},
            {"name": "about", "items": ["About"]},
            "/",  # put this to force next toolbar on new line
            {
                "name": "yourcustomtools",
                "items": [
                    # put the name of your editor.ui.addButton here
                    "Preview",
                    "Maximize",
                    # 'Youtube'
                ],
            },
        ],
        "toolbar": "YourCustomToolbarConfig",  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        "tabSpaces": 4,
        "extraPlugins": ",".join(
            [
                "uploadimage",  # the upload image feature
                # your extra plugins here
                "div",
                "autolink",
                "autoembed",
                "embedsemantic",
                "autogrow",
                # 'devtools',
                "widget",
                "lineutils",
                "clipboard",
                "dialog",
                "dialogui",
                "elementspath"
                # 'youtube'
            ]
        ),
    }
}
SMS_LOGIN = env("SMS_LOGIN")
SMS_KEY = env("SMS_KEY")

CELERY_BROKER_URL = "amqp://localhost"
ASGI_APPLICATION = "project.asgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

CLICK_SETTINGS = {
    "ENDPOINT": "https://api.click.uz/v2/merchant/",
    "merchant_id": "12915",
    "service_id": "17820",
    "merchant_usr_id": "19716",
    "secret_key": "nD3jMQINoSa",
}

# Celery Configuration Options
CELERY_TIMEZONE = "Asia/Tashkent"
CELERY_TASK_TRACK_STARTED = True
