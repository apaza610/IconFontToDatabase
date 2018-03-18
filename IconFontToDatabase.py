# coding: utf-8

#####################################################################
#   llenado de campos de una CSV usando IconFonts
#####################################################################

import tkinter
import os
from fontTools.ttLib import TTFont

raiz = tkinter.Tk()
raiz.geometry("540x100")
archivoCSV = open('D:\\cosas\\listaGlyphs.csv','a',encoding='utf-8')    # guardar salida aqui pada DataBase
miFont = TTFont('d:/cosas/icf_devicon.ttf')                             # creacion de objeto tipo  TTFont

diccioDECHEXglyphs = miFont.getBestCmap()

#------------- Label variable con cada click -------------------------
contador = 3                                    # para evitar los Glyphs de CTRL del OS

def crearUnicode():
    global contador
    global diccioDECHEXglyphs

    valorINT = list( diccioDECHEXglyphs.keys() )[contador]
    return chr(valorINT)

def registrar():
    global contador
    global diccioDECHEXglyphs

    valorUnicode = crearUnicode()
        
    salidaTexto.config(text=valorUnicode,)          # actualizar el icono de la GUI
    #print(valorUnicode)

    valorINT = list( diccioDECHEXglyphs.keys() )[contador]
    archivoCSV.write("'',"+ valorUnicode +",Nombre_Fuente," + str(valorINT) + "," + descripcion.get() + "\n")        # escribir en los campos del CSV
    descripcion.delete(0, tkinter.END)                                              # limpiar pantalla para siguiente entrada
    
    contador += 1
    return

#------------------------- La GUI -------------------------------------------
tkinter.Label(raiz, text="Describir el Glyph siguiente:").grid(row=0,column=0)

salidaTexto = tkinter.Label(raiz, text=crearUnicode(), font=('icf_devicon',40))
salidaTexto.grid(row=0,column=10)

#------------ Entrada de acciones de usuario ------------------------
boton = tkinter.Button(raiz, text="guardar a CSV", command=lambda:registrar())
boton.grid(row=1,column=0)

descripcion = tkinter.Entry(raiz, width=50)
descripcion.grid(row=1,column=1)

raiz.mainloop()
archivoCSV.close()