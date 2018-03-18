# coding: utf-8
#####################################################################
# Fill csv file while watching the glyphs of a IconFont
# autor: Homar Richard Orozco Apaza
# 
#####################################################################

import tkinter
import os
from fontTools.ttLib import TTFont

raiz = tkinter.Tk()
raiz.geometry("540x100")
archivoCSV = open('D:\\cosas\\listaGlyphs.csv','a',encoding='utf-8')    # guardar salida aqui pada DataBase
miFont = TTFont('d:/cosas/icf_devicon.ttf')                             # creacion de objeto tipo  TTFont

diccioDECHEXglyphs = miFont.getBestCmap()                               # dictionary with DEC , HEX values of glyphs
contador = 3                                                            # to avoid CTRL characters of a font

#------------- Label variable con cada click -------------------------

def crearUnicode(indice):    
    global diccioDECHEXglyphs
    valorINT = list( diccioDECHEXglyphs.keys() )[indice]
    return chr(valorINT)

def registrar():
    global contador
    global diccioDECHEXglyphs

    valorUnicode = crearUnicode(contador)
    valorINT = list( diccioDECHEXglyphs.keys() )[contador]
    archivoCSV.write("'',"+ valorUnicode +",Nombre_Fuente," + str(valorINT) + "," + descripcion.get() + "\n")   # escribir en los campos del CSV
    
    contador += 1
    
    salidaTexto.config(text=crearUnicode(contador),)    # actualizar el icono de la GUI    
    descripcion.delete(0, tkinter.END)                  # limpiar pantalla para siguiente entrada
    
    return

#------------------------- La GUI -------------------------------------------
tkinter.Label(raiz, text="Describir el Glyph siguiente:").grid(row=0,column=0)

salidaTexto = tkinter.Label(raiz, text=crearUnicode(contador), font=('icf_devicon',40))
salidaTexto.grid(row=0,column=10)

#------------ Entrada de acciones de usuario ------------------------
boton = tkinter.Button(raiz, text="guardar a CSV", command=lambda:registrar())
boton.grid(row=1,column=0)

descripcion = tkinter.Entry(raiz, width=50)
descripcion.grid(row=1,column=1)

raiz.mainloop()
archivoCSV.close()
