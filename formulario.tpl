<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Get Weather</title>
	</head>
	<body>
		<div id="centrar">
		<a name="Inicio"></a>
		<h1>Get Weather!</h1>
		<form action="/peticion" method="POST">  
	    <br/><p>Introduce el nombre de la localidad de la cual quieres obtener su informacion metereológica.</p>
	    <input type="str" name="nombre" value=""/>
	    <br/>
	     <br>
	      <input type='submit' value='Buscar'/>
	    </form>
	</body>
</html>