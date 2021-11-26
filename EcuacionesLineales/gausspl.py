from .sustRegr import sust_regr
import numpy
from pandas import DataFrame
from rich.console import Console

a = [[2., -1, -3, 2],
     [5, -10, 2, -6],
     [5, -9, 15, -6],
     [2, 1, -1, 10]
     ]
b = [[4], [3], [2], [1]]

console = Console()


def read_matrix(m_size):
    lista = [list(map(float, input().split())) for x in range(m_size)]
    if False in [bool(i) for i in lista]:
        return None
    return lista


def gausspl_menu():
    console.print('Ingrese los parámetros solicitados', style='bold green on black')
    n = int(input(f'Ingresar tamaño de matriz: '))
    console.print(f'Ingresar matriz A separado por espacios y saltos de línea')
    a = read_matrix(n)
    console.print(f'Ingresar Vector B separado por espacios y saltos de línea')
    b = read_matrix(n)
    print('=' * 50)
    console.print(DataFrame(gausspl(a, b)))


def gausspl(a, b):
    Ma = numpy.append(a, b, axis=1)
    n = len(Ma)
    for k in range(0, n - 1, 1):
        for i in range(k + 1, n, 1):
            if Ma[k][k] != 0:
                mult = Ma[i][k] / Ma[k][k]
            else:
                return "pivote en 0"
            for j in range(k, n + 1, 1):
                Ma[i][j] = Ma[i][j] - (mult * Ma[k][j])
    # print(Ma)
    x = sust_regr(Ma)
    return x


'''
z = gausspl(a, b)
print(z)
'''
