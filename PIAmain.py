#!/usr/bin/env python3

import sys
import subprocess
import argparse
import configparser
import PIAportscan as portscan
import PIAanalyzer as analyzer
from PIAmetadatos import mta_ruta as mta
import PIAEmailSMS as emailsms


#tools: una lista con nombre abreviado de las herrameintas
tools = ['Ps','Ua','EoS', 'Mta']


parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description='''The PIA framework is a set of tools used for security purposes,
        consists of a portscaner, urlanalyzer, emails and sms sender,etc''',
                                 epilog = '''
    Dato: Para la funcion de Metadatos no se requieren argumentos

    examples for Ps:
        PIAmain -t Ps -ip 192.168.15.0/24 -p 10-200 -S savehere.txt

    examples for Ua:
        PIAmain -t Ua -K (Tu key de VirusTotal) -U urls_sospechosas.txt

    example for EoS:
        PIAmain -t EoS -EoS email -e (nuestro correo) -co (contraseña) -re (correo de quien recibe) -a "aqui va el asunto" -b "mensaje"
        PIAmain -t EoS -EoS sms -SID "Nuestro SID" -to "Nuestro token" -n "nuestro numero de Twilio" -d +52numero destino -m "mensaje"
        ''')

#choices=tools significa que solo acepta como valores elementos de la lista: tools
parser.add_argument('-t', '--tool', type=str, metavar='', choices=tools, help=
                   "select a tool: portscaner= Ps, UrlAnalyzer= Ua, Emails or SMS= EoS, Metadata from Images= Mta", required=True)
#Creamos el grupo Ps y agregamos los argumentos de PortScaner a ese grupo
Ps = parser.add_argument_group('PortScaner')
Ps.add_argument('-ip', '--address', type=str, metavar='',help='Host(s) to scan' )
Ps.add_argument('-p', '--port', type=str, metavar='',help='ports to scan')
Ps.add_argument('-S', '--save', type=str, metavar='',help='save to file', default=False)
#Creamos el grupo Ua y agregamos los argumentos de UrlAnalyzaer a ese grupo
Ua = parser.add_argument_group('UrlAnalyzer')
Ua.add_argument('-K', '--Key', type=str, metavar='', help="Ingresa tu Key de Virus Total")
Ua.add_argument('-U', '--Urls', type=str, metavar='', help="Archivo con ulrs sospechosas")

#Creamos el grupo EoS y agregamos los argumentos de correos o SMS a ese grupo
EoS = parser.add_argument_group('Emails and SMS')
EoS.add_argument('-EoS', type=str,
                    help='Escribir que deseamos enviar: email, sms, ambos')
# Parametros para email:
EoS.add_argument('-e', '--email', type= str, metavar='',
                    help="Ingresar nuestro correo")
EoS.add_argument('-co', '--contra', type= str, metavar='',
                    help="Ingresar nuestra contraseña")
EoS.add_argument('-re', '--receiver', type= str, metavar='',
                    help="Correo de quien recibira el email")
EoS.add_argument('-a', '--asunto', type= str, metavar='',
                    help="Ingresar el asunto del correo")
EoS.add_argument('-b', '--body', type= str, metavar='',
                    help="Ingresar el cuerpo del correo")
EoS.add_argument('-f', '--file', default= 'no', metavar='',
                    help="Especificar la ruta del archivo a adjuntar")
# Parametros para sms:
EoS.add_argument('-SID', metavar='',
                    help="Ingresar nuestro SID de Twilio")
EoS.add_argument('-to', metavar='',   
                    help="Ingresar nuestra Token de Twilio")
EoS.add_argument('-n','--number', metavar='',
                    help="Ingresar nuestro numero de Twilio")
EoS.add_argument('-d',    metavar='',  
                    help="Ingresar el numero del destinatario(Agregar +52)")
EoS.add_argument('-m', '--msj', metavar='',       
                    help="Ingresar el mensaje a enviar")
EoS.add_argument('--config', '-c', type=argparse.FileType('r'), help='config file')

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
       subprocess.run("./BASHbanner")
    elif OS == 'win32':
        subprocess.run("./PSbanner")
    else:
        Pybanner()


def main():
    print ('running main')
    # Ejecutando el portscanner
    if args.tool == 'Ps':
        print ('Ps selected')
        if not args.address == None:
            if args.save == False:
                    print (banner())
                    print (portscan.PortScan(args.address, args.port))
            else:
                    portscan.Scansaver(args.address, args.port, args.save)
        else:
            print ('ADDRESS NOT GIVEN')

    # Fin de Portscanner
    elif args.tool == 'Mta':
        print ('Metadatos de una Imagen')
        mta()

    elif args.tool == 'EoS':
        print ('EoS Selected')
        if args.EoS == 'email':
            emailsms.send_emailP(args.email,args.contra,args.receiver,args.asunto,args.body,args.file)

        elif args.EoS == 'sms':
            emailsms.send_smsP(args.SID,args.to,args.number,args.d,args.msj)

        elif args.EoS == 'ambos':
            emailsms.send_emailP(args.email,args.contra,args.receiver,args.asunto,args.body,args.file)
            emailsms.send_smsP(args.SID,args.to,args.number,args.d,args.msj)
            
    elif args.tool == 'Ua':
        print ("")
        print ('Ua selected')
        print ("")
        print (Pybanner())
        print ("")
        analyzer.inicio(args.Key, args.Urls)

main()
