#!/usr/bin/env python3

import logging
import sys
import subprocess
import argparse
import configparser
import PIAportscan as portscan
import PIAanalyzer as analyzer
import PIAmetadatos as metadata
import PIAEmailSMS as emailsms
import PIACifrado as cifrado

# Creamos el logger, establecemos niveles, archivo donde se guardara, y formato
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
filehandler = logging.FileHandler('PIAmain.log')
formatter = logging.Formatter( "%(asctime)s: %(levelname)s - %(message)s")
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

# Tools: una lista con nombre abreviado de las herrameintas
tools = ['Ps','Ua','EoS', 'Mta', 'Cif']

# Descripción del Parser
parser = argparse.ArgumentParser(description='''The PIA framework is a set of tools used for security purposes,
        consists of a portscaner, urlanalyzer, emails and sms sender,etc''',
        formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog = '''
        ejemplos:

        PIAmain -t Ps -ip '192.168.15.1' -p 22 80 \n
        PIAmain -t Ua -K (Tu key de VirusTotal) -U urls_sospechosas.txt \n
        PIAmain -t EoS -EoS email -e (nuestro correo) -co (contraseña) -re (correo de quien recibe) -a "aqui va el asunto" -b "mensaje"\n
        PIAmain -t EoS -EoS sms -SID "Nuestro SID" -to "Nuestro token" -n "nuestro numero de Twilio" -d +52numero destino -m "mensaje"\n
        PIAmain -t Cif -m 'este es mi mensaje' -k millave -A c
        ''')

# Choices=tools Significa que solo acepta como valores elementos de la lista: tools
parser.add_argument('-t', '--tool', type=str, metavar='Ps', choices=tools, 
                    help="select a tool: portscaner= Ps, UrlAnalyzer= Ua, Emails or SMS= EoS, Metadata from Images= Mta, cifrado= Cif", 
                    required=True)

# Argumentos de PortScaner
Ps = parser.add_argument_group('PortScaner')
Ps.add_argument('-ip', '--address', type=str, metavar='10.10.10.10',help='una direccion ipv4 ' )
Ps.add_argument('-p', '--port', type=int, metavar='22 80 443',nargs='*',choices=range(0,65534),help='no poner []')

# Argumentos de UrlAnalyzaer
Ua = parser.add_argument_group('UrlAnalyzer')
Ua.add_argument('-K', '--Key', type=str, metavar='API Key', help="Ingresa tu Key de Virus Total")
Ua.add_argument('-U', '--Urls', type=str, metavar='archive', help="Archivo con ulrs sospechosas")

# Creamos el grupo EoS y agregamos los argumentos de correos o SMS a ese grupo
EoS = parser.add_argument_group('Emails and SMS')
EoS.add_argument('-EoS', type=str,metavar='email',
                 help='Escribir que deseamos enviar: email, sms, ambos')

# Parametros para Email:
EoS.add_argument('-e', '--email', type= str, metavar='sndrmail', help="Ingresar nuestro correo")
EoS.add_argument('-co', '--contra', type= str, metavar='pass', help="Ingresar nuestra contraseña")
EoS.add_argument('-re', '--receiver', type= str, metavar='recvmail',help="Correo de quien recibira el email")
EoS.add_argument('-a', '--asunto', type= str, metavar='asunto', help="Ingresar el asunto del correo")
EoS.add_argument('-b', '--body', type= str, metavar='body', help="Ingresar el cuerpo del correo")
EoS.add_argument('-f', '--file', default= 'no', metavar='/ruta', help="Especificar la ruta del archivo a adjuntar")

# Parametros para SMS
EoS.add_argument('-SID', type = str, metavar='SID', help="Ingresar nuestro SID de Twilio")
EoS.add_argument('-to', type = str,  metavar='token', help="Ingresar nuestra Token de Twilio")
EoS.add_argument('-n','--number', type = str, metavar='twilio num', help="Ingresar nuestro numero de Twilio")
EoS.add_argument('-d', type = str, metavar='dest#', help="Ingresar el numero del destinatario(Agregar +52)")
EoS.add_argument('-m', '--msj', type = str, metavar='msje', help="Ingresar el mensaje a enviar")
EoS.add_argument('-c', '--config', type=argparse.FileType('r'), metavar='config file', help='config file')

# Parametros para Metadatos
Meta = parser.add_argument_group("Metadatos de Imagen JPG")
Meta.add_argument('-r', '--ruta', type = str, metavar='/ruta', help="La ruta especifica de la imagen a analizar")

# Parametros para Cifrado
cif = parser.add_argument_group("Cifrado y descifrado")
cif.add_argument('-M', '--msje',type=str, metavar='msje', help='mensaje a cifrar')
cif.add_argument('-k', '--key', type=str, metavar='llave', help='Llave para cifrar')
cif.add_argument('-A', '--accion', type=str, metavar='d',choices=['d', 'e'],  help='cifrar= c , descifrar= d')
args = parser.parse_args()

if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        args.email = config['EMAIL']['email']
        args.contra = config['EMAIL']['contra']
        args.receiver = config['EMAIL']['receiver']
        args.asunto = config['EMAIL']['asunto']
        args.body = config['EMAIL']['body']
        args.file = config['EMAIL']['file']
        args.SID = config['SMS']['SID']
        args.token = config['SMS']['to']
        args.number = config['SMS']['number']
        args.numdest = config['SMS']['d']
        args.msj = config['SMS']['msj']


#Funcion tools, actualmente esta funcion no cumple ninguna funcion en el script.
def tools():
    print ('PortScaner, the simple but powerfull port scannng tool')
    print ('UrlAnalyzer, a tool to analyze urls with VirusTotal')
    print ('opcion3 is the simple but powerfull opcion3')
    print ('opcion4 is the simple but powerfull opcion4')
    print ('opcion5 is the simple but powerfull opcion5')


#Pybanner: imprime el banner: 'PIA' en caso de que el script de PowerShell o Bash fallen
def Pybanner():
    print ('#'*60,'\n\n')
    print (' '*10,'#*'*5,' '*7,'#*'*2,' '*12,'#*'*2)
    print (' '*10,'#*'*2, ' '*2,'#*'*2,' '*5,'#*'*2,' '*10, '#*'*4)
    print (' '*10,'*#'*2, ' '*2,'*#'*2,' '*5,'*#'*2,' '*9, '*#'*2,' '*0,'*#'*2)
    print (' '*10,'*#'*2, ' '*2,'*#'*2,' '*5,'*#'*2,' '*8, '*#'*2,' '*2,'*#'*2)
    print (' '*10,'*#'*2, ' '*1,'*#'*2,' '*6,'*#'*2,' '*7, '*#'*2,' '*4,'*#'*2)
    print (' '*10,'*#'*4, ' '*9,'*#'*2,' '*6,'*#'*2,' '*6, '*#'*2)
    print (' '*10,'*#'*3, ' '*11,'*#'*2,' '*5,'*#'*9)
    print (' '*10,'*#'*3, ' '*11,'*#'*2,' '*4,'*#'*2,' '*10, '*#'*2,)
    print (' '*10,'*#'*3, ' '*11,'*#'*2,' '*3,'*#'*2,' '*12, '*#'*2,)
    print ('\n\n','#'*60)


#imprime el banner: 'PIA', utliza el modulo sys para determinar si usar PowerShell o Bash
def banner():
    OS = sys.platform
    if OS == 'linux' or OS == 'darwin':
        logger.info("Sistema UNIX-LIKE")
        try:
             subprocess.run("./BASHbanner")
        except:
            logger.info("ERROR al ejecutar BASHbanner, usando Pybanner")
            Pybanner()
    elif OS == 'win32':
        logger.info("Sistema Windows detectado")
        try:
            subprocess.run("./PSbanner")
        except:
            logger.info("ERROR al ejecutar PSbanner, usando Pybanner")
            Pybanner()
    else:
        logger.info("No se pudo determinar OS")
        Pybanner()


def main():
    logger.info ('running main')
    # Ejecutando el portscanner
    if args.tool == 'Ps':
        logger.info ('portscaner seleccionado')
        print ("Ps seleccionado")
        banner()
        try:
            portscan.portscan(args.address, args.port)
        except:
            logger.info ("ERROR al ejecutar portscan.portScan")
            print ("ERROR, ip deber ser tipo str y port tipo int, ej: -ip '10.10.10.10' -p 22 80 443 ")

    # Fin de Portscanner
    elif args.tool == 'Mta':
        logger.info('ejecutando metadatos')
        print ("Metadatos seleccionado")
        try:
            if args.ruta == None:
                metadata.Metadatos()
            else: 
                metadata.mta_ruta(args.ruta)
        except:
            logger.info("ERROR al ejecutar mta()")

    elif args.tool == 'EoS':
        logger.info("Emails y mensajes seleccionado")
        print ('EoS Selected')
        if args.EoS == 'email':
            try:
                 emailsms.send_emailP(args.email,args.contra,args.receiver,args.asunto,args.body,args.file)
            except:
                logging.info("ERROR al ejecutar emails.send_emailP")
        elif args.EoS == 'sms':
            try:
                 emailsms.send_smsP(args.SID,args.to,args.number,args.d,args.msj)
            except:
                logging.info("emailsms.send_smsP")

        elif args.EoS == 'ambos':
            try:
                 emailsms.send_emailP(args.email,args.contra,args.receiver,args.asunto,args.body,args.file)
                 emailsms.send_smsP(args.SID,args.to,args.number,args.d,args.msj)
            except:
                logging.info("ERROR al ejecutar emailsms.send_emailP , email.send_smsP")
            
    elif args.tool == 'Ua':
        logging.info("Ua seleccionado")
        print ("")
        print ('Ua selected')
        print ("")
        banner()
        print ("")
        try:
             analyzer.inicio(args.Key, args.Urls)
        except:
            logger.info("ERROR al ejecutar analyzer.inicio")
    elif args.tool == 'Cif':
        banner()
        try:
            cifrado.main(args.msje, args.key, args.accion)
        except:
            logging.info("ERROR al ejecutar PIACifrado.main")
            print ("Atributos para -m y -K de 2 o mas palabras deben estar entre comillas: 'este es un ejemplo '")
main()
