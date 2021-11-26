import numpy as np


def susregr(a, b):
    x = np.zeros((len(a), 1))

    for i in range(len(a) - 1, -1, -1):
        acum = 0
        for j in range(len(a) - 1, i, -1):
            acum += a[i][j] * x[j][0]
        x[i][0] = (b[i][0] - acum) / a[i][i]
    return x
