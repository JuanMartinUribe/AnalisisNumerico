import numpy as np
from susprog import susprog
from susregr import susregr


def lu(a, b):
    l = np.identity(len(a))
    u = np.zeros((len(a), len(a)))

    a = np.array(a)
    b = np.array(b)
    for j in range(len(a) - 1):
        for i in range(j + 1, len(a)):
            mult = a[i][j] / a[j][j]
            l[i][j] = mult
            for k in range(j, len(a)):
                a[i][k] = a[i][k] - mult * a[j][k]

    u = a
    z = susprog(l, b)
    x = susregr(u, z)

    return x


a = [[2, -1, -3, 2],
     [5, -10, 2, -6],
     [5, -9, 15, -6],
     [2, 1, -1, 10]]
b = [[4.], [3.], [2.], [1.]]

# a = [[4,3,-2,-7],[3 ,12,8,-3],[2,3,-9,3],[1,-2,-5,6]]
# b = [[20.],[18.],[31.],[12.]]
for i in range(len(a)):
    for j in range(len(a)):
        a[i][j] = float(a[i][j])

print(lu(a, b))
