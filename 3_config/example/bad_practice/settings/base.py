import os

BASE_DIR = '.'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, '/path/')
MEDIA_URL = '/path/'