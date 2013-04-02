# Django settings for skeleton project.

import os, dj_database_url

DEBUG = (os.environ['SKELETON_ENV_DEBUG'] == 'TRUE')
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
SITE_NAME = "Skeleton - App"


DATABASES = {'default': dj_database_url.config()}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/uploads/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = os.environ['SKELETON_ENV_STATIC_URL']
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'cqi&k)b6m#w4i!%e7hxme_16_#zb9+9*p4v@2lrb11yak=i%g-'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'skeleton.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'skeleton.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    os.path.join(os.path.dirname(__file__), 'skeleton_app/templates').replace('\\','/'),
)

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'south',
    'gunicorn',

    'skeleton_app',
)

INTERNAL_IPS = (
    '127.0.0.1',

                '10.0.0.10', '10.0.0.20',
    '10.0.0.1', '10.0.0.11', '10.0.0.21',
    '10.0.0.2', '10.0.0.12', '10.0.0.22',
    '10.0.0.3', '10.0.0.13', '10.0.0.23',
    '10.0.0.4', '10.0.0.14', '10.0.0.24',
    '10.0.0.5', '10.0.0.15', '10.0.0.25',
    '10.0.0.6', '10.0.0.16', '10.0.0.26',
    '10.0.0.7', '10.0.0.17', '10.0.0.27',
    '10.0.0.8', '10.0.0.18', '10.0.0.28',
    '10.0.0.9', '10.0.0.19', '10.0.0.29',

    '192.168.56.101',
    '192.168.56.1',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# P3P (for cross domain cookies in IE)
P3P_COMPACT = 'CP="NON DSP COR CURa TIA"'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# S3
# ##

# Uncomment for S3 support
# DEFAULT_FILE_STORAGE = os.environ['SKELETON_ENV_DEFAULT_FILE_STORAGE']
# STATICFILES_STORAGE = os.environ['SKELETON_ENV_STATICFILES_STORAGE']
# AWS_ACCESS_KEY_ID = os.environ['SKELETON_ENV_AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = os.environ['SKELETON_ENV_AWS_SECRET_ACCESS_KEY']
# AWS_STORAGE_BUCKET_NAME = os.environ['SKELETON_ENV_AWS_STORAGE_BUCKET_NAME']


