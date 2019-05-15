from tkinter import *
from sys import stdin
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


root = Tk()
varOpcion = IntVar()


Radiobutton(root, text="male", variable=varOpcion, value = 1).pack()
Radiobutton(root, text="female", variable=varOpcion, value = 2).pack()
mainloop()