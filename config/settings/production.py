from .base import *
import os

INSTALLED_APPS += ['whitenoise.runserver_nostatic']
MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware'] + MIDDLEWARE

DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = [".herokuapp.com", "127.0.0.1", "localhost"]
SECRET_KEY = os.environ.get("SECRET_KEY", "clave_backup_conocida")
try:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            ssl_require=True
        )
    }
except ImportError:
    pass

CORS_ALLOWED_ORIGINS = [
    "https://connos-park-frontend.herokuapp.com",
]
