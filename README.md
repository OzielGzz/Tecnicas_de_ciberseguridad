# Herramientas de Ciberseguridad

_En la clase de Programacion para ciberseguridad se nos encargó un programa en el eque se utilicen cinco herramientas relacionadas con la ciberseguridad_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._



### Pre-requisitos 📋

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

### Instalación 🔧

_Descargar el Zip del repositorio_

```
https://github.com/OzielGzz/Tecnicas_de_ciberseguridad/archive/refs/heads/main.zip
```

## Ejecutando las pruebas ⚙️

_Abrir la ventana de comandos (Command Prompt) en windows o la terminal en Linux_
_Ejecutar_

```
python PIAmain.py -h
```
_Para ver información de uso del programa_

| Arg | Argumento | Descripción | Ejemplo |
| ------------- | ------------- | ------------- | ------------- |
|-h	| --help    |        	Muestra un mensaje de ayuda y sale del programa.	| PIAmain.py -h
  -t	|--tool     |  	Muestra un mensaje de ayuda y sale del programa.	|PIAmain.py -t Ps

## Eligiendo herramienta

Herramientas:	|Argumento|
| --------|-------|
Escaneo de Puertos|	Ps|
Analizar URLs|	Ua|
Envio de Emails o SMS|	EoS|
Metadatos de Imágenes	|Mta|
Cifrado de Texto	|Cif|

## Escaneo de Puertos
|Arg	|Argumento	|Descripción	|Ejemplo|
|-|-|-|-|
-ip	|--adress|	La IP que se desea escanear los puertos	|-ip “10.10.10.10” -p 8080                           
-p	|--port	|El puerto al que se comprobará el estado	|-p 8080       

## Analisis de URLs
Arg	|Argumento	|Descripción|	Ejemplo|
|-|-|-|-|
-K|	--Key|	Ingresa la Key de Virus Total|	-K **********
-U|	--Urls	|Archivo con ulrs sospechosas	|--Urls C:\urls_sospechosas.txt

## Envio de correos y SMS
Arg	|Argumento	|Descripción|	Ejemplo|
|-|-|-|-|
-EoS	|N/A	|Para elegir entre Email, SMS o Ambos	|•	-EoS email •	-EoS sms •	-EoS ambos|
-e	|--email	|Email origen	|--email tucorreo@gmail.com
-c	|--contra|	Contraseña del email origen	|--contra *******
-re	|--reciber	|El correo destino|	--reciber correodetuamigo@gmail.com
-a|	--asunto	|El asunto del correo	|--asunto “IMPORTANTE!” _Dato: Entre comillas en caso de que sea más de una palabra_
-b	|--body|	El cuerpo del correo	|--body “Hola, buenas tardes” _Dato: Entre comillas en caso de que sea más de una palabra_
-f	|--file|	Especificar la ruta del archivo a adjuntar |_Dato: Este argumento es opcional	-f C:\foto.jpg_
-SID|	N/A|	Ingresar nuestro SID de Twilio	|-SID *******
-to|	N/A	|Ingresar nuestra Token de Twilio	|-to *******
-n|	--number|	Número de Twilio	|-n +818181818181
-d	| N/A|	El número del destinatario (Agregar +52)	|-d +528181818181
-m|	--msj	|Ingresar el mensaje a enviar	|--msj “Hola, buenas tardes” _Dato: Entre comillas en caso de que sea más de una palabra_

## Metadatos
Arg	|Argumento	|Descripción|	Ejemplo|
|-|-|-|-|
-r|	--ruta|	Ruta de la imagen JPG a analizar	|--ruta C:\imagen.jpg

## Cifrado y Descifrado
Arg	|Argumento	|Descripción|	Ejemplo|
|-|-|-|-|
-M	|--msje|	Texto que queremos cifrar|	--msje “Quiero cifrar este mensaje”
-k	|--key	|Llave que necesitaremos para descifrar el mensaje|	--key “Contraseña”
-A|	--accion |	Para seleccionar si queremos cifrar o descifrar el texto Opciones:  c = Cifrar  d = Descifrar	•	-A c | -A d

## EJEMPLOS COMPLETOS
Herramienta |	Ejemplo|
|-|-|
Escaneo de puertos:|	PIAmain.py -t Ps -ip '192.168.15.1' -p 22 80
Analizar URLs|	PIAmain.py -t Ua -K (Tu key de VirusTotal) -U urls_sospechosas.txt
Emails	|PIAmain.py -t EoS -EoS email -e (nuestro correo) -co (contraseña) -re (correo de quien recibe) -a "aqui va el asunto" -b "mensaje"
SMS	|PIAmain.py -t EoS -EoS sms -SID "Nuestro SID" -to "Nuestro token" -n "nuestro numero de Twilio" -d +52numero destino -m "mensaje"
Cifrado	|PIAmain.py -t Cif -m 'este es mi mensaje' -k millave -A c
Metadatos|	PIAmain.py -r C:\foto.jpg


## Construido con 🛠️

_Python_
_Powershell_
_Bash_

* [Python](https://www.python.org/downloads/) - Enlace de descarga última versión de Python
* [Powershell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2) - Información acerca de Powershell
* [Bash](https://es.wikipedia.org/wiki/Bash) - Información acerca de Bash


## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Jesus Dorado** - *Metadatos* - [DoradoMX](https://github.com/DoradoMx)
* **Jorge Rodriguez** - *Escaneo de puertos* - [Jorgestudent](https://github.com/Jorgestudent)
* **Oziel Gonzalez** - *Analisis de Páginas* - [OzielGzz](https://github.com/OzielGzz)
* **Sebastian Hernandez** - *Envio de Correos y SMS's* - [Sebas17900](https://github.com/Sebas17900)
* **Julian Torres** - *Cifrado de mensajes* - [juliantorres00](https://github.com/juliantorres00)


## Expresiones de Gratitud 🎁

* Queremos agradecer al profe Osvaldo Gonzalez por la clase impartida 📢
* Los invitamos a una carnita asada finalizando el semestre 🍺. 

---

