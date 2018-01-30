# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:11:32 2018

@author: Administrator
"""

def application(environ,start_response):
    start_response('200 OK',[(('Content-Type', 'text/html'))])
    return [b'<h1>hello </h1>']

from wsgiref.simple_server import make_server

httpd = make_server('192.168.1.19',8080,application)
print('Serving Http on port 8080')
httpd.serve_forever()