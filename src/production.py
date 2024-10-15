import os
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = [
    os.environ.get('RAILWAY_STATIC_URL', ''),
]

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

CSRF_TRUSTED_ORIGINS = [
        os.environ.get('RAILWAY_STATIC_URL', ''),
    ]

CORS_ORIGIN_ALLOW_ALL = True