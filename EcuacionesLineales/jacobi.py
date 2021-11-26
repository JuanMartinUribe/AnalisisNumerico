import numpy
from numpy.linalg import inv, eigvals, norm

from pandas import DataFrame
from rich.console import Console

console = Console()


def read_matrix(m_size):
    lista = [list(map(float, input().split())) for x in range(m_size)]
    if False in [bool(i) for i in lista]:
        return None
    return lista


def jacobi_menu():
    console.print('Ingrese los parámetros solicitados', style='bold green on black')
    n = int(input(f'Ingresar tamaño de matriz: '))
    console.print(f'Ingresar matriz A separado por espacios y saltos de línea')
    a = read_matrix(n)
    console.print(f'Ingresar Vector B separado por espacios y saltos de línea')
    b = read_matrix(n)
    console.print(f'Ingresar Vector x0 separado por espacios y saltos de línea (Def None)')
    x0 = read_matrix(n)
    console.print(f'Ingresar Max iteraciones:', end=' ')
    max_iter = int(input())
    console.print(f'Ingresar tolerancia:', end=' ')
    tolerancia = float(input())

    print('=' * 50)
    console.print(jacobi(a, b, max_iter, x0, tolerancia))


def jacobi(a, b, n, x0=None, tol=None):
    l = -numpy.tril(a, -1)
    u = -numpy.triu(a, 1)
    d = a + l + u
    t = numpy.matmul(inv(d), l + u)
    c = numpy.matmul(inv(d), b)
    if max(abs(eigvals(t))) > 1:
        print("No converge")
        return 0
    if x0 is None:
        x0 = []
        for i in range(len(a)):
            x0.append([0])
    if tol is None:
        tol = 10 ** -5
    xn = numpy.matmul(t, x0) + c
    cont = 0
    e = 1000
    while (x0 != xn).all() and cont < n and e > tol:
        x0 = xn
        xn = numpy.matmul(t, x0) + c
        cont += 1
        e = norm(x0 - xn)
    return xn, cont, e


a = [[45, 13, -4, 8],
     [-5, -28, 4, -14],
     [9, 15, 63, -7],
     [2, 3, -8, -42]
     ]
b = [[-25],
     [82],
     [75],
     [-43]]

'''
print(jacobi(a, b, 100, None, None))
'''
