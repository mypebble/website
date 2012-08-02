from setuptools import setup, find_packages

setup(
    name='mypebble',
    version='1.0.0',
    description="MyPebble website",
    author="SF Software limited t/a Pebble",
    author_email="sysadmin@talktopebble.co.uk",
    url="http://www.mypebble.co.uk",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'psycopg2>=2.4.2',

        'gunicorn==0.14.3',

        'html5lib==0.95',

        'Django==1.4',
        'South==0.7.5',

        'django-cms==2.3',
        'django-mptt==0.5.1',
        'django-forms-builder==0.7.10',

        'django-mptt==0.5.1',
        'django-picklefield==0.2.1',
        'django-activelink==0.3',
        'django-classy-tags==0.3.4.1',
        'django-reversion==1.6.1',
        'django-coverage==1.2.2',
        'django_email_auth==0.1.3',
        'django_logtail==0.0.2',

        'cmsplugin_blog==1.1.2',

        'ssh',
        'fabric',
    ],
)
