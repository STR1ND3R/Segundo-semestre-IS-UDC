from tkinter import *
import main
def gui():

    TOP = Tk()

#coeficiente a
    a = Entry(TOP, justify=LEFT)
    al = Label(TOP, text="Coeficiente a:")
    a.grid(row=0, column=1)
    al.grid(row=0, column=0)

    

#coeficiente b
    b = Entry(TOP, justify=LEFT)
    bl = Label(TOP, text="Coeficiente b:")
    b.grid(row=1, column=1)
    bl.grid(row=1, column=0)

#coeficiente b
    c = Entry(TOP, justify=LEFT)
    cl = Label(TOP, text="Coeficiente c:")
    c.grid(row=2, column=1)
    cl.grid(row=2, column=0)

#coeficiente x0

    x0 = Entry(TOP, justify=LEFT)
    x0l = Label(TOP, text="X0:")
    x0.grid(row=3, column=1)
    x0l.grid(row=3, column=0)

#coeficiente x1
    x1 = Entry(TOP, justify=LEFT)
    x1l = Label(TOP, text="X1:")
    x1.grid(row=4, column=1)
    x1l.grid(row=4, column=0)

#iteraciones n
    n = Entry(TOP, justify=LEFT)
    nl = Label(TOP, text="Numero de iteraciones:")
    n.grid(row=5, column=1)
    nl.grid(row=5, column=0)


#sacando los valores y calculando
    def calcsec():
        try:
            a_value= float(a.get())
        except:
            a_value = 0.0

        try:
            b_value = float(b.get())
        except:
            b_value = 0.0

        try:
            c_value= float(c.get())
        except:
            c_value = 0.0

        try:
            x0_value= float(x0.get())
        except:
            x0_value = 0.0

        try:
            x1_value= float(x1.get())
        except:
            x1_value = 0.0

        try:
            n_value= int(n.get())
        except:
            n_value = 0.0
        
        ressec.delete(0,END)
        res = main.sec(a_value,b_value,c_value,x0_value,x1_value,n_value)
        ressec.insert(0, res)
        #print(main.sec(a_value,b_value,c_value,x0_value,x1_value,n_value))



#boton secante
    boton = Button(TOP, text="Calcular raiz", command=calcsec)
    boton.grid(row=7, column=1)

#resultado de la secante
    ressec = Entry(TOP, justify=LEFT )
    ressecl = Label(TOP,text="Resultado:")
    ressec.grid(row=6, column=1)
    ressecl.grid(row=6,column=0)

    TOP.mainloop()

if __name__ == '__main__':
    gui()

