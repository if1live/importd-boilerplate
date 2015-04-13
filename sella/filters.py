#-*- coding: utf-8 -*-

from django_jinja import library
import jinja2
import json

@library.filter
@jinja2.contextfilter
def tojson(ctx, val):
    return json.dumps(val)
