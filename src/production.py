import os

CSRF_TRUSTED_ORIGINS = [
        'https://*.up.railway.app',
        "https://datamotive-production.up.railway.app",
    ]

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = [
    os.environ.get('RAILWAY_STATIC_URL', ''),
]

DEBUG = False
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["PGDATABASE"],
        'USER': os.environ["PGUSER"],
        'PASSWORD': os.environ["PGPASSWORD"],
        'HOST': os.environ["PGHOST"],
        'PORT': os.environ["PGPORT"],
    }
}