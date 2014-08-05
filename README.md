# importd-boilerplate

[![Build Status](https://travis-ci.org/if1live/importd-boilerplate.svg?branch=master)](https://travis-ci.org/if1live/importd-boilerplate)

[importd](https://github.com/amitu/importd) is django based mini framework inspired from sinatra. Fully compatible with django. This repository is boilerplate code for importd.

## Feature

* [HTML5 Boilerplate](http://html5boilerplate.com/) 4.3.0
* [Jinja2](http://jinja.pocoo.org/docs/) support
* [Django Debug Toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar) support
* [Django REST framework](http://www.django-rest-framework.org/) support


## Install
```bash
pip install -r requirements.txt
python sella/app.py syncdb
python sella/app.py runserver_plus
```

## Unit Test
```bash
python sella/app.py test --exe sella demo api
```

## Sample URL
* http://127.0.0.1:8000/ : Jinja2 sample
* http://127.0.0.1:8000/demo/filters/jinja2 : jinja2 filter sample
* http://127.0.0.1:8000/api/v1/users/1 : django rest framework sample
 
