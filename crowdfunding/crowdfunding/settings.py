import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url



# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env") 

# AWS S3 Settings for Media Uploads
STORAGES = {
    'default': {
        'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
    },
    'staticfiles': {
        'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
    },
}


AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME", "ap-southeast-2")  # Replace with your region
AWS_REGION = AWS_S3_REGION_NAME

AWS_QUERYSTRING_AUTH = False  # URLs won't include auth query strings
AWS_S3_FILE_OVERWRITE = False  # Prevent overwriting files with the same name
AWS_DEFAULT_ACL = None  # Use bucket-level permissions
AWS_S3_ADDRESSING_STYLE = "virtual"
# AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"
# DEFAULT_FILE_STORAGE = 'myapp.storage_backends.MediaStorage'

# MEDIA_URL: S3 Base URL for uploaded files
# MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/"
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# SECURITY SETTINGS
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-1+558-tm+#71!o7*dhg$6f%2*x%838zajahkykpwgzu_0_a%!)"
)
DEBUG = os.environ.get("DJANGO_DEBUG") != "False"
# ALLOWED_HOSTS = ["*"]  # Modify this for production
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'drops2ocean.netlify.app', 'drops2ocean-031097d5a977.herokuapp.com']

# CORS SETTINGS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost",
#     "https://your-frontend-url.com",
# ]

# APPLICATION CONFIG
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
    'django_extensions',
    'storages'
]

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

# DATABASE CONFIG
DATABASES = {
    'default': dj_database_url.config(default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}", conn_max_age=500)
}

# STATIC AND MEDIA SETTINGS
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_STORAGE = 'myapp.storage_backends.StaticStorage'

# REST FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'
ROOT_URLCONF = 'crowdfunding.urls'
WSGI_APPLICATION = 'crowdfunding.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Optional: Path to custom templates directory
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
