from tkinter import *
from sys import stdin
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

mainteance = True
def quit():
    global root
    global mainteance
    mainteance = False
    root.quit()

root = Tk()
while mainteance:
    Button(root, text="Quit", command=quit).pack()
    if(mainteance == False):
        break
    root.mainloop()
    #do something
print("ok")