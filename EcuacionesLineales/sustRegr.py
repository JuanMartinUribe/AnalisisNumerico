from numpy import *
from numpy import *
import numpy
import sympy


def susRegr(A):
    n=len(A)
    
    x=numpy.zeros((n), dtype=float)
    
    for i in range(n-1,-1,-1):
        sum=0
        for p in range(i+1,n,1):
            
            sum=sum + A[i][p]*x[p]
            
        x[i]=(A[i][n]-sum)/A[i][i]
        
    return x
