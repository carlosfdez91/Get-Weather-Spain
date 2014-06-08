#coding: utf-8
def buscar(text):
	import os
	import requests
	from lxml import etree

	yweatherns = "{http://xml.weather.yahoo.com/ns/rss/1.0}"

	nombre = text.lower()
	nombresin = nombre.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n");

	codigos = open('codigos.txt','r')
	
	encontrado = False
	
	for linea in codigos:
		if nombresin == linea.split(",")[0]:
			ciudad = linea.split(",")[1]
			encontrado = True
			break

	if encontrado <> True:
		espacio = nombresin.replace(" ","-")
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
	reemplazar = cielo.replace("10"
		,"Lluvia congelada").replace("11"
		,"Lluvia").replace("12"
		,"Lluvia").replace("13"
		,"Rafagas de Nieve").replace("14"
		,"Nevada ligera").replace("15"
		,"Nieve con viento").replace("16"
		,"Nieve").replace("17"
		,"Granizo").replace("18"
		,"Aguanieve").replace("19"
		,"Polvo").replace("20"
		,"Neblina").replace("21"
		,"Niebla ligera").replace("22"
		,"Bruma").replace("23"
		,"Vendaval").replace("24"
		,"Con viento").replace("25"
		,"Helado").replace("26"
		,"Nublado").replace("27"
		,"Muy nublado (noche)").replace("28"
		,"Muy nublado (dia)").replace("29"
		,"Parcialmente nublado (noche)").replace("30"
		,"Parcialmente nublado (dia)").replace("31"
		,"Despejado (noche)").replace("32"
		,"Soleado").replace("33"
		,"Despejado (noche)").replace("34"
		,"Despejado (dia)").replace("35"
		,"Lluvia y Granizo").replace("36"
		,"Caluroso").replace("37"
		,"Tormentas electricas aisladas").replace("38"
		,"Tormentas electricas dispersas").replace("39"
		,"Tormentas electricas dispersas").replace("40"
		,"Lluvia dispersa").replace("41"
		,"Nieve densa").replace("42"
		,"Nieve y lluvia dispersas").replace("43"
		,"Nieve densa").replace("44"
		,"Parcialmente nublado").replace("45"
		,"Tormentas electricas").replace("46"
		,"Nieve").replace("47"
		,"Tormentas electricas aisladas").replace("3200"
		,"No disponible");

	
	prevision = {
	'ciudad':ciudad,
	'tiempo.text':tiempo.url,
	'ciudad':ciudad,
	'tiempode':tiempode,
	'fechayhora':fechayhora,
	'tempactual':tempactual,
	'grados':grados,
	'sensacion':sensacion,
	'direccion':direccion,
	'velocidad':velocidad,
	'speed':speed,
	'humedad':humedad,
	'vision':vision,
	'km':km,
	'presion':presion,
	'press':press,
	'sol':sol,
	'puesta':puesta,
	'cielo':cielo,
	'reemplazar':reemplazar,
	'cielo':cielo,
	'city':city}

	return prevision