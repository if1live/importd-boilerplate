#-*- coding: utf-8 -*-

from importd import d

@d('/')
def index(request):
    return d.render_to_response('index.jinja2')

