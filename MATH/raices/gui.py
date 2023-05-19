from tkinter import *
import main
def gui():

    TOP = Tk()

#titulo del metodo
    titsec = Text(TOP, height=1, width=50, bg='#DDDDDD')
    titsec.insert(INSERT, "Método de la secante para segundo grado:")
    titsec.grid(row=0, column=0)
#coeficiente a
    a = Entry(TOP, justify=LEFT)
    al = Label(TOP, text="Coeficiente a:")
    a.grid(row=1, column=1)
    al.grid(row=1, column=0)

    

#coeficiente b
    b = Entry(TOP, justify=LEFT)
    bl = Label(TOP, text="Coeficiente b:")
    b.grid(row=2, column=1)
    bl.grid(row=2, column=0)

#coeficiente c
    c = Entry(TOP, justify=LEFT)
    cl = Label(TOP, text="Coeficiente c:")
    c.grid(row=3, column=1)
    cl.grid(row=3, column=0)

#coeficiente x0

    x0 = Entry(TOP, justify=LEFT)
    x0l = Label(TOP, text="X0:")
    x0.grid(row=4, column=1)
    x0l.grid(row=4, column=0)

#coeficiente x1
    x1 = Entry(TOP, justify=LEFT)
    x1l = Label(TOP, text="X1:")
    x1.grid(row=5, column=1)
    x1l.grid(row=5, column=0)

#iteraciones n
    n = Entry(TOP, justify=LEFT)
    nl = Label(TOP, text="Numero de iteraciones:")
    n.grid(row=6, column=1)
    nl.grid(row=6, column=0)


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
    boton.grid(row=8, column=1)

#resultado de la secante
    ressec = Entry(TOP, justify=LEFT )
    ressecl = Label(TOP,text="Resultado:")
    ressec.grid(row=7, column=1)
    ressecl.grid(row=7,column=0)

################################################
################################################
################################################

#titulo del metodo
    titnewr = Text(TOP, height=1, width=70, bg='#DDDDDD')
    titnewr.insert(INSERT, "Método de Newton-Raphson para segundo grado:")
    titnewr.grid(row=0, column=3)
#coeficiente a
    anewr = Entry(TOP, justify=LEFT)
    alnewr = Label(TOP, text="Coeficiente a:")
    anewr.grid(row=1, column=4)
    alnewr.grid(row=1, column=3)

    

#coeficiente b
    bnewr = Entry(TOP, justify=LEFT)
    blnewr = Label(TOP, text="Coeficiente b:")
    bnewr.grid(row=2, column=4)
    blnewr.grid(row=2, column=3)

#coeficiente c
    cnewr = Entry(TOP, justify=LEFT)
    clnewr = Label(TOP, text="Coeficiente c:")
    cnewr.grid(row=3, column=4)
    clnewr.grid(row=3, column=3)

#coeficiente x0

    x0newr = Entry(TOP, justify=LEFT)
    x0lnewr = Label(TOP, text="X0:")
    x0newr.grid(row=4, column=4)
    x0lnewr.grid(row=4, column=3)

#coeficiente x1
    x1newr = Entry(TOP, justify=LEFT)
    x1lnewr = Label(TOP, text="X1:")
    x1newr.grid(row=5, column=4)
    x1lnewr.grid(row=5, column=3)

#iteraciones n
    nnewr = Entry(TOP, justify=LEFT)
    nlnewr = Label(TOP, text="Numero de iteraciones:")
    nnewr.grid(row=6, column=4)
    nlnewr.grid(row=6, column=3)


#sacando los valores y calculando
    def calcnewr():
        try:
            anewr_value= float(anewr.get())
        except:
            anewr_value = 0.0

        try:
            bnewr_value = float(bnewr.get())
        except:
            bnewr_value = 0.0

        try:
            cnewr_value= float(cnewr.get())
        except:
            cnewr_value = 0.0

        try:
            x0newr_value= float(x0newr.get())
        except:
            x0newr_value = 0.0

        try:
            x1newr_value= float(x1newr.get())
        except:
            x1newr_value = 0.0

        try:
            nnewr_value= int(nnewr.get())
        except:
            nnewr_value = 0.0
        
        resnewr.delete(0,END)
        res = main.newr(anewr_value,bnewr_value,cnewr_value,x0newr_value,x1newr_value,nnewr_value)
        resnewr.insert(0, res)
        #print(main.sec(a_value,b_value,c_value,x0_value,x1_value,n_value))



#boton secante
    botonnewr = Button(TOP, text="Calcular raiz", command=calcnewr)
    botonnewr.grid(row=8, column=4)

#resultado de la secante
    resnewr = Entry(TOP, justify=LEFT )
    resnewrl = Label(TOP,text="Resultado:")
    resnewr.grid(row=7, column=4)
    resnewrl.grid(row=7,column=3)

    TOP.mainloop()

if __name__ == '__main__':
    gui()

