from bottle import route, get, post, run, template, request, static_file, default_app
from busqueda import buscar
import os

# @route('/')
# def index():
#     return template('inicio.tpl')

@route('/')
def entrada():
    return template("busqueda.html")

@route('/static/images/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/images/')

@route('/static/css/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/css/')

@post('/resultado')
def busqueda():
    text = request.forms.get('text')
    if text == "":
        return template ("campo_vacio.html")
    else:
        prevision = buscar(text)
        return template("resultado.html",datos=prevision)

# @post('/resultado')
# def vacio():
#     nulo = buscar(text)
#     return template("campo_vacio.html")    

import os
from bottle import TEMPLATE_PATH

ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

if ON_OPENSHIFT:
    TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
                                      'app-root/repo/wsgi/views/'))
    application=default_app()
else:
    run(host='localhost', port=8080)