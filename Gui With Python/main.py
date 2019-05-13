from tkinter import *
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
link curso: https://www.youtube.com/watch?v=nZF9SwhmPRo

"""

def IntervaloMiuSigmaConocido(n, miu, variacion, alfa, sigma):
    #normal estandar
    z = stats.norm(0,1)
    estadistico = z.ppf(alfa/2)
    limiIzq = miu
    limiDer = miu
    


def IntervaloMiuSigmaDesconocido(n, miu, variacion, alfa):
    df = n-1
    limiIzq = miu
    limiDer = miu
    t = stats.t(df)
    estadistico = t.ppf(alfa/2)
    limiIzq += estadistico*(variacion/((n)**0.5)) 
    limiDer -= estadistico*(variacion/((n)**0.5))
    print(estadistico)
    return (round(limiIzq,5),round(limiDer,5))


raiz = Tk()
raiz.title("intervalos de confianza para MIU ")
raiz.geometry("600x400")

miFrame = Frame(raiz,width = 1200, height = 600)
miFrame.pack()

rowGrid = 1
#######################################
labelTamMuestra = Label(miFrame,text = "Tamaño de la muestra")
labelTamMuestra.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entryTamMuestra = Entry(miFrame)
entryTamMuestra.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entryTamMuestra.config(justify = "center")
rowGrid += 1
#######################################
labelMiu = Label(miFrame,text = "Valor de Miu")
labelMiu.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entryMiu = Entry(miFrame)
entryMiu.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entryMiu.config(justify = "center")
rowGrid += 1
#######################################
labelVariacion = Label(miFrame,text = "valor de la variación")
labelVariacion.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entryVariacion = Entry(miFrame)
entryVariacion.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entryVariacion.config(justify = "center")
rowGrid += 1
#######################################
labelAlfa = Label(miFrame,text = "valor de la de alfa")
labelAlfa.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entryAlfa = Entry(miFrame)
entryAlfa.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entryAlfa.config(justify = "center")
rowGrid += 1
#######################################
labelSigma = Label(miFrame,text = "valor del sigma (sino lo conoce deje vació el campo)")
labelSigma.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entrySigma = Entry(miFrame)
entrySigma.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entrySigma.config(justify = "center")
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
    n = float(entryTamMuestra.get())
    variacion = float(entryVariacion.get())
    miu = float(entryMiu.get())
    alfa = float(entryAlfa.get())
    sigma = entrySigma.get()
    if(sigma):
        print(sigma)
    else:
        limites = IntervaloMiuSigmaDesconocido(n,miu,variacion, alfa)
    #actualización valores
    labelLimiIzVal = Label(miFrame,text = str(limites[0]))
    labelLimiIzVal.grid(row = rowGrid-2, column = 1, padx = 10, pady = 10)
    labelDerVal = Label(miFrame,text = str(limites[1]))
    labelDerVal.grid(row = rowGrid-1, column = 1, padx = 10, pady = 10)
    print(limites)

botonSubir = Button(raiz, text = "calcular intervalo", command = capturarDatos)
botonSubir.pack()


raiz.mainloop()