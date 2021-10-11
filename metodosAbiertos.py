from Funcion import *

def puntoFijo(g,x0,tol,Nmax):
    cont=0
    error=tol+1
    while(cont<Nmax and error>tol):
        xn = g.evaluar(g.getF(),x0)
        error = abs(xn-x0)
        cont = cont + 1
        x0 = xn
    return [xn,error,cont]
def newton(f,x0,tol,Nmax):
    cont=0
    error=tol+1
    df=f.derivada()
    while(cont<Nmax and error>tol):
        xn = x0 - (f.evaluar(f.getF(),x0))/(df.evaluar(f.getF(),x0))
        error = abs(xn-x0)
        cont = cont + 1
        x0 = xn
    return [xn,error,cont]
def secante(f,x0,x1,tol,Nmax):
    cont=0
    error=tol+1 
    while(cont<Nmax and error>tol):
        xn = x1 - f.evaluar(f.getF(),x1)*(x1-x0)/((f.evaluar(f.getF(),x1))-(f.evaluar(f.getF(),x0)))
        error = abs(xn-x1)
        cont = cont + 1
        x0 = x1
        x1 = xn
    return [xn,error,cont]
def multiplesRaices(f,x0,tol,Nmax):
    cont=0
    error=tol+1
    df=f.derivada()
    df2 = df.derivada()
    while(cont<Nmax and error>tol):
        xn = x0 - ((f.evaluar(f.getF(),x0))/(df.evaluar(f.getF(),x0))/((df.evaluar(f.getF(),x0))^2)-((f.evaluar(f.getF(),x0))*df2.evaluar(f.getF(),x0)))
        error = abs(xn-x0)
        cont = cont + 1
        x0 = xn
    return [xn,error,cont]
print("introduce la funcion en terminos de x ")
expr = input()
x = Funcion(expr)
a = float(input("introduce el intervalo inicial "))
b= float(input("introduce el intervalo final "))
tol= float(input("introduce la tolerancia "))
Nmax = float(input("introduce las iteraciones maximas "))
resul= puntoFijo(x,a,tol,Nmax)
print(resul)