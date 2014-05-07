from bottle import route, get, post, run, template, request
from busqueda import busqueda1

@route('/')
def index():
    return template('inicio.tpl')

@get('/busqueda')
def entrada():
    return template('busqueda.tpl')

@post('/resultado')
def resultado():
	return busqueda1('resultado.tpl')

import os
from bottle import TEMPLATE_PATH

ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

if ON_OPENSHIFT:
    TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
                                      'runtime/repo/wsgi/views/'))
    
    application=default_app()
else:
	run(host='localhost', port=8080)
	
