import os
from PIL import Image as Imagen
from PIL.ExifTags import TAGS as ETIQUETAS
from tkinter.filedialog import askopenfilename

#Esta funcion sobra mucho, pero la dejo por la nostalgia
def haveMta(existen):
    if (existen == True):
        print ("\tMetadatos encontrados:")
    else:
        print ("\tNo hay metadatos encontrados")

def Metadatos():
    contiene_metadatos = False
    datos = {}
    try:
        # Aqui abrimos el explorador de archivos
        archivo_imagen = askopenfilename()
        foto = Imagen.open(archivo_imagen)
        for etiqueta, value in foto._getexif().items():
            if etiqueta in ETIQUETAS:
                datos[ETIQUETAS[etiqueta]] = value
            
        contiene_metadatos = True
    except:
        print ("\tERROR!\n\tPor favor revisa que la ruta sea correcta:\n",archivo_imagen,)
        print ("\t Asegurate que el archivo este en formato JPG")
    #Imprimimos en pantalla los metadatos
    haveMta(contiene_metadatos) 
    for etiqueta, value in datos.items():
        key = ETIQUETAS.get(etiqueta, etiqueta)
        print ("\t-" + key + ": " + str(value))
        


def mta_ruta(ruta):
    # Creamos una variable para avisar si hay o no metadatos
    contiene_metadatos = False
    datos = {}
    try:
        # Asignamos la ruta de la imagen JPG
        foto = Imagen.open(ruta)
        for etiqueta, value in foto._getexif().items():
            if etiqueta in ETIQUETAS:
                datos[ETIQUETAS[etiqueta]] = value            
        contiene_metadatos = True
    except:
        print ("\tERROR!\n\tPor favor revisa que la ruta sea correcta:\n",ruta,)
        print ("\tAsegurate que el archivo este en formato JPG")
    #Imprimimos en pantalla los metadatos
    haveMta(contiene_metadatos) 
    for etiqueta, value in datos.items():
        key = ETIQUETAS.get(etiqueta, etiqueta)
        print ("\t-" + key + ": " + str(value))
    