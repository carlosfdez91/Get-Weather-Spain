#coding: utf-8
import os
import requests
from lxml import etree

yweatherns = "{http://xml.weather.yahoo.com/ns/rss/1.0}"

lista_direccion = []

def orientacion(direccion):
	"""Función que calcula la dirección de la que procede el viento"""
	if direccion == 0 or direccion == 360:
		return 'Norte'
	elif direccion > 0 and direccion < 90:
		return 'Noreste'
	if direccion == 90:
		return 'Este'
	elif direccion > 90 and direccion < 180:
		return 'Sureste'
	if direccion == 180:
		return 'Sur'
	elif direccion > 180 and direccion < 270: 
		return 'Suroeste'
	if direccion == 270:
		return 'Oeste'
	elif direccion > 270 and direccion < 360:
		return 'Noroeste'
	

localidad = raw_input('¿De que ciudad quieres el tiempo? ')

espacio = localidad.replace(" ","-").replace("sevilla","seville").replace(
	"Sevilla","Seville")

url = requests.get('http://xoap.weather.com/weather/search/search?'
	,params = {'where':'%s' % espacio})

raiz = etree.fromstring(url.text.encode("utf-8"))
loc = raiz.find("loc")
ciudad = loc.attrib["id"]
#ciudad = ('SPXX0081')

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
#direccion = str(20)
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
	,"Nublado").replace("26","Nublado").replace("32"
	,"Soleado").replace("33","Noche").replace("27"
	,"Mayormente Nublado").replace("11","Lluvia").replace("12"
	,"Chubascos").replace("31","Despejado").replace("34"
	,"Día").replace("28","Mayormente Nublado").replace("29"
	,"Parcialmente Nublado").replace("30","Parcialmente Nublado")

direcc = orientacion(direccion)
lista_direccion.append(direcc)

os.system ('clear')
print "-Lugar de la consulta: %s " % tiempode
print "-Fecha y hora de la actualización de datos: %s" % fechayhora
print "-Temperatura actual: %s %s, Condición actual: %s" % (tempactual
	,grados,reemplazar)
print "-Viento: Sensación térmica %s %s, Dirección %s, Velocidad %s %s" % (
	sensacion,grados,lista_direccion,velocidad,speed)
print "-Atmosfera: Humedad %s por ciento, Visibilidad %s %s, Presión %s %s" % (
	humedad,vision,km,presion,press)
print "-Astronomía: Amanecer: %s, Ocaso: %s" % (sol,puesta)
print direccion

