#coding: utf-8
import requests
from lxml import etree

yweatherns = "{http://xml.weather.yahoo.com/ns/rss/1.0}"

#localidad = raw_input('¿De que ciudad quieres el tiempo? ')

#url = requests.get('http://xoap.weather.com/weather/search/search?'
#	,params = {'where':'%s' % localidad})

#raiz = etree.fromstring(url.text.encode("utf-8"))
#loc = raiz.find("loc")
#ciudad = loc.attrib["id"]
ciudad = ('SPXX0081')

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
humedad = raiz2.find('channel/%satmosphere' % yweatherns).attrib["humidity"]


print "Lugar de la consulta: %s " % tiempode
print "Fecha y hora de la consulta: %s" % fechayhora
print "Temperatura actual: %s %s" % (tempactual,grados)
print "Viento: Sensacion %s %s Direccion %s %s Velocidad %s %s" % (sensacion,
	grados,direccion,km,velocidad,speed)
print "Caracteristicas atmosfericas: Humedad %s " % (humedad)

