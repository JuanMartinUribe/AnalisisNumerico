from sympy import *
x = Symbol('x')
class Funcion:
    f=0;
    def __init__(self,f):
        self.f = f
    def getF(self):
        return self.f
    def setF(self,f):
        self.f = f

    def evaluar(self,expr,a):
        y=sympify(expr,evaluate=True).subs(x,a)
        return y

"""print("introduce la funcion en terminos de x ")
expr = input()
f = Funcion(expr)

print("introduce el valor a evaluar")
a = input()
print(f.evaluar(f.getF(),a))"""