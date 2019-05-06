import numpy as np
from scipy import stats
import matplotlib.pyplot as plt



x=np.linspace(0,10,100)
fig,ax=plt.subplots(1,1)
linestyles=['--','-.',':','-']
degrees_of_freedom=[1,3,7,5]
for df,ls in zip(degrees_of_freedom,linestyles):
    ax.plot(x,stats.chi2.pdf(x,df),linestyle=ls)
plt.xlim(0,7)
plt.ylim(0,0.5)
plt.show()

