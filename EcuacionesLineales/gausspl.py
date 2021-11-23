from numpy import *
from sustRegr import *
import numpy
a = [[2., -1, -3, 2],
     [5, -10, 2, -6],
     [5, -9, 15, -6],
     [2, 1, -1, 10]
     ]
b= [[4],[3],[2],[1]]
def gausspl(A,b):
    
    Ma=numpy.append(A,b, axis=1)
    n=len(Ma)
    for k in range(0,n-1,1):
        for i in range(k+1,n,1):
            if Ma[k][k]!=0:
                mult = Ma[i][k]/Ma[k][k]
            else:
                return("pivote en 0")
            for j in range(k,n+1,1):
                Ma[i][j]=Ma[i][j] - (mult*Ma[k][j])
                
    
    
    x=susRegr(Ma)
    return x
    
z=gausspl(a,b)
print(z)
    