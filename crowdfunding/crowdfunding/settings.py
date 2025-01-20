import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url



# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env") 


# SECURITY SETTINGS
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-1+558-tm+#71!o7*dhg$6f%2*x%838zajahkykpwgzu_0_a%!)"
)


DEBUG = os.environ.get("DJANGO_DEBUG") != "False"
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'drops2ocean.netlify.app', 'drops2ocean-031097d5a977.herokuapp.com']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get(
    'DJANGO_DEBUG'
) != 'False'

ALLOWED_HOSTS = ['*']

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173",
#     "https://drops2ocean.netlify.app",
#     "http://127.0.0.1:8000"
# ]


CORS_ALLOW_ALL_ORIGINS = True


# Application definition

INSTALLED_APPS = [
    'projects.apps.ProjectsConfig',
    'users.apps.UsersConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': [
      'rest_framework.authentication.TokenAuthentication',
  ]
}

AUTH_USER_MODEL = 'users.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'crowdfunding.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'crowdfunding.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # AWS S3 Settings for Media Uploads
# AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", "ap-southeast-2")  # Replace with your region

# AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"

# AWS_QUERYSTRING_AUTH = False  # URLs won't include auth query strings
# AWS_S3_FILE_OVERWRITE = False  # Prevent overwriting files with the same name
# AWS_DEFAULT_ACL = None  # Use bucket-level permissions



# # Location prefixes in the S3 bucket
# AWS_STATIC_LOCATION = 'static'
# AWS_MEDIA_LOCATION = 'media'

# STORAGES = {
#     # Media storage (S3)
#     'default': {
#         'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
#     },
#     # Static files storage (WhiteNoise for local)

#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }
    # 'staticfiles': {
    #     'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',  # Static Storage
    #     'OPTIONS': {
    #         'location': AWS_STATIC_LOCATION,
    #     },
        # }


# # URLs for media and static files
# STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/"
# MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_MEDIA_LOCATION}/"

# # Local development settings for static files
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # Local static files
# STATIC_ROOT = os.path.join(BASE_DIR, "assets")  # Directory for collectstatic








# # APPLICATION CONFIG
# INSTALLED_APPS = [
#     'projects.apps.ProjectsConfig',
#     'users.apps.UsersConfig',
#     'rest_framework',
#     'rest_framework.authtoken',
#     'corsheaders',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'django_extensions',
#     # 'storages',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'corsheaders.middleware.CorsMiddleware',  
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',  
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]


# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         # 'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Optional: Path to custom templates directory
#         'DIRS': [],

#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# # DATABASE CONFIG
# DATABASES = {
#     'default': dj_database_url.config(default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}", conn_max_age=500)
# }


# # REST FRAMEWORK SETTINGS
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
#     ]
# }


# # INTERNATIONALIZATION
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTH_USER_MODEL = 'users.CustomUser'
# ROOT_URLCONF = 'crowdfunding.urls'
# WSGI_APPLICATION = 'crowdfunding.wsgi.application'



# # CORS SETTINGS
# # CORS_ALLOWED_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5174",
#     "https://drops2ocean.netlify.app",
#     "http://127.0.0.1:8000"
# ]



# # Optional Logging for Debugging S3 Issues
# if DEBUG:
#     import logging
#     logging.basicConfig(level=logging.INFO)


# # STATIC AND MEDIA SETTINGS
# # STATIC_URL = '/static/'
# # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# # AWS_LOCATION = 'static'


# # STATICFILES_STORAGE = 'myapp.storage_backends.StaticStorage'
# # MEDIA_URL = '/media/'
# # STATIC_URL = '/static/'
# # STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# # STATIC_ROOT = os.path.join(BASE_DIR, "assets")
# # STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage" 
# # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # AWS_REGION = AWS_S3_REGION_NAME

# # AWS_S3_ADDRESSING_STYLE = "virtual"


# # AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

# # MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"
# # DEFAULT_FILE_STORAGE = 'myapp.storage_backends.MediaStorage'

# # STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
# # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# # MEDIA_URL: S3 Base URL for uploaded files
# # MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/"
# # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')











