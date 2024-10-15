import os

DEBUG = True

ALLOWED_HOSTS = [
    os.environ.get('RAILWAY_STATIC_URL', ''),
    '.railway.app'
    'motcho.pt',
]