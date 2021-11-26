import numpy


def sust_regr(A):
    n = len(A)
    cadena = ""
    x = numpy.zeros(n, dtype=float)

    for i in range(n - 1, -1, -1):
        sum = 0
        for p in range(i + 1, n, 1):
            sum = sum + A[i][p] * x[p]

        x[i] = (A[i][n] - sum) / A[i][i]

    for i in range(0, len(x), 1):
        cadena = cadena + "x" + str(i) + "= " + str(x[i]) + " "

    return cadena
