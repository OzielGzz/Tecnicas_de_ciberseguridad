#!/usr/bin/env python3

import sys
import subprocess


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



def banner():
    OS = sys.platform
    if OS == 'linux' or OS == 'darwin':
       subprocess.run("./BASHbanner")
    elif OS == 'win32':
        subprocess.run("./PSbanner")
    else:
        Pybanner()



def main():
    while True:
        print ('\n\nopcion 1\nopcion 2\nopcion 3\nopcion 4\nopcion 5\nsalir')
        entrada = input('\n>>> ')
        if entrada == '1':
            print ('OPCION 1')
        elif entrada == '2':
            print ('OPCION 2')
        elif entrada == '3':
            print ('OPCION 3')
        elif entrada == '4':
            print ('OPCION 4')
        elif entrada == '5':
            print ('OPCION 5')
        elif entrada == 'salir':
            break
        else:
            print ('OPCION NO ENCONTRADA')



banner()
main()

