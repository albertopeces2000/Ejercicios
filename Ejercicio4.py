
print('Este programa es capaz de operar con fracciones de este tipo ==> a/b y c/d.')
print('Las operaciones seguirán el siguiente orden a la hora de operar. 1º a/b y 2º c/d')
a = float(input('Introduce el valor de a:'))
b = float(input('Introduce el valor de b:'))
c = float(input('Introduce el valor de c:'))
d = float(input('Introduce el valor de d:'))
fraccion_1 = a/b
fraccion_2 = c/d
class Fraccion:
    def __init__(self,fraccion_1,fraccion_2):
        self.fraccion_1 = fraccion_1
        self.fraccion_2 = fraccion_2
    def suma(self):
        return self.fraccion_1 + self.fraccion_2
    def resta(self):
        return self.fraccion_1 - self.fraccion_2
    def multiplicacion(self):
        return self.fraccion_1 * self.fraccion_2
    def division(self):
        return self.fraccion_1 / self.fraccion_2

datos = Fraccion(fraccion_1,fraccion_2)
print('\n','Su suma es:',datos.suma(),'\n','Su diferencia es:',datos.resta(),'\n','Su producto es:',datos.multiplicacion(),'\n','Su division es:',datos.division())
