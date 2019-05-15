from tkinter import *
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
link curso: https://www.youtube.com/watch?v=nZF9SwhmPRo

"""

def IntervaloSigma(n,s,alfa):
    df = n-1
    numerador = (n-1)*s*s
    chi  = stats.chi2(df)
    chi1 = chi.ppf(alfa/2)
    chi2 = chi.ppf(1-alfa/2)
    print("chi",chi1,chi2)
    limiDer = (numerador/chi1)**(0.5)
    limiIz = (numerador/chi2)**(0.5)
    return (round(limiIz,5), round(limiDer,5))


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
labelLimiIz = Label(miFrame,text = "límite Izquierdo")
labelLimiIz.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

labelLimiIzVal = Label(miFrame,text = "0.0")
labelLimiIzVal.grid(row = rowGrid, column = 1, padx = 10, pady = 10)
rowGrid += 1
#######################################
labelLimiDer = Label(miFrame,text = "límite derecho")
labelLimiDer.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

labelDerVal = Label(miFrame,text = "0.0")
labelDerVal.grid(row = rowGrid, column = 1, padx = 10, pady = 10)
rowGrid += 1
#######################################
def capturarDatos():
    n = float(entryTamMuestra.get())
    variacion = float(entryVariacion.get())
    alfa = float(entryAlfa.get())
    limites = IntervaloSigma(n,variacion, alfa)
    #actualización valores
    labelLimiIzVal = Label(miFrame,text = str(limites[0]))
    labelLimiIzVal.grid(row = rowGrid-2, column = 1, padx = 10, pady = 10)
    labelLimiDerVal = Label(miFrame,text = str(limites[1]))
    labelLimiDerVal.grid(row = rowGrid-1, column = 1, padx = 10, pady = 10)
    print(limites)

botonSubir = Button(raiz, text = "calcular intervalo", command = capturarDatos)
botonSubir.pack()


raiz.mainloop()