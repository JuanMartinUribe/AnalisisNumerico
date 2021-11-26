import numpy as np

def difdivid(Vx,Vy):
    output=list()

    X = np.array(Vx)
    n = X.size

    Y = np.array(Vy)

    D = np.zeros((n,n))

    D[:,0]=Y.T
    for i in range(1,n):
        aux0 = D[i-1:n,i-1]
        aux = np.diff(aux0)
        aux2 = X[i:n] - X[0:n-i]
        D[i:n,i] = aux/aux2.T  

    Coef = np.diag(D)
    
    output.append("D")
    output.append(D)
    output.append("Coef")
    output.append(Coef)
    
    for i in output:
        print(i)
        print("\n")
#difdivid([-1, 0, 3, 4],[15.5, 3, 8, 1])