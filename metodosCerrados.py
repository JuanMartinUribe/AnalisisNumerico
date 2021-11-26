from Funcion import *
print("introduce la funcion en terminos de x ")
expr = input()
x = Funcion(expr)
def busquedas(f,a,b,Nmax):
    xant=a
    fant=f.evaluar(f.getF(),xant)
    xact=xant+b
    fact=f.evaluar(f.getF(),xact)
    if(fant==0):
        return [xact]
    else:
        xact=xant+b
        cont = 0
        while((cont>=Nmax) and (fant*fact>0)):
            xant = xact
            xact = xant + b
            cont = cont  + 1
    if fact == 0:
            return [xact]
    elif (fact*fant<0):
        return [xant,xact]
    else: 
        return ["no se encontro"]

def biseccion(f,a,b,tol,Nmax):
    m0=a
    m=b
    cont = 0
    fa=f.evaluar(f.getF(),a)
    fb=f.evaluar(f.getF(),b)
    E=1000
    if(fa*fb>0):
        return ["la funcion no cambia de signo"]
    elif (fa*fb==0):
        return [a,b]
    while((E>tol) and (cont<Nmax)):
        m0=m
        m=(a+b)/2
        fa=f.evaluar(f.getF(),a)
        fm=f.evaluar(f.getF(),m)
        fb=f.evaluar(f.getF(),b)
        if((fa*fm)<0):
            b=m
        if((fm*fb)<0):
            a=m
        cont = cont + 1
        E=abs(m0-m)
    if(E>tol):
        cadena="Hay una raiz que no cumple con esa tolerancia en el x = " + str(m)+ " en el intervalo =  " + str(cont) + " con error = " + str(E)
    else:
        cadena="Hay una raiz que cumple con esa tolerancia en el x = " + str(m)+ " en el intervalo =  " + str(cont) + " con error = " + str(E)
    return cadena
def reglaFalsa(f,a,b,tol,Nmax):
    cadena=""
    m0=a
    m=b
    cont = 0
    fa=f.evaluar(f.getF(),a)
    fb=f.evaluar(f.getF(),b)
    E=1000
    if(fa*fb>0):
        return ["la funcion no cambia de signo"]
    elif (fa*fb==0):
        return [a,b]
    while((E>tol) and (cont<Nmax)):
        m0=m
        m=(fb*a-fa*b)/(fb-fa)
        fa=f.evaluar(f.getF(),a)
        fm=f.evaluar(f.getF(),m)
        fb=f.evaluar(f.getF(),b)
        if((fa*fm)<0):
            b=m
        if((fm*fb)<0):
            a=m
        cont = cont + 1
        E=abs(m0-m)
    cadena="Hay una raiz que cumple con esa tolerancia en el x = " + str(m)+ " en el intervalo =  " + str(cont) + " con error = " + str(E)
    return cadena
a = float(input("introduce el intervalo inicial "))
b= float(input("introduce el intervalo final "))
tol= float(input("introduce la tolerancia "))
Nmax = float(input("introduce las iteraciones maximas "))
resul= biseccion(x,a,b,tol,Nmax)
"""resul=busquedas(x,a,b,Nmax)"""
print(resul)