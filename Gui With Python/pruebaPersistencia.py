from tkinter import *

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