from tkinter import *

raiz = Tk()

raiz.title("Intervalos de confianza")

#raiz.geometry("650x500")

miFrame = Frame(raiz, width = 500, height = 400)

miFrame.pack()

#miFrame.config(bg = "red")

miLabel = Label(miFrame, text = "intervalos de confianza", font = 18)

miLabel.place(x = 100, y = 200)

raiz.mainloop()
