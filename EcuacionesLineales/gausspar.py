from .sustRegr import sust_regr
import numpy
from pandas import DataFrame
from rich.console import Console

console = Console()


def read_matrix(m_size):
    return [list(map(int, input().split())) for x in range(m_size)]


def gausspar_menu():
    console.print('Ingrese los parámetros solicitados', style='bold green on black')
    n = int(input(f'Ingresar tamaño de matriz: '))
    console.print(f'Ingresar matriz A separado por espacios y saltos de línea')
    a = read_matrix(n)
    console.print(f'Ingresar Vector B separado por espacios y saltos de línea')
    b = read_matrix(n)
    print('=' * 50)
    console.print(DataFrame(gausspar(a, b)))


a = [[-7., 2, -3, 4],
     [5, -1, 14, -1],
     [1, 9, -7, 5],
     [-12, 13, -8, -4]
     ]
b = [[-12], [13], [31], [-32]]


def gausspar(a, b):
    Ma = numpy.append(a, b, axis=1)
    n = len(Ma)
    for k in range(0, n - 1, 1):
        columna = abs(Ma[k:, k])
        dondeMax = numpy.argmax(columna)
        if dondeMax != 0:
            temporal = numpy.copy(Ma[k, :])
            Ma[k, :] = Ma[dondeMax + k, :]
            Ma[dondeMax + k, :] = temporal
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
z = gausspar(a, b)
print(z)
'''
