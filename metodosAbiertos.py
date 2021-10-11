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
    df= Funcion(f.derivada())
    f0= f.evaluar(f.getF(),x0)
    f1= df.evaluar(df.getF(),x0)
    while(cont<Nmax and error>tol):
        xn = x0 - (f0)/(f1)
        error = abs(xn-x0)
        cont = cont + 1
        x0 = xn
        f0= f.evaluar(f.getF(),x0)
        f1= df.evaluar(df.getF(),x0)
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
    df=Funcion(f.derivada())
    df2 = Funcion(df.derivada())
    factual= f.evaluar(f.getF(),x0)
    fderivada = df.evaluar(df.getF(),x0)
    fderivada2 =df2.evaluar(df2.getF(),x0)
    while(cont<Nmax and error>tol):
        xn = x0 - ((factual*fderivada)/((fderivada*fderivada)-(factual*fderivada2)))
        error = abs(xn-x0)
        cont = cont + 1
        x0 = xn
        factual= f.evaluar(f.getF(),x0)
        fderivada = df.evaluar(df.getF(),x0)
        fderivada2 =df2.evaluar(df2.getF(),x0)
    return [xn,error,cont]
print("introduce la funcion en terminos de x ")
expr = input()
x = Funcion(expr)
a = float(input("introduce el intervalo inicial "))
b= float(input("introduce el intervalo final "))
tol= float(input("introduce la tolerancia "))
Nmax = float(input("introduce las iteraciones maximas "))
resul = newton(x,a,tol,Nmax)
"""resul= multiplesRaices(x,a,tol,Nmax)"""
print(resul)