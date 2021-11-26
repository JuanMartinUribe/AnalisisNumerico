from Funcion import *
from pandas import DataFrame
from rich.console import Console

console = Console()


def read_matrix(m_size):
    lista = [list(map(float, input().split())) for x in range(m_size)]
    if False in [bool(i) for i in lista]:
        return None
    return lista


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
    a = float(input("introduce el intervalo inicial "))

    tol = float(input("introduce la tolerancia "))
    Nmax = float(input("introduce las iteraciones maximas "))

    print('=' * 50)
    console.print(DataFrame(punto_fijo(x, a, tol, Nmax)))


def punto_fijo(g, x0, tol, Nmax):
    cont = 0
    error = tol + 1
    while cont < Nmax and error > tol:
        xn = g.evaluar(g.getF(), x0)
        error = abs(xn - x0)
        cont = cont + 1
        x0 = xn
    if E > tol:
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
    console.print(DataFrame(newton(x, a, tol, Nmax)))


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
    if E > tol:
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
    a = float(input("introduce el intervalo inicial "))
    b = float(input("introduce el intervalo final "))

    tol = float(input("introduce la tolerancia "))
    Nmax = float(input("introduce las iteraciones maximas "))

    print('=' * 50)
    console.print(DataFrame(secante(x, a, b, tol, Nmax)))


def secante(f, x0, x1, tol, Nmax):
    cont = 0
    error = tol + 1
    while cont < Nmax and error > tol:
        xn = x1 - f.evaluar(f.getF(), x1) * (x1 - x0) / ((f.evaluar(f.getF(), x1)) - (f.evaluar(f.getF(), x0)))
        error = abs(xn - x1)
        cont = cont + 1
        x0 = x1
        x1 = xn
    if E > tol:
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
    a = float(input("introduce el intervalo inicial "))

    tol = float(input("introduce la tolerancia "))
    Nmax = float(input("introduce las iteraciones maximas "))

    print('=' * 50)
    console.print(DataFrame(multiples_raices(x, a, tol, Nmax)))


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
    if E > tol:
        cadena = "Hay una raiz que no cumple con esa tolerancia en el x = " + str(xn) + " en el intervalo =  " + str(
            cont) + " con error = " + str(error)
    else:
        cadena = "Hay una raiz que cumple con esa tolerancia en el x = " + str(xn) + " en el intervalo =  " + str(
            cont) + " con error = " + str(error)
    return cadena
