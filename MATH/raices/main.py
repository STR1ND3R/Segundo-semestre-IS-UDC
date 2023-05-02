import gui

def sec(a,b,c,x0,x1,n):
    x0: float = x0
    x1: float = x1
    fx0: float = a*x0**2+b*x0+c
    fx1: float = a*x1**2+b*x1+c
    for i in range(n):
        x2: float = x1-(fx1*(x0 - x1))/(fx0-fx1)
        fx2: float = a*x2**2+b*x2+c

        print(x2)
        x0 = x1
        x1 = x2
        fx0: float = a*x0**2+b*x0+c
        fx1: float = a*x1**2+b*x1+c
    
    return x2

def newr(a,b,c,x0,x1,n):
    x0: float = (x0+x1)/2

    fx0: float = a*x0**2+b*x0+c
    fpx0: float = (a*2)*x0+b
    for i in range(n):
        x2: float = x0-(fx0/fpx0)

        print(x2)
        x0 = x2
        fx0: float = a*x0**2+b*x0+c
        fpx0: float = (a*2)*x0+b
    
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
    #sec(a,b,c,x0,x1,n)
    print(sec(1,-3,-4,5,7,3))
    #newr(a,b,c,x0,x1,n)
    print(newr(-3,8,-1,2,3,2))
if __name__ == '__main__':
    main()