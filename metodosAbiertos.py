from Funcion import *

def puntoFijo(g,x0,tol,Nmax):
    cont=0
    error=tol+1
    while(cont<Nmax and error>tol):
        xn = g.evaluar(x0)
        error = abs(xn-x0)
        cont = cont + 1
        x0 = xn
    return [xn,error,cont]
def newton(f,x0,tol,Nmax):
    cont=0
    error=tol+1
    df=f.derivada()
    while(cont<Nmax and error>tol):
        xn = x0 - (f.evaluar(x0))/(df.evaluar(x0))
        error = abs(xn-x0)
        cont = cont + 1
        x0 = xn
    return [xn,error,cont]
def secante(f,x0,x1,tol,Nmax):
    cont=0
    error=tol+1
    df=f.derivada()
    while(cont<Nmax and error>tol):
        xn = x1 - f.evaluar(x1)*(x1-x0)/((f.evaluar(x1))-(f.evaluar(x0)))
        error = abs(xn-x1)
        cont = cont + 1
        x0 = x1
        x1 = xn
    return [xn,error,cont]
def newton(f,x0,tol,Nmax):
    cont=0
    error=tol+1
    df=f.derivada()
    df2 = df.derivada()
    while(cont<Nmax and error>tol):
        xn = x0 - ((f.evaluar(x0))/(df.evaluar(x0))/((df.evaluar(x0))^2)-((f.evaluar(x0))*df2.evaluar(x0)))
        error = abs(xn-x0)
        cont = cont + 1
        x0 = xn
    return [xn,error,cont]
    