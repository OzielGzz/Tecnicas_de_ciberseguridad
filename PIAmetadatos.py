import os
from PIL import Image as Imagen
from PIL.ExifTags import TAGS as ETIQUETAS
from tkinter.filedialog import askopenfilename

def Metadatos():
    print("Ejecutada la funcion")
    # Explorador de archivos
    archivo_imagen = askopenfilename()
    foto = Imagen.open(archivo_imagen)
    contiene_metadatos = False
    datos = {}
    try:
        for etiqueta, value in foto._getexif().items():
            if etiqueta in ETIQUETAS:
                datos[ETIQUETAS[etiqueta]] = value
            
        contiene_metadatos = True
    except:
        print("La imagen no es compatible porque no contiene metadatos")
    #print (datos)
    print("")
   
    for etiqueta, value in datos.items():
        key = ETIQUETAS.get(etiqueta, etiqueta)
        print ("\t-" + key + ": " + str(value))
