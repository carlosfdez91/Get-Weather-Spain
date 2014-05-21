<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC '-// W3C // DTD XHTML 1.0 Strict //EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="es">
	<head>
		<title>Get Weather!</title >
	</head>
		<body>
			<h1>Prevision Metereologica</h1>
			<h2>Localidad: {{datos.tiempode}}</h2>
				<ul>
					<li>Lugar de la consulta: {{tiempode}}</li>
					<li>Fecha y hora de la actualización de datos: {{fechayhora}}</li>
					<li>Temperatura actual: {{tempactual}} {{grados}}, Condición actual: {{reemplazar}}</li>
					<li>Viento: Sensación térmica {{sensacion}} {{grados}}, Dirección {{direccion}}, Velocidad {{velocidad}} {{speed}}</li>
					<li>Atmosfera: Humedad {{humedad}} por ciento, Visibilidad {{vision}} {{km}}, Presión {{presion}} {{press}}</li>
					<li>Astronomía: Amanecer: {{sol}}, Ocaso: {{puesta}}</li>
				</ul>
		</body>
</html>
