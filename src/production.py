import os
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = [
    os.environ.get('RAILWAY_STATIC_URL', ''),
    '.railway.app'
    'motcho.pt',
]

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}