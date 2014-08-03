#-*- coding: utf-8 -*-

from importd import d

@d('/', name='demo.index')
def demo_index(request):
    return d.render_to_response('demo/index.jinja2')

@d('/filters/jinja2', name='demo.filters_jinja2')
def filters_jinja2(request):
    return d.render_to_response('demo/filter_jinja.jinja2')

@d('/param/<int:foo>/<slug:bar>', name='demo.param_url')
def param_url(request, foo, bar):
    return {'foo': int(foo), 'bar': int(bar)}

