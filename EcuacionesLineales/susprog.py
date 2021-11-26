def susprog(a, b):
    for i in range(1, len(a)):
        acum = 0.
        for j in range(i):
            acum += a[i][j] * b[j][0]
        b[i][0] = b[i][0] - acum

    return b
