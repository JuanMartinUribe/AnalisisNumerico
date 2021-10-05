from Funcion import *
print("introduce la funcion en terminos de x ")
expr = input()
f = Funcion(expr)
def busquedas(a,b,Nmax):
    xant=a
    fant=f.evaluar(f.getF(),xant)
    xact=xant+b
    fact=f.evaluar(f.getF(),xact)
    for i in range(Nmax+1):
        if(fant*fact<0):
            break
        xant=xact
        fant=fact
        xact=xant+b
        fact=f.evaluar(f.getF(),xact)
    return [xant, xact, i]
def biseccion(a,b,tol,Nmax):
    m0=a
    m=b
    cont = 0
    fa=f.evaluar(f.getF(),a)
    fb=f.evaluar(f.getF(),b)
    E=1000
    if(fa*fb>0):
        print("la funcion no cambia de signo")
        return [-1]
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
    return [m,cont,E]

a = float(input("introduce el intervalo inicial "))
b= float(input("introduce el intervalo final "))
tol= float(input("introduce la tolerancia "))
Nmax = float(input("introduce las iteraciones maximas "))
resul= biseccion(a,b,tol,Nmax)
print(resul)