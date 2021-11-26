import numpy as np
from rich.console import Console

console = Console()


def vandermonde_menu():
    console.print('Ingrese los parámetros solicitados', style='bold green on black')
    n = int(input(f'Ingresar n: '))
    x = list(map(float, input(f'Ingresar vector x separado por espacios: ').split()))
    y = list(map(float, input(f'Ingresar vector y separado por espacios: ').split()))
    console.print(Vandermonde(n, x, y))


def Vandermonde(n, x, y):
    points = zip(x, y)
    sorted_points = sorted(points)
    new_xs = [point[0] for point in sorted_points]
    new_ys = [point[1] for point in sorted_points]
    xn = np.array(new_xs)
    yn = np.array([new_ys]).T
    print()
    console.print("Los x en orden son: ", style= "bold magenta")
    console.print(xn)
    print()
    console.print("Los y en orden son: ", style= "bold magenta")
    console.print(yn)
    A = np.vander(xn)
    Ainv = np.linalg.inv(A)
    a = np.dot(Ainv, yn)
    print()
    console.print("Dot= ", style= "bold magenta")
    console.print(a)
    print()
    str1 = ""
    print()
    for i in range(n):
        str1 = str1 + "a" + str(n - 1 - i) + " = " + str(a[i]) + " "
    return str1
