#coding: utf-8
import requests
import webbrowser
from lxml import etree

#localidad = raw_input('¿De que ciudad quieres el tiempo? ')

#url = requests.get('http://xoap.weather.com/weather/search/search?'
#	,params = {'where':'%s' % localidad})

#raiz = etree.fromstring(url.text.encode("utf-8"))
#loc = raiz.find("loc")
#ciudad = loc.attrib["id"]
ciudad = ('SPXX0081')

valores = {'p': '%s' % ciudad,'&u':'c'}
tiempo = requests.get('http://weather.yahooapis.com/forecastrss?'
	,params = valores)

raiz2 = etree.fromstring(tiempo.text.encode("utf-8"))
tiempode = raiz2[0][2].text
fechayhora = raiz2[0][4].text
local = raiz2[0][6].attrib


print "Lugar de la consulta: %s " % tiempode
print "Fecha y hora de la consulta: %s" % fechayhora
print local
