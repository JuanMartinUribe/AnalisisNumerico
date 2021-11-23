from numpy import *
from sustRegr import *
import numpy
a = [[-7., 2, -3, 4],
     [5, -1, 14, -1],
     [1, 9, -7, 5],
     [-12, 13, -8, -4]
     ]
b= [[-12],[13],[31],[-32]]
def gausspar(A,b):
    Ma=numpy.append(A,b, axis=1)
    n=len(Ma)
    for k in range(0,n-1,1):
        columna = abs(Ma[k:,k])
        dondeMax=numpy.argmax(columna)
        if (dondeMax !=0):
            temporal = numpy.copy(Ma[k,:])
            Ma[k,:]=Ma[dondeMax+k,:]
            Ma[dondeMax+k,:] = temporal
        for i in range(k+1,n,1):
                
            if Ma[k][k]!=0:
                    mult = Ma[i][k]/Ma[k][k]
            else:
                return("pivote en 0")
            for j in range(k,n+1,1):
                    Ma[i][j]=Ma[i][j] - (mult*Ma[k][j])         
    print(Ma)
    x=susRegr(Ma)
    return x
z=gausspar(a,b)
print(z)