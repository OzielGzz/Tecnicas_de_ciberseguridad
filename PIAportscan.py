#!/usr/bin/env python3

import nmap 
import argparse


#parser = argparse.ArgumentParser(description='Network Scanner')
#parser.add_argument('-H', '--host', type=str, metavar='', required=True, help='Host(s) to scan')
#parser.add_argument('-p', '--port', type=str, metavar='', required=True, help='Port or range of ports')
#group = parser.add_mutually_exclusive_group()
#group.add_argument('-S', '--save', action='store_true', help='save to file')
#args = parser.parse_args()


def PortScan(host, port):
    nm = nmap.PortScanner()
    nm.scan(host, port)
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
   
            lport = nm[host][proto].keys()
#            lport.sort()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))


def Scansaver(host, port, arch):
    nm = nmap.PortScanner()
    nm.scan(host, port)
    #name = input('Guardar como: ')
    #archname = name + '.txt'
    with open(arch, 'w')as arch:
        arch.write(nm.csv())


if __name__ == '__main__':
    if args.save:
        Scansaver(args.host, args.port)
    else:
        print (PortScan(args.host, args.port))

