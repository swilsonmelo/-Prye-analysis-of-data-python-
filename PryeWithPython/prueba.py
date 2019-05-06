from sys import stdin
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def chiSquare(df,beta):
    """
    hace la función de chi cuadrado y su grafica
    df = grados de libertad
    beta = nivel de confianza
    """
    
    criticalFin = stats.chi2.ppf(0.99, df)
    fig,ax = plt.subplots(1,1)
    fig = None

    #print(criticalFin)
    ini = 0
    fin = int(criticalFin)+20
    cant = 100000

    #generea el conjunto de coordendas
    #entre mayor sea cant es más fluida la gráfica
    x = np.linspace(ini,fin,cant)
    y = stats.chi2.pdf(x,df)
    maxY = max(y)+0.05
    maxX = max(x)
    ax.plot(x,y)

    #ax.fill_between(x, y, y2 = 0,color = 'b')
    critical = stats.chi2.ppf(beta, df)

    #print(critical)
    ax.fill_betweenx(y, critical, x, where = x >= critical)

    xLimi = maxX
    yLimi = maxY
    #print(xLimi,yLimi)

    if(df == 1):
        yLimi = 1
    plt.title('Distribución chi Cuadrado')
    plt.xlabel('valores Chi Cuadrado')
    plt.xlim(0,xLimi)
    plt.ylim(0,yLimi)
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
    if(tipo == 1 or tipo == 0):
        plt.fill_betweenx(fp, criticalR, x, where = x >= criticalR)
    if(tipo == -1 or tipo == 0):
        plt.fill_betweenx(fp, criticalL, x, where = x <= criticalL)
    plt.show()
    print(criticalL,criticalR)

def tStudent(df, alfa, tipo):
    """
    Graficando t de Student
    """
    t = stats.t(df)
    x = np.linspace(t.ppf(0.000001),t.ppf(0.999999), 10000)
    fp = t.pdf(x) # Función de Probabilidad
    plt.plot(x, fp)
    critical = t.ppf(alfa)
    if(tipo == 1 or tipo == 0):
        plt.fill_betweenx(fp, critical*-1, x, where = x >= critical*-1)
    if(tipo == -1 or tipo == 0):
        plt.fill_betweenx(fp, critical, x, where = x <= critical)
    plt.title('Distribución t de Student')
    plt.xlabel('valores')
    plt.show()

def fFischer(v1,v2,alfa):
    """
    v1 = grados de libertad 1
    v2 = grados de libertad 2
    alfa = area debajo de la curva a la derecha
    """
    v1 = 30
    v2 = 25
    
    f = stats.f(v1,v2)
    x = np.linspace(f.ppf(0.000001),f.ppf(0.999999), 10000)
    fp = f.pdf(x)
    plt.plot(x,fp)
    plt.show()

def main():
    #fFischer()
    print("digite 1 para chicuadrado")
    print("digite 2 para normal estandar")
    print("digite 3 t Student")
    n = int(stdin.readline().strip())
    if(n == 1):
        print("inserte los grados de libertad (valor minimo 1)")
        df = int(stdin.readline().strip())
        print("inserte el nivel de confianza, valor mayor que 0 y menor que 1")
        beta = float(stdin.readline().strip())
        chiSquare(df,beta)

    elif(n == 2):
        print("Digitar el valor para miu")
        mu = float(stdin.readline().strip())
        print("Digitar el valor para sigma")
        sigma = float(stdin.readline().strip())
        print("Digitar el valor para alfa")
        alfa = float(stdin.readline().strip())
        print("I para el area a la izquierda, D para el area a la derecha y B para ambas areas ")
        tipo = stdin.readline().strip()
        if(tipo == "I"):
            lados = -1
        elif(tipo == "B"):
            lados = 0
        else:
            lados = 1
        normalEstandar(mu,sigma,alfa,lados)

    elif(n == 3):
        print("inserte los grados de libertad(valor minimo 1)")
        df = float(stdin.readline().strip())
        print("inserte el alfa")
        alfa = float(stdin.readline().strip())
        print("I para el area a la izquierda, D para el area a la derecha y B para ambas areas ")
        tipo = stdin.readline().strip()
        print(tipo)
        if(tipo == "I"):
            lados = -1
        elif(tipo == "B"):
            lados = 0
        else:
            lados = 1
        tStudent(df, alfa, lados)
        
main()