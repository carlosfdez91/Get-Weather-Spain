import bottle
import get
import post
import run
import template
import request

@get('/')
def obtener():
	return template('formulario.tpl')

@post('/peticion')
def mostrar():
		texto = request.forms.get('search')
		return '<p>%s</p>' % texto

run(host='localhost', port=8080, debug=True)