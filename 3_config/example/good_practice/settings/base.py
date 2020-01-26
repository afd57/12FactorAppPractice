import os

BASE_DIR = '.'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, '/path/')
MEDIA_URL = '/path/'
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "all_ip_allowed")
DATABASE_IP = os.environ.get("DATABASE_IP", "localhost")
DEBUG = os.environ.get("DEBUG", False)

if type(DEBUG) == str and DEBUG.lower() == "true":
    DEBUG = True
