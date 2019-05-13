from tkinter import *

"""
link curso: https://www.youtube.com/watch?v=nZF9SwhmPRo

"""

raiz = Tk()
raiz.title("intervalos de confianza para MIU")

def calcularIntervaloSigmaDesconocido(n, miu, variacion):
    limiIzq = float("-inf")
    limiDer = float("inf")
    return (limiIzq,limiDer)

miFrame = Frame(raiz,width = 1200, height = 600)
miFrame.pack()

labelTamMuestra = Label(miFrame,text = "Tamaño de la muestra")
labelTamMuestra.grid(row = 0, column = 0, padx = 10, pady = 10)

entryTamMuestra = Entry(miFrame)
entryTamMuestra.grid(row = 0, column = 1,padx = 10, pady = 10)
entryTamMuestra.config(justify = "center")

labelSigma = Label(miFrame,text = "Tamaño de la muestra")
labelSigma.grid(row = 0, column = 0, padx = 10, pady = 10)

entrySigma = Entry(miFrame)
entrySigma.grid(row = 0, column = 1,padx = 10, pady = 10)
entrySigma.config(justify = "center")

labelVariacion = Label(miFrame,text = "Tamaño de la muestra")
labelVariacion.grid(row = 0, column = 0, padx = 10, pady = 10)

entryVariacion = Entry(miFrame)
entryVariacion.grid(row = 0, column = 1,padx = 10, pady = 10)
entryVariacion.config(justify = "center")

def capturarDatos():
    print()

botonSubir = Button(raiz, text = "Enviar", command = capturarDatos)
botonSubir.pack()


