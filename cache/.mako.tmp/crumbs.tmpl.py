# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427903191.206474
_enable_loop = True
_template_filename = u'/home/decause/.virtualenvs/decauseblog/lib/python2.7/site-packages/nikola/data/themes/base/templates/crumbs.tmpl'
_template_uri = u'crumbs.tmpl'
_source_encoding = 'utf-8'
_exports = ['bar']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bar(context,crumbs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n')
        if crumbs:
            __M_writer(u'<nav class="breadcrumbs">\n<ul class="breadcrumb">\n')
            for link, text in crumbs:
                if text != 'index.html':
                    if link == '#':
                        __M_writer(u'                <li>')
                        __M_writer(unicode(text))
                        __M_writer(u'</li>\n')
                    else:
                        __M_writer(u'                <li><a href="')
                        __M_writer(unicode(link))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a></li>\n')
            __M_writer(u'</ul>\n</nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 4, "33": 5, "34": 7, "35": 8, "36": 9, "37": 10, "38": 10, "39": 10, "40": 11, "41": 12, "42": 12, "43": 12, "44": 12, "45": 12, "46": 16, "15": 0, "20": 2, "21": 19, "52": 46, "27": 3, "31": 3}, "uri": "crumbs.tmpl", "filename": "/home/decause/.virtualenvs/decauseblog/lib/python2.7/site-packages/nikola/data/themes/base/templates/crumbs.tmpl"}
__M_END_METADATA
"""
