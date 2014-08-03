#-*- coding: utf-8 -*-
from importd import d

d(
    DEBUG=True,
    INSTALLED_APPS=(
        # external library
        'django_extensions',
        'django_jinja',
        'django_nose',

        # django rest framework
        'rest_framework',
        'rest_framework.authtoken',

        'sella',
        'demo',
    ),
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

    mounts={"demo": "/demo/"}
)

if __name__ == "__main__":
    d.main()


