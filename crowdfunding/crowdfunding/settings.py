from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from the .env file
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))

# ==========================
# Core Settings
# ==========================
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'fallback-secret-key')
DEBUG = os.getenv('DJANGO_DEBUG', 'False') != 'False'  # Defaults to False in production

# Allowed hosts for production and development
ALLOWED_HOSTS = [
    'localhost', 
    '127.0.0.1', 
    'drops2ocean.netlify.app', 
    'drops2ocean-031097d5a977.herokuapp.com',
]

# ==========================
# Applications and Middleware
# ==========================
INSTALLED_APPS = [
    'projects.apps.ProjectsConfig',
    'users.apps.UsersConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',  # Enable Cross-Origin Resource Sharing
    'storages',  # AWS S3 Storage Backend
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Serve static files efficiently
    'corsheaders.middleware.CorsMiddleware',  # CORS Middleware MUST be before other middlewares
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',  
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'crowdfunding.urls'
WSGI_APPLICATION = 'crowdfunding.wsgi.application'

# ==========================
# Database Configuration
# ==========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Use Heroku DATABASE_URL when available
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# ==========================
# AWS S3 Storage Settings
# ==========================
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = 'ap-southeast-2'
AWS_S3_FILE_OVERWRITE = False
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
AWS_QUERYSTRING_AUTH = False  # Public URLs do not require querystring authentication
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Media settings for S3
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static Files for Heroku Deployment
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ==========================
# CORS Configuration
# ==========================
# Allow origins for frontend and production
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Development Frontend
    "https://drops2ocean.netlify.app",  # Production Frontend
    "https://drops2ocean-031097d5a977.herokuapp.com",  # Backend Heroku App
]

CORS_ALLOW_CREDENTIALS = True  # Allow credentials like cookies
CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
CORS_ALLOW_HEADERS = ['Authorization', 'Content-Type', 'Accept', 'Origin']

# ==========================
# REST Framework
# ==========================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

# ==========================
# Security Settings
# ==========================
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "https://drops2ocean.netlify.app",
    "https://drops2ocean-031097d5a977.herokuapp.com",
]

# ==========================
# Other Settings
# ==========================
AUTH_USER_MODEL = 'users.CustomUser'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==========================
# Password Validators
# ==========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
