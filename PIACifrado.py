#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Este es el diccinario que va a usar para detectar las palabras de la posicion 0 a la 26
LETRAS = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

#Esta es la funcion main
def main(mensaje, myKey, accion):
    #Aqui se mandan a llamar las funciones de encriptar o descifrar segun tu eleecion
    if accion=='e':
        traducido=cifrar_mensaje(myKey,mensaje)
    elif accion=='d':
        traducido=descifrar_mensaje(myKey,mensaje)
    print("Tu resultado es: "+ traducido)

#Estas son las dos acciones que va a realizar el script
#Ambas reciben como argumento la palabra clave y el texto de la opcion
def cifrar_mensaje(clave,mensa):
    return traductor_mensaje(clave,mensa,'encriptar')

def descifrar_mensaje(clave,mensa):
    return traductor_mensaje(clave,mensa,'descifrar')

#Aqui se reliza la operación de encriptar o descifrar segun lo que se halla seleccionado
def traductor_mensaje(clave,mensa,accion):
    traducido=[]
    indice_clave=0
    clave=clave.upper()
#aqui se realiza la operacion de sustitucion, va a leer cada caracter, lo buscará en que posición está, ya esa posición le va a sumar la posición en la que se encuentra ese caracter en la clave, y será reemplazado por el caracter que se encuentre en el resultado de la suma
    for symbol in mensa:
        num=LETRAS.find(symbol.upper())
        if num!=-1:
            if accion=='encriptar':
                num+=LETRAS.find(clave[indice_clave])
                #Aquí se hace lo mismo, pero a la inversa, en lugar de sumar posiciones, las resta
            elif accion=='descifrar':
                num-=LETRAS.find(clave[indice_clave])
            num%=len(LETRAS)
            if symbol.isupper():
                traducido.append(LETRAS[num])
            elif symbol.islower():
                traducido.append(LETRAS[num].lower())
            indice_clave+=1
            if indice_clave==len(clave):
                indice_clave=0

        else:
            traducido.append(symbol)
    return ('').join(traducido)

#if __name__ == '__main__':
#    main('hello fools', 'jorge', 'encriptar')
