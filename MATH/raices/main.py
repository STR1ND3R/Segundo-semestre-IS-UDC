


def sec(a,b,c,x0,x1,n):
    x0 = x0
    x1 = x1
    fx0 = a*x0**2+b*x0+c
    fx1 = a*x1**2+b*x1+c
    x2 = (fx1(x0 - x1))/(fx0-fx1)
    fx2 = a*x2**2+b*x2+c
    for i in range(n):
        x0 = x1
        x1 = x2
    
    return x2








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
    print(sec(2,3,1,1,3,15))
if __name__ == '__main__':
    main()