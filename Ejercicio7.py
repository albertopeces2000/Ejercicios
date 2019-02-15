lista_nombres = ['Alberto','Maria','Estela','Celia','Carla','Alicia','Ainhoa']
lista_datos = [[500,100,1400],[153,12,974],[298,0,4540],[123,234, 30],[2343,98,504],[1609,0,500],[1056,0, 950]]
trabajadores = dict(zip(lista_nombres,lista_datos))
lista_aux = []
print(lista_nombres)
nombre = input('Introduce el nombre de un trabajador:')
class Empleado():
    def __init__(self,nombre,sueldo,dinero_de_mas):
        self.nombre = nombre
        self.sueldo = sueldo
        self.dinero_de_mas = dinero_de_mas
    def info_empleado(self):
        return self.nombre ,self.sueldo, self.dinero_de_mas


info_1 = Empleado(nombre,trabajadores[nombre][0],trabajadores[nombre][1])
lista_aux.append(info_1)
#info_2 = Empleado(trabajadores)
#info_3 = Empleado(trabajadores)

class Ejecutivo(Empleado):
    def __init__(self,ejecutivo):
        self.ejecutivo = ejecutivo
    def info_ejecutivo(self):
        return self.ejecutivo
new_info = Ejecutivo(lista_aux[0])
print('Nombre:',nombre,'Sueldo:',new_info.ejecutivo.sueldo,'Aumento:',new_info.ejecutivo.dinero_de_mas)

#class Empresa():


#Tendremos clases de diferentes tipos, una clase es parecida a la otra casi identica.
#El directivo es lo msmo que un empleado por ejemploself.#Primero defino la clase empleado y solo programo la diferencia y a eso le llamo...
#Concepto de Herencia.

#Toma productos todos los productos tienen un nombre y un precioself.
#Algunos productos son medicamentosself.Los medicamentos tienen además una composición y un porcentaje.
#3 clases con herencia
