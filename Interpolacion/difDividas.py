import numpy as np

from rich.console import Console

console = Console()


def difdivid_menu():
    console.print('Ingrese los parámetros solicitados', style='bold green on black')
    n = int(input(f'Ingresar n: '))
    x = list(map(float, input(f'Ingresar vector x separado por espacios: ').split()))
    y = list(map(float, input(f'Ingresar vector y separado por espacios: ').split()))
    difdivid(x, y)


def difdivid(Vx, Vy):
    output = list()

    X = np.array(Vx)
    n = X.size

    Y = np.array(Vy)

    D = np.zeros((n, n))

    D[:, 0] = Y.T
    for i in range(1, n):
        aux0 = D[i - 1:n, i - 1]
        aux = np.diff(aux0)
        aux2 = X[i:n] - X[0:n - i]
        D[i:n, i] = aux / aux2.T

    Coef = np.diag(D)

    output.append("D")
    output.append(D)
    output.append("Coef")
    output.append(Coef)

    for i in output:
        console.print(i)
        console.print("\n")
# difdivid([-1, 0, 3, 4],[15.5, 3, 8, 1])
