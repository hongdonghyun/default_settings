# debug.py
# base.py에 있는 값을 불러옴 import *로 무조건 설정할것
from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

WSGI_APPLICATION = 'config.wsgi.deploy.application'

# aws server,s3 settings
AWS_ACCESS_KEY_ID = config_secret_deploy['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret_deploy['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret_deploy['aws']['s3_bucket_name']
AWS_S3_REGION_NAME = config_secret_deploy['aws']['s3_region_name']
S3_USE_SIGV4 = True

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'

DATABASES = config_secret_deploy['django']['databases']

INSTALLED_APPS += [
    # add your deploy apps
    'storages',
]

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']