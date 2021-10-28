#!/usr/bin/env python3

import sys
import subprocess
import argparse
import PIAportscan as portscan


#tools: una lista con nombre abreviado de las herrameintas
tools = ['Ps','Ua','EoS']


parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description='''The PIA framework is a set of tools used for security purposes, 
        consists of a portscaner, urlanalyzer, emails and sms sender,etc''', 
                                 epilog = '''examples:
        PIAmain -t Ps -ip 192.168.15.0/24 -p 10-200 -S savehere.txt''')

#choices=tools significa que solo acepta como valores elementos de la lista: tools
parser.add_argument('-t', '--tool', type=str, metavar='', choices=tools, help= 
                   "select a tool: portscaner= Ps ,UrlAnalyzer= Ua ,Emails or SMS= EoS", required=True)
#Creamos el grupo Ps y agregamos los argumentos de PortScaner a ese grupo
Ps = parser.add_argument_group('PortScaner')
Ps.add_argument('-ip', '--address', type=str, metavar='',help='Host(s) to scan' )
Ps.add_argument('-p', '--port', type=str, metavar='',help='ports to scan')
Ps.add_argument('-S', '--save', type=str, metavar='',help='save to file', default=False)
#Creamos el grupo Ua y agregamos los argumentos de UrlAnalyzaer a ese grupo
#NOTA: los argumentos añadidos son solo de prueba
Ua = parser.add_argument_group('UrlAnalyzer')
Ua.add_argument('-A', '--analyze', type=str, metavar='', help='read urls from file')
#Creamos el grupo EoS y agregamos los argumentos de correos o SMS a ese grupo
#NOTA: los argumentos añadidos son solo de prueba
EoS = parser.add_argument_group('Emails and SMS')
EoS.add_argument('-e', '--email', type=str, metavar='', help="sender's email")
args = parser.parse_args()


#Funcion tools, actualmente esta funcion no cumple ninguna funcion en el script.
def tools():
    print ('PortScaner, the simple but powerfull port scannng tool') 
    print ('opcion2 is the simple but powerfull opcion2') 
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


main()



