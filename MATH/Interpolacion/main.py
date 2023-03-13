import matplotlib.pyplot as plt
import numpy as np
import simpy


#newton 1
def inter1():

    x0 = float(input('Escriba el Valor de X0: '))
    fx0 = float(input('Escriba el Valor de f(x0): '))
    x1 = float(input('Escriba el Valor de X1: '))
    fx1 = float(input('Escriba el Valor de f(x1): '))
    x = float(input('Escriba el Valor de X: '))
    fx = fx0 + ((fx1 - fx0)/(x1-x0)) * (x - x0)

    xp = np.array([x0, x1,x])
    yp = np.array([fx0, fx1, fx])

    plt.plot(xp, yp, 'o-')
    plt.plot(xp[-1], yp[-1], 'o')

    plt.savefig("grafica.png")

    return fx


#lagrange 2
def inter2():

    x0 = float(input('Escriba el Valor de X0: '))
    fx0 = float(input('Escriba el Valor de f(x0): '))
    x1 = float(input('Escriba el Valor de X1: '))
    fx1 = float(input('Escriba el Valor de f(x1): '))
    x2 = float(input('Escriba el Valor de X2: '))
    fx2 = float(input('Escriba el Valor de f(x2): '))
    x = float(input('Escriba el Valor de X: '))
    fx = ((x-x1)/(x0-x1)) * ((x-x2)/(x0-x2))*fx0 + ((x-x0)/(x1-x0)) * ((x-x2)/(x1-x2))*fx1 + ((x-x0)/(x2-x0)) * ((x-x1)/(x2-x1))*fx2

    xp = np.array([x0, x1, x2, x])
    yp = np.array([fx0, fx1, fx2, fx])

    x = xp[:-1]
    y = xp[:-1]

    plt.plot(xp, yp, 'o')
    plt.plot(xp[-1], yp[-1], 'o')
    plt.savefig("grafica.png")
    return fx

#lagrange 1
def inter3():
    x0 = float(input('Escriba el Valor de X0: '))
    fx0 = float(input('Escriba el Valor de f(x0): '))
    x1 = float(input('Escriba el Valor de X1: '))
    fx1 = float(input('Escriba el Valor de f(x1): '))
    x = float(input('Escriba el Valor de X: '))
    fx = ((x-x1)/(x0-x1))*fx0 + ((x-x0)/(x1-x0))*fx1

    xp = np.array([x0, x1, x])
    yp = np.array([fx0, fx1, fx])

    plt.plot(xp, yp, 'o-')
    plt.plot(xp[-1], yp[-1], 'o')

    plt.savefig("grafica.png")

    return fx



#newton2
def inter4():
    x0 = float(input('Escriba el Valor de X0: '))
    fx0 = float(input('Escriba el Valor de f(x0): '))
    x1 = float(input('Escriba el Valor de X1: '))
    fx1 = float(input('Escriba el Valor de f(x1): '))
    x2 = float(input('Escriba el Valor de X2: '))
    fx2 = float(input('Escriba el Valor de f(x2): '))
    x = float(input('Escriba el Valor de X: '))

    b0 = fx0
    b1 = (fx1-fx0)/(x1-x0)
    b2 = (((fx2-fx0)/(x2-x0))-b1)/(x2-x1)
    fx = b0 + b1*(x-x0) + b2*(x-x0)*(x-x1)

    xp = np.array([x0, x1, x2, x])
    yp = np.array([fx0, fx1, fx2, fx])

    x = xp[:-1]
    y = xp[:-1]

    plt.plot(xp, yp, 'o')
    plt.plot(xp[-1], yp[-1], 'o')



    plt.savefig("grafica.png")
    return fx


def error(vverdadero, vaprox):

    erabs = vverdadero - vaprox
    errel = (erabs/vverdadero) * 100
    return erabs, errel


def calcular_error(fx):

    a = input('Desea calcular el error absoluto y relativo? (S)/(N)')

    if a.upper() == 'S':

        erabs, errel = error(float(input('Escriba el valor verdadero de f(x): ')), fx)
        print('El error absoluto es de: ' + str(erabs))
        print('El error relativo porcentual es de: ' + str(errel) + '%')


def main():

    a = int(input(
        """
        [1] Interpolación lineal de Newton
        [2] Interpolación lineal de Lagrange
        [3] Interpolación cuadrática de Newton
        [4] Interpolación cuadrática de Lagrange
        
        Escoja un método de interpolación:"""""))

    match a:
        case 1:
            fx = inter1()
            print('El valor de f(x) es: ' + str(fx))
            calcular_error(fx)
        case 2:
            fx = inter3()
            print('El valor de f(x) es: ' + str(fx))
            calcular_error(fx)

        case 3:
            fx = inter2()
            print('El valor de f(x) es: ' + str(fx))
            calcular_error(fx)
        case 4:
            fx = inter4()
            print('El valor de f(x) es: ' + str(fx))
            calcular_error(fx)


if __name__ == '__main__':
    main()
