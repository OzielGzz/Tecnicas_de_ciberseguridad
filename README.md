# Herramientas de Ciberseguridad

_En la clase de Programacion para ciberseguridad se nos encarg贸 un programa en el eque se utilicen cinco herramientas relacionadas con la ciberseguridad_

## Comenzando 馃殌

_Estas instrucciones te permitir谩n obtener una copia del proyecto en funcionamiento en tu m谩quina local para prop贸sitos de desarrollo y pruebas._



### Pre-requisitos 馃搵

_Que cosas necesitas para instalar el software y como instalarlas_
_virustotal-api_
_openpyxl_
_pillow_
_twilio_

```
pip install virustotal-api
pip install openpyxl
pip install pillow
pip install twilio
```

### Instalaci贸n 馃敡

_Descargar el Zip del repositorio_

```
https://github.com/OzielGzz/Tecnicas_de_ciberseguridad/archive/refs/heads/main.zip
```

## Ejecutando las pruebas 鈿欙笍

_Abrir la ventana de comandos (Command Prompt) en windows o la terminal en Linux_
_Ejecutar_

```
python PIAmain.py -h
```
_Para ver informaci贸n de uso del programa_

| Arg | Argumento | Descripci贸n | Ejemplo |
| ------------- | ------------- | ------------- | ------------- |
|-h	| --help    |        	Muestra un mensaje de ayuda y sale del programa.	| PIAmain.py -h
  -t	|--tool     |  	Muestra un mensaje de ayuda y sale del programa.	|PIAmain.py -t Ps

## Eligiendo herramienta

Herramientas:	|Argumento|
| --------|-------|
Escaneo de Puertos|	Ps|
Analizar URLs|	Ua|
Envio de Emails o SMS|	EoS|
Metadatos de Im谩genes	|Mta|
Cifrado de Texto	|Cif|

## Escaneo de Puertos
|Arg	|Argumento	|Descripci贸n	|Ejemplo|
|-|-|-|-|
-ip	|--adress|	La IP que se desea escanear los puertos	|-ip 鈥?10.10.10.10鈥? -p 8080                           
-p	|--port	|El puerto al que se comprobar谩 el estado	|-p 8080       

## Analisis de URLs
Arg	|Argumento	|Descripci贸n|	Ejemplo|
|-|-|-|-|
-K|	--Key|	Ingresa la Key de Virus Total|	-K **********
-U|	--Urls	|Archivo con ulrs sospechosas	|--Urls C:\urls_sospechosas.txt

## Envio de correos y SMS
Arg	|Argumento	|Descripci贸n|	Ejemplo|
|-|-|-|-|
|-EoS	|N/A	|Para elegir entre Email, SMS o Ambos	|鈥?	-EoS email 鈥?	-EoS sms 鈥?	-EoS ambos|
|-e	|--email	|Email origen	|--email tucorreo@gmail.com
|-c	|--contra|	Contrase帽a del email origen	|--contra *******
|-re	|--reciber	|El correo destino|	--reciber correodetuamigo@gmail.com
|-a|	--asunto	|El asunto del correo	|--asunto 鈥淚MPORTANTE!鈥? _Dato: Entre comillas en caso de que sea m谩s de una palabra_
|-b	|--body|	El cuerpo del correo	|--body 鈥淗ola, buenas tardes鈥? _Dato: Entre comillas en caso de que sea m谩s de una palabra_
|-f	|--file|	Especificar la ruta del archivo a adjuntar |_Dato: Este argumento es opcional	-f C:\foto.jpg_
|-SID |	N/A|	Ingresar nuestro SID de Twilio	|-SID *******
|-to |	N/A	|Ingresar nuestra Token de Twilio	|-to *******
|-n |	--number|	N煤mero de Twilio	|-n +818181818181
|-d | N/A|	El n煤mero del destinatario (Agregar +52)	|-d +528181818181
|-m |	--msj	|Ingresar el mensaje a enviar	|--msj 鈥淗ola, buenas tardes鈥? _Dato: Entre comillas en caso de que sea m谩s de una palabra_

## Metadatos
Arg	|Argumento	|Descripci贸n|	Ejemplo|
|-|-|-|-|
-r|	--ruta|	Ruta de la imagen JPG a analizar	|--ruta C:\imagen.jpg

## Cifrado y Descifrado
Arg	|Argumento	|Descripci贸n|	Ejemplo|
|-|-|-|-|
-M	|--msje|	Texto que queremos cifrar|	--msje 鈥淨uiero cifrar este mensaje鈥?
-k	|--key	|Llave que necesitaremos para descifrar el mensaje|	--key 鈥淐ontrase帽a鈥?
-A|	--accion |	Para seleccionar si queremos cifrar o descifrar el texto Opciones:  c = Cifrar  d = Descifrar	鈥?	-A c | -A d

## EJEMPLOS COMPLETOS
Herramienta |	Ejemplo|
|-|-|
Escaneo de puertos:|	PIAmain.py -t Ps -ip '192.168.15.1' -p 22 80
Analizar URLs|	PIAmain.py -t Ua -K (Tu key de VirusTotal) -U urls_sospechosas.txt
Emails	|PIAmain.py -t EoS -EoS email -e (nuestro correo) -co (contrase帽a) -re (correo de quien recibe) -a "aqui va el asunto" -b "mensaje"
SMS	|PIAmain.py -t EoS -EoS sms -SID "Nuestro SID" -to "Nuestro token" -n "nuestro numero de Twilio" -d +52numero destino -m "mensaje"
Cifrado	|PIAmain.py -t Cif -m 'este es mi mensaje' -k millave -A c
Metadatos|	PIAmain.py -r C:\foto.jpg


## Construido con 馃洜锔?

_Python_
_Powershell_
_Bash_

* [Python](https://www.python.org/downloads/) - Enlace de descarga 煤ltima versi贸n de Python
* [Powershell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2) - Informaci贸n acerca de Powershell
* [Bash](https://es.wikipedia.org/wiki/Bash) - Informaci贸n acerca de Bash


## Autores 鉁掞笍

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Jesus Dorado** - *Metadatos* - [DoradoMX](https://github.com/DoradoMx)
* **Jorge Rodriguez** - *Escaneo de puertos* - [Jorgestudent](https://github.com/Jorgestudent)
* **Oziel Gonzalez** - *Analisis de P谩ginas* - [OzielGzz](https://github.com/OzielGzz)
* **Sebastian Hernandez** - *Envio de Correos y SMS's* - [Sebas17900](https://github.com/Sebas17900)
* **Julian Torres** - *Cifrado de mensajes* - [juliantorres00](https://github.com/juliantorres00)


## Expresiones de Gratitud 馃巵

* Queremos agradecer al profe Osvaldo Gonzalez por la clase impartida 馃摙
* Los invitamos a una carnita asada finalizando el semestre 馃嵑. 

---

