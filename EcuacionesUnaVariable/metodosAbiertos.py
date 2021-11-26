from .Funcion import *
from pandas import DataFrame
from rich.console import Console

console = Console()


"""print()
expr = input("introduce la funcion en terminos de x ")
x = Funcion(expr)
a = float(input("introduce el intervalo inicial "))

tol= float(input("introduce la tolerancia "))
Nmax = float(input("introduce las iteraciones maximas "))
resul = newton(x,a,tol,Nmax)
resul= multiplesRaices(x,a,tol,Nmax)
print(resul)"""


def punto_fijo_menu():
    console.print('Ingrese los parámetros solicitados', style='bold green on black')
    expr = input("introduce la funcion en terminos de x ")
    x = Funcion(expr)
    a = float(input("introduce el punto incial "))

    tol = float(input("introduce la tolerancia "))
    Nmax = float(input("introduce las iteraciones maximas "))

    print('=' * 50)
    console.print(punto_fijo(x, a, tol, Nmax))


def punto_fijo(g, x0, tol, Nmax):
    cont = 0
    error = tol + 1
    while cont < Nmax and error > tol:
        xn = g.evaluar(g.getF(), x0)
        error = abs(xn - x0)
        cont = cont + 1
        x0 = xn
    if error > tol:
        cadena = "Hay una raiz que no cumple con esa tolerancia en el x = " + str(xn) + " en el intervalo =  " + str(
            cont) + " con error = " + str(error)
    else:
        cadena = "Hay una raiz que cumple con esa tolerancia en el x = " + str(xn) + " en el intervalo =  " + str(
            cont) + " con error = " + str(error)
    return cadena


def newton_menu():
    console.print('Ingrese los parámetros solicitados', style='bold green on black')
    expr = input("introduce la funcion en terminos de x ")
    x = Funcion(expr)
    a = float(input("introduce el intervalo inicial "))

    tol = float(input("introduce la tolerancia "))
    Nmax = float(input("introduce las iteraciones maximas "))

    print('=' * 50)
    console.print(newton(x, a, tol, Nmax))


def newton(f, x0, tol, Nmax):
    cont = 0
    error = tol + 1
    df = Funcion(f.derivada())
    f0 = f.evaluar(f.getF(), x0)
    f1 = df.evaluar(df.getF(), x0)
    while cont < Nmax and error > tol:
        xn = x0 - f0 / f1
        error = abs(xn - x0)
        cont = cont + 1
        x0 = xn
        f0 = f.evaluar(f.getF(), x0)
        f1 = df.evaluar(df.getF(), x0)
    if error > tol:
        cadena = "Hay una raiz que no cumple con esa tolerancia en el x = " + str(xn) + " en el intervalo =  " + str(
            cont) + " con error = " + str(error)
    else:
        cadena = "Hay una raiz que cumple con esa tolerancia en el x = " + str(xn) + " en el intervalo =  " + str(
            cont) + " con error = " + str(error)
    return cadena


def secante_menu():
    console.print('Ingrese los parámetros solicitados', style='bold green on black')
    expr = input("introduce la funcion en terminos de x ")
    x = Funcion(expr)
    a = float(input("introduce el x0 "))
    b = float(input("introduce el x1 "))

    tol = float(input("introduce la tolerancia "))
    Nmax = float(input("introduce las iteraciones maximas "))

    print('=' * 50)
    console.print(secante(x, a, b, tol, Nmax))


def secante(f, x0, x1, tol, Nmax):
    cont = 0
    error = tol + 1
    while cont < Nmax and error > tol:
        xn = x1 - f.evaluar(f.getF(), x1) * (x1 - x0) / ((f.evaluar(f.getF(), x1)) - (f.evaluar(f.getF(), x0)))
        error = abs(xn - x1)
        cont = cont + 1
        x0 = x1
        x1 = xn
    if error > tol:
        cadena = "Hay una raiz que no cumple con esa tolerancia en el x = " + str(xn) + " en el intervalo =  " + str(
            cont) + " con error = " + str(error)
    else:
        cadena = "Hay una raiz que cumple con esa tolerancia en el x = " + str(xn) + " en el intervalo =  " + str(
            cont) + " con error = " + str(error)
    return cadena


def multiples_raices_menu():
    console.print('Ingrese los parámetros solicitados', style='bold green on black')
    expr = input("introduce la funcion en terminos de x ")
    x = Funcion(expr)
    a = float(input("introduce el x inicial "))

    tol = float(input("introduce la tolerancia "))
    Nmax = float(input("introduce las iteraciones maximas "))

    print('=' * 50)
    console.print(multiples_raices(x, a, tol, Nmax))


def multiples_raices(f, x0, tol, Nmax):
    cont = 0
    error = tol + 1
    df = Funcion(f.derivada())
    df2 = Funcion(df.derivada())
    factual = f.evaluar(f.getF(), x0)
    fderivada = df.evaluar(df.getF(), x0)
    fderivada2 = df2.evaluar(df2.getF(), x0)
    while cont < Nmax and error > tol:
        xn = x0 - ((factual * fderivada) / ((fderivada * fderivada) - (factual * fderivada2)))
        error = abs(xn - x0)
        cont = cont + 1
        x0 = xn
        factual = f.evaluar(f.getF(), x0)
        fderivada = df.evaluar(df.getF(), x0)
        fderivada2 = df2.evaluar(df2.getF(), x0)
    if error > tol:
        cadena = "Hay una raiz que no cumple con esa tolerancia en el x = " + str(xn) + " en el intervalo =  " + str(
            cont) + " con error = " + str(error)
    else:
        cadena = "Hay una raiz que cumple con esa tolerancia en el x = " + str(xn) + " en el intervalo =  " + str(
            cont) + " con error = " + str(error)
    return cadena
