import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# 環境変数から機密情報を取得しています。SECRET_KEYはDjangoアプリケーションのセキュリティ上非常に重要なキーです。
SECRET_KEY = os.environ.get("SECRET_KEY")

# デバッグモードの設定。デバッグモードは開発時に有効にし、運用時には無効にする必要があります。
DEBUG = bool(os.environ.get("DEBUG", default=0))

# 許可するホスト名のリスト。環境変数からスペースで区切られたリストを取得しています。
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',  # Django REST framework
    'rest_framework.authtoken',  # 認証トークン管理

    'core.apps.CoreConfig',
    'api_user.apps.ApiUserConfig',
    'api_dm.apps.ApiDmConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sns.urls'

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

WSGI_APPLICATION = 'sns.wsgi.application'


# データベースの設定。環境変数からデータベース接続情報を取得しています。
DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE"),  # 使用するデータベースエンジン（例：django.db.backends.postgresql）
        'NAME': os.environ.get("SQL_DATABASE"),  # データベース名
        'USER': os.environ.get("SQL_USER"),  # データベースユーザー
        'PASSWORD': os.environ.get("SQL_PASSWORD"),  # データベースパスワード
        'HOST': os.environ.get("SQL_HOST"),  # データベースホスト
        'PORT': os.environ.get("SQL_PORT"),  # データベースポート
    }
}


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

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
