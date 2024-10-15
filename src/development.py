from dotenv import load_dotenv

DEBUG = False

load_dotenv('.env.dev')

DEBUG = True

ALLOWED_HOSTS = ['*']
