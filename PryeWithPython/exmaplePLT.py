import numpy as np
from scipy import stats
import matplotlib.pyplot as plt



#First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

#Creates just a figure and only one subplot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')

plt.show()



f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)
plt.show()

#Creates four polar axes, and accesses them through the returned array
fig, axes = plt.subplots(2, 2, subplot_kw=dict(polar=True))
axes[0, 0].plot(x, y)
axes[1, 1].scatter(x, y)
plt.show()

#Share a X axis with each column of subplots
plt.subplots(2, 2, sharex='col')
plt.show()

#Share a Y axis with each row of subplots
plt.subplots(2, 2, sharey='row')
plt.show()

#Share both X and Y axes with all subplots
plt.subplots(2, 2, sharex='all', sharey='all')
plt.show()

#Note that this is the same as
plt.subplots(2, 2, sharex=True, sharey=True)
plt.show()

#Creates figure number 10 with a single subplot
#and clears it if it already exists.
fig, ax=plt.subplots(num=10, clear=True)
plt.show()
