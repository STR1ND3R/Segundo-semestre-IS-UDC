
def inter1():
    x0 = float(input('Escriba el Valor de X0: '))
    fx0 = float(input('Escriba el Valor de f(x0): '))
    x1 = float(input('Escriba el Valor de X1: '))
    fx1 = float(input('Escriba el Valor de f(x1): '))
    x = float(input('Escriba el Valor de X: '))
    fx = fx0 + ((fx1 - fx0)/(x1-x0)) * (x - x0)

    return fx


def inter2():

    x0 = float(input('Escriba el Valor de X0: '))
    fx0 = float(input('Escriba el Valor de f(x0): '))
    x1 = float(input('Escriba el Valor de X1: '))
    fx1 = float(input('Escriba el Valor de f(x1): '))
    x2 = float(input('Escriba el Valor de X2: '))
    fx2 = float(input('Escriba el Valor de f(x2): '))
    x = float(input('Escriba el Valor de X: '))

    fx = ((x-x1)/(x0-x1)) * ((x-x2)/(x0-x2))*fx0 + ((x-x0)/(x1-x0)) * ((x-x2)/(x1-x2))*fx1 + ((x-x0)/(x2-x0)) * ((x-x1)/(x2-x1))*fx2

    return fx

def error(vverdadero, vaprox):
    erabs = vverdadero - vaprox
    errel = (erabs/vverdadero) * 100
    return erabs, errel

def main():

    a = int(input('Escriba 1 para interpolacion lineal 2 para interpolacion cuadratica: '))

    if a == 1:
        fx = inter1()
        print('El valor de f(x) es: ' + fx)
        erabs, errel = error()

    if a == 2:
        fx = inter2()
        print('El valor de f(x) es: ' + fx)




if __name__ == '__main__':
    main()

