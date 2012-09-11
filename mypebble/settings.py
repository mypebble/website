# -*- coding: utf-8 -*-
import os

gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
LOG_FILE = os.path.join(PROJECT_PATH, 'mypebble.log')

# Django settings for mypebble project.
try:
    from mypebble.local_settings import *
except ImportError:
    pass

ADMINS = (
     ('AH', 'ah@talktopebble.co.uk'),
     ('ENQ', 'www+enquiries@mypebble.co.uk'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mypebble_cms',
        'USER': 'pebble',
        'PASSWORD': 'pebble',
        'HOST': 'localhost',
        'PORT': '',
    }
}



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

LANGUAGES = [
    ('en', 'English'),
]

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = os.path.join(PROJECT_PATH, "another-static/")
STATIC_URL = "/static/"
ADMIN_MEDIA_PREFIX = "/static/admin/"

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'f&ue2^6sn=!yhpyc^!n3_7t5qg7sxynqmcg57vs9cf2$@-5xi&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',

)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',

    #'cmsplugin_blog.middleware.MultilingualBlogEntriesMiddleware',
)

CMSPLUGIN_BLOG_PLACEHOLDERS = ('first', 'second', 'third')

ROOT_URLCONF = 'mypebble.urls'

TEMPLATE_DIRS = (
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
  # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'templates'),
    os.path.join(PROJECT_PATH, 'templates/forms'),
    #os.path.join(PROJECT_PATH, 'templates/cmsplugin_blog'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)


INSTALLED_APPS = (
   'cms', #django CMS itself
   'mptt', #utilities for implementing a modified pre-order traversal tree
   'menus', #helper for model independent hierarchical website navigation
   'south', #intelligent schema and data migrations
   'sekizai', #for javascript and css management
   'activelink',
   'forms_builder.forms',
   'gunicorn',
   #blog stuff
   #'simple_translation',
   #'cmsplugin_blog',
   #'tagging',
   #'missing',
   # 'staticfiles',
   # MK 29-Aug-2012: random quotes for testimonials
    'cmsplugin_randomquote',
    'cms.plugins.file',
    'cms.plugins.video',
    #'cms.plugin.flash',
    #'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    #'cms.plugins.teaser',


    'cms.plugins.text',  #text plugin
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
    'mypebble.core',
    'mypebble.testimonials',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['log_file', ],
            'level': 'ERROR',
            'propagate': False,
        },
        'mypebble': {
            'handlers': ['log_file', ],
            'level': 'INFO',
        },
    },
}

CMS_TEMPLATES = (
    ('home.html', 'Home Template'),
    ('product_fm.html', 'Product FM Template'),
    ('product_ff.html', 'Product FF Template'),
    ('support.html', 'Support Template'),
	('support_product.html', 'Support Product Template'),
	('support_productSFF.html', 'Support Product SFF Template'),
	('support_productSFM.html', 'Support Product SFM Template'),
	('support_document.html', 'Support Document Template'),
    ('contact.html', 'Contact Template'),
    ('contact2.html', 'Contact Template'),
    ('login.html', 'Login Template'),
    ('404.html', 'Error 404'),
    ('500.html', 'Error 500'),
    
    ('privacy.html','Privacy Template'),
    ('tandc.html','T&C Template'),
    ('accessibility.html','Accessibility Template'),
    ('security.html','Security Template'),

    ('misc.html', 'Misc Template'),
    ('about.html', 'About Template'),
    ('upgrade.html', 'Upgrade Template'),
    ('test.html', 'Test Template'),
    ('newsletter.html', 'Newsletter'),
    ('blog.html', 'blog Template'),
    #('cmsplugin_blog_base.html', 'cmsplugin_blog'),
)

#for blog
#JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
#JQUERY_UI_JS = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
#JQUERY_UI_CSS = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'

#SEO
CMS_SEO_FIELDS = True
