import numpy as np
import sys

def gaussTot(A,b):
    # Se crea un numpy array de n*(n+1) para guardar la matriz aumentada
    Ma=np.append(A,b, axis=1)
    n=len(Ma)
    a = np.zeros((n,n+1))

    # Creando un vector donde se almacenará la solución de la matriz
    x = np.zeros(n)
    x1 = np.zeros(n)
    c0= 0
    for i in range(n):
        x1[i] = c0
        c0 = c0+1
    # Ingresar los valores de los coeficientes de la matriz aumentad
    cont = 0
    for i in range(n):
        for j in range(n+1):
            a[i][j] = A[cont]
            cont = cont + 1
    #Gauss
    c = 0
    c1 = 0
    for k in range(0,n-1):
        Max = 0
        columnaN = k
        filaN = k
        for j in range(k,n):
            for i in range(k,n):
                if k != j or k != i:
                    if abs(a[i][j]) > abs(a[k][k]):
                        if abs(a[i][j]) > Max:
                            columnaN = j
                            filaN = i
                            Max = abs(a[i][j])
        if (columnaN != k):
            a[:, [columnaN, k]] = a[:, [k, columnaN]] 
            x1[k], x1[columnaN] = x1[columnaN], x1[k]
        if (filaN != k):
            c = c+1
            a[[k,filaN]] = a[[filaN,k]]
            print("Transformación: "+str(c))
            print(a)

        for i in range(k+1,n):
            Multiplicador = a[i][k]/a[k][k]
            for j in range(k,n+1):
                a[i][j] = a[i][j] - Multiplicador*a[k][j]
        c1=c1+1
        print("Reducción: "+str(c1))
        print(a)

    print("\n matriz reducida aumentada reducida")
    print(a)
    #Solución
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum = sum + a[i][j]*x[j]
        x[i] = (a[i][n] - sum)/a[i][i]

    str1 = '\nLa solución es: '
    for i in range(n):
        str1 = str1 +' X%d = %0.2f' %(x1[i],x[i])
    return(str1)
a = [[-7., 2, -3, 4],
     [5, -1, 14, -1],
     [1, 9, -7, 5],
     [-12, 13, -8, -4]
     ]
b= [[-12],[13],[31],[-32]]
z=gaussTot(a,b)
print(z)