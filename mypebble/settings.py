# -*- coding: utf-8 -*-
import os

gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TESTING = True
TEMPLATE_DEBUG = DEBUG
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
LOG_FILE = os.path.join(PROJECT_PATH, 'mypebble.log')
INTERNAL_IPS = ('127.0.0.1',)

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
        'NAME': 'circle_test',
        'USER': 'ubuntu',
        'PASSWORD': ':',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

try:
    from local_settings import DEFAULT_DATABASE
except ImportError:
    pass

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
STATIC_ROOT = os.path.join(PROJECT_PATH, "collected-static/")
STATIC_URL = "/static/"

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
    'sekizai.context_processors.sekizai',
    'cms.context_processors.media',
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

    ('login.html', 'Login Template'),
    ('404.html', 'Error 404'),
    ('500.html', 'Error 500'),

    ('privacy.html','Privacy Template'),
    ('tandc.html','T&C Template'),
    ('accessibility.html','Accessibility Template'),
    ('security.html','Security Template'),
    ('training.html', 'Webinar Training Template'),
    ('blog.html','Blog Template'),

    #support video templates
    ('support_document_ul.html','User Login Template'),
    ('support_document_al.html','Apply Licence Template'),
    ('support_document_sl.html','SFM location Template'),
    ('support_document_rb.html','Receipts to Bank Template'),
    ('support_document_rp.html','Record Payments Template'),
    ('support_document_rec.html','Reconcile Bank Template'),
    ('support_document_pe1.html','PeriodEnd 1 Template'),
    ('support_document_pe2.html','PeriodEnd 2 Template'),

    #support videos fm
    ('support_document_ma.html','Manage Accounts FM Template'),
    ('support_document_mn.html','Manage Names FM Template'),
    ('support_document_st.html','Search Transaction FM Template'),
    ('support_document_wnp.html','Whos not paid FM Template'),
    ('support_document_pefm.html', 'Period End Closedown FM Template'),
    ('support_document_gs.html','Get Satisfaction FM Template'),
    ('support_document_pa.html','Offers FM Template'),
    ('support_document_bh.html','Bank History FM Template'),
    ('support_document_ct.html','Cancel Transaction FM Template'),
    ('support_document_sq.html','Squid FM Template'),

    ('support_document_rpfm.html','Receipts and Record a Payment FM Template'),
    ('support_document_ar.html','Account Report Create Acc FM Template'),
    ('support_document_rbfm.html','Receipt to Bank FM Template'),
    ('support_document_brfm.html','Reconcile Bank FM Template'),

    ('support_document_iep.html','Import ePayment FM Template'),
    ('support_document_mt.html','Make Transfer FM Template'),
    ('support_document_gift.html','Gift Aid FM Template'),
    ('support_document_sa.html','Settlement Account FM Template'),
    ('support_document_tsa.html','Transfer Settlement Account FM Template'),
    ('support_document_ubsabt.html','Reconcile Bank Statement Amend Bank Transfer FM Template'),

    #misc
    ('misc.html', 'Misc Template'),
    ('about.html', 'About Template'),
    ('upgrade.html', 'Upgrade Template'),
    ('misapp.html', 'Misapp Template'),
    ('test.html', 'Test Template'),
    ('newsletter.html', 'Newsletter'),
    ('blog.html', 'blog Template'),
    #('cmsplugin_blog_base.html', 'cmsplugin_blog'),


    ('FM_terms.html', 'FM Terms Template'),
    ('Joinos_terms.html', 'Joinos Template'),


)

#SEO
CMS_SEO_FIELDS = True

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
