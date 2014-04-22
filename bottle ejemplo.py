from bottle import route, get, post, run, template, request, 

@get('/')
def codigo_ciudad():
	url = requests.get('http://xoap.weather.com/weather/search/search?'
	,params = {'where':'%s' % espacio})
	return template('formulario.tpl')

@post('/peticion')
def mostrar():
		texto = request.forms.get('search')
		return '<p>%s</p>' % texto

run(host='localhost', port=8080, debug=True)