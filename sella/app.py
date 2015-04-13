#!/usr/bin/env python
#-*- coding: utf-8 -*-
from importd import d
import os

def get_sentry_apps():
    if 'SENTRY_DSN' in os.environ:
        return ('raven.contrib.django.raven_compat',)
    else:
        return ()

DEBUG = False

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
    ADMINS=(),
    mounts={"demo": "/demo/", 'rest_framework': '/api/'}
)

if __name__ == "__main__":
    d.main()
