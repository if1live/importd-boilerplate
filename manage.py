#!/usr/bin/env python
#-*- coding: utf-8 -*-
from importd import d
import os
import sys

def get_sentry_apps():
    if 'SENTRY_DSN' in os.environ:
        return ('raven.contrib.django.raven_compat',)
    else:
        return ()

if 'gunicorn' in sys.argv[0]:
    DEBUG = False
else:
    DEBUG = True

d(
    DEBUG=DEBUG,
    INSTALLED_APPS=(
        # external library
        'django_nose',

        # django rest framework
        'rest_framework',
        'rest_framework.authtoken',

        'sella',
        'demo',
        'api',
    ) + get_sentry_apps(),
    # django-jinja
    DEFAULT_JINJA2_TEMPLATE_EXTENSION='.jinja2',
    TEMPLATE_LOADERS=(
        # django-jinja
        'django_jinja.loaders.AppLoader',
        'django_jinja.loaders.FileSystemLoader',
        # django
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ),
    # django-nose
    TEST_RUNNER='django_nose.NoseTestSuiteRunner',
    # sentry
    RAVEN_CONFIG={
        'dsn': os.environ['SENTRY_DSN'] if 'SENTRY_DSN' in os.environ else '',
    },

    # whitenoise + gzip
    STATICFILES_STORAGE='whitenoise.django.GzipManifestStaticFilesStorage',

    # for heroku deploy
    # '*' or '127.0.0.1' or 'importd-boilerplate.herokuapp.com'
    ALLOWED_HOSTS=['*'],
    EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend',

    mounts={"demo": "/demo/", 'rest_framework': '/api/'}
)

if __name__ == "__main__":
    d.main()
