#coding: utf-8
import os
import requests
from lxml import etree

yweatherns = "{http://xml.weather.yahoo.com/ns/rss/1.0}"

def orientacion(direccion):
	"""Función que calcula la dirección de la que procede el viento"""
	for grados in str(direccion):
		if direccion >= 337 and direccion < 22.5:
			return 'N'
		elif direccion >= 22.5 and direccion < 67.5:
			return 'NE'
		elif direccion >= 67.5 and direccion < 112.5:
			return 'E'
		elif direccion >= 112.5 and direccion < 157.5:
			return 'SE'
		elif direccion >= 157.5 and direccion < 202.5:
			return 'S'
		elif direccion >= 202.5 and direccion < 247.5:
			return 'SO'
		elif direccion >= 247.5 and direccion < 292.5:
			return 'O'
		elif direccion >= 292.5 and direccion < 337.5:
			return 'NO'

localidad = raw_input('¿De que ciudad quieres el tiempo? ')

espacio = localidad.replace(" ","-")

url = requests.get('http://xoap.weather.com/weather/search/search?'
	,params = {'where':'%s' % espacio})

raiz = etree.fromstring(url.text.encode("utf-8"))
loc = raiz.find("loc")
ciudad = loc.attrib["id"]
#ciudad = ('SPXX0081')

valores = {'p': '%s' % ciudad,'u':'c'}
tiempo = requests.get('http://weather.yahooapis.com/forecastrss?',
	params = valores)

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
reemplazar = cielo.replace("44"
	,"Nublado").replace("26","Nublado").replace("32",
	"Soleado").replace("33","Noche").replace("27",
	"Mayormente Nublado").replace("11","Lluvia").replace("31",
	"Despejado").replace("34","Día").replace("28",
	"Mayormente Nublado").replace("29",
	"Parcialmente Nublado").replace("30",
	"Parcialmente Nublado")
direcc = orientacion(direccion)

os.system ('clear')
print "-Lugar de la consulta: %s " % tiempode
print "-Fecha y hora de la actualización de datos: %s" % fechayhora
print "-Temperatura actual: %s %s, Cielo: %s" % (tempactual,grados,reemplazar)
print "-Viento: Sensación térmica %s %s, Dirección %s, Velocidad %s %s" % (
	sensacion,grados,direcc,velocidad,speed)
print "-Atmosfera: Humedad %s por ciento, Visibilidad %s %s, Presión %s %s" % (
	humedad,vision,km,presion,press)
print "-Astronomía: Amanecer: %s, Ocaso: %s" % (sol,puesta)

