from sys import stdin
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
x=np.linspace(0,10,100)
fig,ax=plt.subplots(1,1)
linestyles=['--','-.',':','-']
degrees_of_freedom=[1,3,7,5]
for df,ls in zip(degrees_of_freedom,linestyles):
    ax.plot(x,stats.chi2.pdf(x,df),linestyle=ls)
plt.xlim(0,7)
plt.ylim(0,0.5)
plt.show()
"""

##grados de libertad
print("inserte los grados de libertad")
df = int(stdin.readline().strip())

print("inserte el nivel de confianza, valor mayor que 0 y menor que 1")
beta = float(stdin.readline().strip())
fig,ax = plt.subplots(1,1)
criticalFin = stats.chi2.ppf(0.99, df)

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

plt.xlim(0,xLimi)
plt.ylim(0,yLimi)
plt.show()
