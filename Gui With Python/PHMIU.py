from tkinter import *
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


root = Tk()
root.title("Prueba de hipotesis para miu")

root.geometry("800x600")

myFrame = Frame(root, width = 800, height= 600)
myFrame.pack()


rowGrid = 1
#######################################
labelTamMuestra = Label(myFrame,text = "Tamaño de la muestra")
labelTamMuestra.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entryTamMuestra = Entry(myFrame)
entryTamMuestra.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entryTamMuestra.config(justify = "center")
rowGrid += 1
#######################################
labelMiu = Label(myFrame,text = "Valor de Miu")
labelMiu.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entryMiu = Entry(myFrame)
entryMiu.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entryMiu.config(justify = "center")
rowGrid += 1
#######################################
labelMedia = Label(myFrame,text = "Valor de la media")
labelMedia.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entryMedia = Entry(myFrame)
entryMedia.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entryMedia.config(justify = "center")
rowGrid += 1
#######################################
labelVariacion = Label(myFrame,text = "valor de la variación")
labelVariacion.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entryVariacion = Entry(myFrame)
entryVariacion.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entryVariacion.config(justify = "center")
rowGrid += 1
#######################################
labelAlfa = Label(myFrame,text = "valor de la de alfa")
labelAlfa.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entryAlfa = Entry(myFrame)
entryAlfa.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entryAlfa.config(justify = "center")
rowGrid += 1
#######################################
labelSigma = Label(myFrame,text = "valor del sigma (sino lo conoce deje vacio el campo)")
labelSigma.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

entrySigma = Entry(myFrame)
entrySigma.grid(row = rowGrid, column = 1,padx = 10, pady = 10)
entrySigma.config(justify = "center")
rowGrid += 1
#######################################
AlfaRegion = 0.005
muestra = 60
varOpcion = IntVar()
varOpcion.set(1)
miuV = StringVar()
miuV.set("@")

Radiobutton(myFrame, text="Ho = "+miuV.get()+" and H1 != "+miuV.get(), variable=varOpcion, value = 1).grid(row = rowGrid, column = 0,padx = 10, pady = 10)
rowGrid += 1
Radiobutton(myFrame, text="Ho >= "+miuV.get()+" and H1 < "+miuV.get(), variable=varOpcion, value = 2).grid(row = rowGrid, column = 0,padx = 10, pady = 10)
rowGrid += 1
Radiobutton(myFrame, text="Ho <= "+miuV.get()+" and H1 > "+miuV.get(), variable=varOpcion, value = 3).grid(row = rowGrid, column = 0,padx = 10, pady = 10)
rowGrid += 1

#######################################
labelrr = Label(myFrame,text = "Region de rechazo: ")
labelrr.grid(row = rowGrid, column = 0, padx = 10, pady = 10)
rowGrid += 1
#######################################
labelEstadisP = Label(myFrame,text = "Estadistico de prueba: ")
labelEstadisP.grid(row = rowGrid, column = 0, padx = 10, pady = 10)
rowGrid += 1
#######################################

def calcularRegionDeRechazo(n, miu, x, variacion, alfa, tipoHipotesis):
    n = float(n)
    miu = float(miu)
    x = float(x)
    variacion = float(variacion)
    alfa = float(alfa)
    estadisticoPrueba = round((x - miu)/(variacion/(n**0.5)),5)
    if(n > 30):
        distribucion = stats.norm(0,1)
    else:
        distribucion = stats.t(n-1)
    res = []
    rr1 = (float("-inf"), round(distribucion.ppf(alfa/2),5))
    rr2 = (round(-1*distribucion.ppf(alfa/2),5), float("inf"))
    if(tipoHipotesis == 1):
        res.append(rr1)
        res.append(rr2)        
    elif(tipoHipotesis == 2):
        res.append(rr1)
    elif(tipoHipotesis == 3):
        res.append(rr2)    
    #print(res,estadisticoPrueba)
    res.append(estadisticoPrueba)
    return res

def capturarDatos():
    global muestra, AlfaRegion
    n = entryTamMuestra.get()
    miu = entryMiu.get()
    x = entryMedia.get()
    s = entryVariacion.get()
    sigma = entrySigma.get()
    alfa = entryAlfa.get()
    AlfaRegion = float(alfa)
    muestra = float(n)
    if(not sigma):
        regionRechazo = calcularRegionDeRechazo(n, miu, x, s, alfa, varOpcion.get())
    else:        
        regionRechazo = calcularRegionDeRechazo(n, miu, x, sigma, alfa, varOpcion.get())
    estadistico = regionRechazo[-1]
    if(len(regionRechazo) >= 3):
        rr = [str(regionRechazo[0]), str(regionRechazo[1])]
    else:
        rr = str(regionRechazo[0])

    labelrr = Label(myFrame,text = "Region de rechazo: "+" ".join(rr))
    labelrr.grid(row = rowGrid-2, column = 0, padx = 10, pady = 10)
    labelEstadisP = Label(myFrame,text = "Estadistico de prueba: "+ str(estadistico))
    labelEstadisP.grid(row = rowGrid-1, column = 0, padx = 10, pady = 10)


def tStudent(df, alfa, tipo):
    """
    Graficando t de Student
    """
    t = stats.t(df)
    x = np.linspace(t.ppf(0.000001),t.ppf(0.999999), 10000)
    fp = t.pdf(x) # Función de Probabilidad
    plt.plot(x, fp)
    critical = t.ppf(alfa)
    if(tipo == 3 or tipo == 1):
        plt.fill_betweenx(fp, critical*-1, x, where = x >= critical*-1)
    if(tipo == 2 or tipo == 1):
        plt.fill_betweenx(fp, critical, x, where = x <= critical)
    plt.title('Distribución t de Student')
    plt.xlabel('valores')
    plt.show()  


def normalEstandar(mu, sigma, alfa, tipo):
    """
    Actualmente dado un alfa saca los dos lados del alfa
    mu = media
    sigma = variación estandar
    alfa = area bajo la curva
    tipo:
    -1 area de la izquierda
    0 area de izquierda y derecha
    1 area de la derecha
    """
    #mu, sigma = 0, 1 # media y desvio estandar
    #alfa = 0.4j
    normal = stats.norm(mu, sigma)
    x = np.linspace(normal.ppf(0.00001),normal.ppf(0.99999), 10000)
    fp = normal.pdf(x) # Función de Probabilidad
    plt.plot(x, fp)
    plt.title('Distribución Normal')
    plt.xlabel('valores')
    criticalL = normal.ppf(alfa)
    criticalR =criticalL + 2*(mu-criticalL)
    if(tipo == 3 or tipo == 1):
        plt.fill_betweenx(fp, criticalR, x, where = x >= criticalR)
    if(tipo == 2 or tipo == 1):
        plt.fill_betweenx(fp, criticalL, x, where = x <= criticalL)
    plt.show()
    #print(criticalL,criticalR)

def graficarRegion():
    global muestra, AlfaRegion
    if(muestra <= 30):
        tStudent(muestra-1,  AlfaRegion/2, varOpcion.get())
    else:
        normalEstandar(0, 1, AlfaRegion/2,varOpcion.get())
    

    

botonDatos = Button(root, text = "Región de rechazo", command = capturarDatos)
botonDatos.pack()


botonGraficar = Button(root, text = "Graficar Región de rechazo", command = graficarRegion)
botonGraficar.pack()

""""
labelLimiIz = Label(myFrame,text = "límite Izquierdo")
labelLimiIz.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

labelLimiIzVal = Label(myFrame,text = "0.0")
labelLimiIzVal.grid(row = rowGrid, column = 1, padx = 10, pady = 10)
rowGrid += 1
#######################################
labelDer = Label(myFrame,text = "límite derecho")
labelDer.grid(row = rowGrid, column = 0, padx = 10, pady = 10)

labelDerVal = Label(myFrame,text = "0.0")
labelDerVal.grid(row = rowGrid, column = 1, padx = 10, pady = 10)
rowGrid += 1
#######################################
"""



root.mainloop()