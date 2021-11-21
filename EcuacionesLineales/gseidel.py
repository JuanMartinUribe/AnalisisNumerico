import numpy
from numpy.linalg import inv, eigvals, norm


def gseidel(a, b, n, x0=None, tol=None):
    l = -numpy.tril(a, -1)
    u = -numpy.triu(a, 1)
    d = a + l + u
    t = numpy.matmul(inv(d - l), u)
    c = numpy.matmul(inv(d - l), b)

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
    return xn,cont,e


a = [[45, 13, -4, 8],
     [-5, -28, 4, -14],
     [9, 15, 63, -7],
     [2, 3, -8, -42]
     ]
b = [[-25],
     [82],
     [75],
     [-43]]

print(gseidel(a, b, 100, None, None))
