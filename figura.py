import math
lado = int(input('Introduce el lado del cuadrado:'))
class Figura():
    def perimetro(self):
        return 'No tiene perímetro.'
    def area(self):
        return 'No tiene área.'


class Square(Figura):
    def __init__(self):
        self.lado = lado

    def get_perimetro(self):
        return self.lado * 4
    def get_area(self):
        return self.lado ** 2
area = Square()


print('CUADRADO ==> El area es:',area.get_area(),'y su perimetro:',area.get_perimetro())

base = int(input('Introduce la base del rectángulo:'))

altura = int(input('Introduce la altura del rectángulo:'))
class Rectangle(Figura):
    def __init__(self):
        self.base = base
        self.altura = altura
    def get_perimetro(self):
        return 2*self.base + 2*self.altura
    def get_area(self):
        return self.base * self.altura
datos = Rectangle()
print('RECTÁNGULO ==> El area es:',datos.get_area(),'y su perímetro:',datos.get_perimetro())

radio = int(input('Introduce el valor del radio:'))
class Circle(Figura):
    def __init__(self):
        self.radio = radio

    def get_perimetro(self):
        return self.radio *2*math.pi
    def get_area(self):
        return math.pi*(self.radio**2)
datos_2 = Circle()
print('CÍRCULO ==> El area es:',datos_2.get_area(),'y su perimetro:',datos_2.get_perimetro())

eje_menor = int(input('Introduce el semieje menor de la elipse:'))
eje_mayor = int(input('Introduce el semieje mayor de la elipse:'))

class Elipse(Figura):
    def __init__(self):
        self.eje_menor = eje_menor
        self.eje_mayor = eje_mayor

    def get_perimetro(self):
        return 2*math.pi*(((self.eje_mayor**2 + self.eje_menor**2)*(1/2))**(1/2))
    def get_area(self):
        return self.eje_mayor * self.eje_menor * math.pi
datos_3 = Elipse()
print('ELIPSE ==> El area es:',datos_3.get_area(),'y su perimetro:',datos_3.get_perimetro())
