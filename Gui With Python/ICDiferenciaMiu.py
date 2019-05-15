from tkinter import *
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
link curso: https://www.youtube.com/watch?v=nZF9SwhmPRo

"""


def sp(n1,n2,s1,s2):
    res1 = ((s1*s1)*(n1-1))/(n1+n2-2)
    res2 = ((s1*s1)*(n1-1))/(n1+n2-2)
    return (res1+res2)**(0.5)


def ICDiffMiuSigmaConocido(n1, n2, miu1, miu2, sigma1, sigma2, alfa):
    #normal estandar
    z = stats.norm(0,1)
    estadistico = z.ppf(alfa/2)
    limiIzq = miu1-miu2
    limiDer = miu1-miu2
    limiIzq += estadistico*(( ((sigma1**2)/n1) + ((sigma2**2)/n2) ) * 0.5)
    limiDer -= estadistico*(( ((sigma1**2)/n1) + ((sigma2**2)/n2) ) * 0.5)
    print(estadistico)
    return (round(limiIzq,5), round(limiDer,5))

def ICDiffMiuSigmaDesconocidoIguales(n1, n2, miu1, miu2, variacion1, variacion2, alfa):
    df = n1+n2-2
    limiIzq = miu1-miu2
    limiDer = miu1-miu2
    t = stats.t(df)
    estadistico = t.ppf(alfa/2)
    sP = sp(n1, n2, variacion1, variacion2)
    limiIzq += estadistico*(( (1/n1) + (1/n2) ) * 0.5)*sP
    limiDer -= estadistico*(( (1/n1) + (1/n2) ) * 0.5)*sP
    print(estadistico)
    return (round(limiIzq,5), round(limiDer,5))


raiz = Tk()
raiz.title("intervalos de confianza para MIU ")
raiz.geometry("1200x400")

miFrame = Frame(raiz,width = 1200, height = 600)
miFrame.pack()

rowGrid = 1
#######################################
labelTamMuestra1 = Label(miFrame,text = "Tamaño de la muestra1")
labelTamMuestra1.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entryTamMuestra1 = Entry(miFrame)
entryTamMuestra1.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entryTamMuestra1.config(justify = "center")

labelTamMuestra2 = Label(miFrame,text = "Tamaño de la muestra2")
labelTamMuestra2.grid(row = rowGrid, column = 2, padx = 10, pady = 10)

entryTamMuestra2 = Entry(miFrame)
entryTamMuestra2.grid(row = rowGrid, column = 3,padx = 10, pady = 10)
entryTamMuestra2.config(justify = "center")
rowGrid += 1
#######################################
labelMiu1 = Label(miFrame,text = "Valor de Miu1")
labelMiu1.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entryMiu1 = Entry(miFrame)
entryMiu1.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entryMiu1.config(justify = "center")

labelMiu2 = Label(miFrame,text = "Valor de Miu2")
labelMiu2.grid(row = rowGrid, column = 2, padx = 10, pady = 10)

entryMiu2 = Entry(miFrame)
entryMiu2.grid(row = rowGrid, column = 3,padx = 10, pady = 10)
entryMiu2.config(justify = "center")
rowGrid += 1
#######################################
labelVariacion1 = Label(miFrame,text = "valor de la variación1")
labelVariacion1.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entryVariacion1 = Entry(miFrame)
entryVariacion1.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entryVariacion1.config(justify = "center")

labelVariacion2 = Label(miFrame,text = "valor de la variación2")
labelVariacion2.grid(row = rowGrid, column = 2, padx = 10, pady = 10)

entryVariacion2 = Entry(miFrame)
entryVariacion2.grid(row = rowGrid, column = 3,padx = 10, pady = 10)
entryVariacion2.config(justify = "center")
rowGrid += 1
#######################################
labelAlfa = Label(miFrame,text = "valor de la de alfa")
labelAlfa.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entryAlfa = Entry(miFrame)
entryAlfa.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entryAlfa.config(justify = "center")
rowGrid += 1
#######################################
labelSigma1 = Label(miFrame,text = "valor del sigma1 (sino lo conoce deje vació el campo)")
labelSigma1.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entrySigma1 = Entry(miFrame)
entrySigma1.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entrySigma1.config(justify = "center")

labelSigma2 = Label(miFrame,text = "valor del sigma2 (sino lo conoce deje vació el campo)")
labelSigma2.grid(row = rowGrid, column = 2, padx = 10, pady = 10)

entrySigma2 = Entry(miFrame)
entrySigma2.grid(row = rowGrid, column = 3,padx = 10, pady = 10)
entrySigma2.config(justify = "center")
rowGrid += 1
#######################################
labelLimiIz = Label(miFrame,text = "límite Izquierdo")
labelLimiIz.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

labelLimiIzVal = Label(miFrame,text = "0.0")
labelLimiIzVal.grid(row = rowGrid, column = 1, padx = 10, pady = 10)
rowGrid += 1
#######################################
labelDer = Label(miFrame,text = "límite derecho")
labelDer.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

labelDerVal = Label(miFrame,text = "0.0")
labelDerVal.grid(row = rowGrid, column = 1, padx = 10, pady = 10)
rowGrid += 1
#######################################
def capturarDatos():
    n1 = float(entryTamMuestra1.get())
    n2 = float(entryTamMuestra2.get())
    miu1 = float(entryMiu1.get())
    miu2 = float(entryMiu2.get())
    variacion1 = float(entryVariacion1.get())
    variacion2 = float(entryVariacion2.get())
    alfa = float(entryAlfa.get())
    sigma1 = entrySigma1.get()
    sigma2 = entrySigma2.get()
    if(sigma1 and sigma2):
        sigma1 = float(sigma1)
        sigma2 = float(sigma2)
        limites = ICDiffMiuSigmaConocido(n1, n2, miu1, miu2, sigma1, sigma2, alfa)
    else:
        limites = ICDiffMiuSigmaDesconocidoIguales(n1, n2, miu1, miu2, variacion1, variacion2, alfa)
    #actualización valores
    labelLimiIzVal = Label(miFrame,text = str(limites[0]))
    labelLimiIzVal.grid(row = rowGrid-2, column = 1, padx = 10, pady = 10)
    labelDerVal = Label(miFrame,text = str(limites[1]))
    labelDerVal.grid(row = rowGrid-1, column = 1, padx = 10, pady = 10)
    print(limites)

botonSubir = Button(raiz, text = "calcular intervalo", command = capturarDatos)
botonSubir.pack()


raiz.mainloop()