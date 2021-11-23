import numpy as np
import sys
def Vandermonde(n,x,y):
    points = zip(x,y)
    sorted_points = sorted(points)
    new_xs = [point[0] for point in sorted_points]
    new_ys = [point[1] for point in sorted_points]
    xn = np.array(new_xs)
    yn = np.array([new_ys]).T
    print("Los x en orden son: ")
    print(xn)
    print("Los y en orden son: ")
    print(yn)
    A = np.vander(xn)
    Ainv = np.linalg.inv(A)
    a = np.dot(Ainv,yn)
    print(a)
    str1 = ""
    for i in range(n):
        str1 = str1 + "a" + str(n-1-i) + " = " + str(a[i])
    return(str1)