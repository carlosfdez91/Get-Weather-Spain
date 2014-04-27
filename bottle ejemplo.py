from bottle import route, get, post, run, template, request

@get('/peticion')
def codigo_ciudad():
	return template('formulario.tpl')

#ciudad = raw_input('search')
#url = requests.get('http://xoap.weather.com/weather/search/search?',params = {'where':'%s' % ciudad})
#print url

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
	