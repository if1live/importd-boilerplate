#-*- coding: utf-8 -*-

from importd import d

@d('/')
def index(request):
    return d.render_to_response('index.jinja2')

@d('/restful-api/')
def view_restful_api(request):
    return d.render_to_response('restful_api.jinja2')
