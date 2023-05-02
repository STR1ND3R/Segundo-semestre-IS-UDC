from tkinter import *
import main
def gui():

    TOP = Tk()

    a = Entry(TOP, justify=LEFT)
    al = Label(TOP, text="Coeficiente a:")

    a.grid(row=0, column=1)
    al.grid(row=0, column=0)

    b = Entry(TOP, justify=LEFT)
    bl = Label(TOP, text="Coeficiente b:")

    b.grid(row=1, column=1)
    bl.grid(row=1, column=0)

    c = Entry(TOP, justify=LEFT)
    cl = Label(TOP, text="Coeficiente c:")

    c.grid(row=2, column=1)
    cl.grid(row=2, column=0)

    x0 = Entry(TOP, justify=LEFT)
    x0l = Label(TOP, text="X0:")

    x0.grid(row=3, column=1)
    x0l.grid(row=3, column=0)

    x1 = Entry(TOP, justify=LEFT)
    x1l = Label(TOP, text="X1:")

    x1.grid(row=4, column=1)
    x1l.grid(row=4, column=0)

    TOP.mainloop()

if __name__ == '__main__':
    gui()

