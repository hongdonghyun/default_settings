# debug.py
# base.py에 있는 값을 불러옴 import *로 무조건 설정할것
from .base import *

# base.py에 있는 CONFIG_SECRET_DEBUG_FILE값을 읽어옴
config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')

# media URLs
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')

# WSGI setting
WSGI_APPLICATION = 'config.wsgi.debug.application'

# debug모드에서만 사용하는 앱들
INSTALLED_APPS += [
    # add your debug apps
]

# 로컬 테스트용 DB설정
DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        "HOST": '',
        'PORT': '',
    },
}
"""
brew install mysql
brew link --overwrite --dry-run mysql
brew link mysql

create database localdb;
create user mysql_local identified by 'ghdehdgus';
grant all on localdb.* to 'mysql_local'@'%';
flush privileges;

"""

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

print('@@@@@@ DEBUG @@@@@@ : ', DEBUG)
print('@@@@@@ ALLOWED_HOSTS @@@@@@ : ', ALLOWED_HOSTS)
