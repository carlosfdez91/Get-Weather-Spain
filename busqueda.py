def busqueda1():
	import os
	import requests
	from lxml import etree
	from bottle import request, template

	entrada = request.forms.get('entrada')
	yweatherns = "{http://xml.weather.yahoo.com/ns/rss/1.0}"
	localidad = entrada

	espacio = localidad.replace(" ","-").replace("sevilla","seville").replace(
		"Sevilla","Seville")

	url = requests.get('http://xoap.weather.com/weather/search/search?'
		,params = {'where':'%s' % espacio})

	raiz = etree.fromstring(url.text.encode("utf-8"))
	loc = raiz.find("loc")
	ciudad = loc.attrib["id"]

	valores = {'p': '%s' % ciudad,'u':'c'}
	tiempo = requests.get('http://weather.yahooapis.com/forecastrss?'
		,params = valores)

	raiz2 = etree.fromstring(tiempo.text.encode("utf-8"))
	tiempode = raiz2.find('channel/description').text
	fechayhora = raiz2.find('channel/lastBuildDate').text
	city = raiz2.find('channel/%slocation' % yweatherns).attrib["city"]
	condiciones = raiz2.find('channel/item/title').text
	tempactual = raiz2.find('channel/item/%scondition' % yweatherns).attrib["temp"]
	grados = raiz2.find('channel/%sunits' % yweatherns).attrib["temperature"]
	sensacion = raiz2.find('channel/%swind' % yweatherns).attrib["chill"]
	direccion = raiz2.find('channel/%swind' % yweatherns).attrib["direction"]
	velocidad = raiz2.find('channel/%swind' % yweatherns).attrib["speed"]
	km = raiz2.find('channel/%sunits' % yweatherns).attrib["distance"]
	speed = raiz2.find('channel/%sunits' % yweatherns).attrib["speed"]
	press = raiz2.find('channel/%sunits' % yweatherns).attrib["pressure"]
	humedad = raiz2.find('channel/%satmosphere' % yweatherns).attrib["humidity"]
	vision = raiz2.find('channel/%satmosphere' % yweatherns).attrib["visibility"]
	presion = raiz2.find('channel/%satmosphere' % yweatherns).attrib["pressure"]
	sol = raiz2.find('channel/%sastronomy' % yweatherns).attrib["sunrise"]
	puesta = raiz2.find('channel/%sastronomy' % yweatherns).attrib["sunset"]
	cielo = raiz2.find('channel/item/%scondition' % yweatherns).attrib["code"]
	reemplazar = cielo.replace("44","Nublado").replace("26",
		"Nublado").replace("32","Soleado").replace("33",
		"Noche").replace("27","Mayormente Nublado").replace("11",
		"Lluvia").replace("12","Chubascos").replace("31",
		"Despejado").replace("34","Dia").replace("28","Mayormente Nublado"
		).replace("29","Parcialmente Nublado").replace("30","Parcialmente Nublado")

	return template('resultado.tpl',tiempode=tiempode,fechayhora=fechayhora,tempactual=tempactual,grados=grados,
		reemplazar=reemplazar,sensacion=sensacion,grados=grados,direccion=direccion,velocidad=velocidad,
		speed=speed,humedad=humedad,vision=vision,km=km,presion=presion,press=press,sol=sol,puesta=puesta)