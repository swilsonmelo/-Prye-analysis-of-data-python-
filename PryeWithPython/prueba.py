from sys import stdin
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def chiSquare():
    """
    hace la función de chi cuadrado y su grafica
    """

    ##grados de libertad
    print("inserte los grados de libertad")
    df = int(stdin.readline().strip())

    print("inserte el nivel de confianza, valor mayor que 0 y menor que 1")
    beta = float(stdin.readline().strip())
    criticalFin = stats.chi2.ppf(0.99, df)

    fig,ax = plt.subplots(1,1)

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


def normalEstandar():
    """
    Actualmente dado un alfa saca los dos lados del alfa
    """

    print("Vamos a graficar la normal estandar")
    print("Digitar el valor para miu")
    mu = float(stdin.readline().strip())
    print("Digitar el valor para sigma")
    sigma = float(stdin.readline().strip())
    print("Digitar el valor para alfa")
    alfa = float(stdin.readline().strip())
    mu, sigma = 0, 1 # media y desvio estandar
    #alfa = 0.4
    normal = stats.norm(mu, sigma)
    x = np.linspace(normal.ppf(0.00001),normal.ppf(0.99999), 10000)
    fp = normal.pdf(x) # Función de Probabilidad
    plt.plot(x, fp)
    plt.title('Distribución Normal')
    
    plt.xlabel('valores')
    critical = normal.ppf(alfa)
    plt.fill_betweenx(fp, critical*-1, x, where = x >= critical*-1)
    plt.fill_betweenx(fp, critical, x, where = x <= critical)
    plt.show()
    print(critical)


def tStudent():
    """
    Graficando t de Student
    """

    print("inserte los grados de libertad")
    df = float(stdin.readline().strip())
    print("inserte el alfa")
    alfa = float(stdin.readline().strip())
    #df = 15 # parametro de forma.
    t = stats.t(df)
    
    x = np.linspace(t.ppf(0.000001),t.ppf(0.999999), 10000)
    fp = t.pdf(x) # Función de Probabilidad
    plt.plot(x, fp)
    critical = t.ppf(alfa)
    print(critical)
    plt.fill_betweenx(fp, critical*-1, x, where = x >= critical*-1)
    plt.fill_betweenx(fp, critical, x, where = x <= critical)
    plt.title('Distribución t de Student')
    
    plt.xlabel('valores')
    plt.show()


def main():
    print("digite 1 para chicuadrado")
    print("digite 2 para normal estandar")
    print("digite 3 t Student")
    n = int(stdin.readline().strip())
    if(n == 1):
        chiSquare()
    elif(n == 2):
        normalEstandar()
    elif(n == 3):
        tStudent()

main()