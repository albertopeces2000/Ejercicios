
lista_productos = ['paracetamol','frenadol',"ibuprofeno","aspirina",'corticoides','insulina','amoxicilina','dalsi']
datos_productos = [[5,'povidona',500],[15,'dextrometorfano',5],[20,"codeína" , 0.40],[12,"serotonina", 0.30],[2,'serina',50],[16,'triptófano',5],[10,"mielina" , 0.50],[19,"hemoglobina", 0.20]]
lista_aux = []
dict_datos = dict(zip(lista_productos,datos_productos))
print(lista_productos)
nombre_1 = input('Dime el nombre del producto nº1:')
nombre_2 = input('Dime el nombre del producto nº2:')

class Productos():
    def info_productos(self):
        return 'No poseemos información de ningún producto en estos momentos.'


#info_1 = Productos(nombre,datos_productos[0][0])
class Medicamentos(Productos):

    def __init__(self,nombre,precio,compuesto,porcentaje):
        self.nombre = nombre
        self.precio = precio
        self.compuesto = compuesto
        self.porcentaje = porcentaje
    def info_medicamentos(self):
        return self.nombre,self.precio,self.compuesto,self.porcentaje

info_aux_1 = Medicamentos(nombre_1,dict_datos[nombre_1][0],dict_datos[nombre_1][1],dict_datos[nombre_1][2])
info_aux_2 = Medicamentos(nombre_2,dict_datos[nombre_2][0],dict_datos[nombre_2][1],dict_datos[nombre_2][2])
lista_aux.append(info_aux_1)
lista_aux.append(info_aux_2)
#Con la lista_aux guardo la class Medicamento en una lista con los valores que le correspondan a los nombres 1 y 2.

class Laboratorio(Medicamentos):
    def __init__(self,lab_1,lab_2):
        self.lab_1 = lab_1
        self.lab_2 = lab_2

    def info_labs(self):
        return self.lab_1,self.lab_2
info = Laboratorio(lista_aux[0],lista_aux[1])
print('Laboratorio Bayer [fármacos disponibles]. ==> Nombre del producto:',info.lab_1.nombre,'==>Precio del producto:',info.lab_1.precio,'==>Compuesto:',info.lab_1.compuesto,'==>Porcentaje [mg]:',info.lab_1.porcentaje)
print('Laboratorio Norwey [fármacos disponibles]. ==> Nombre del producto:',info.lab_2.nombre,'==>Precio del producto:',info.lab_2.precio,'==>Compuesto:',info.lab_2.compuesto,'==>Porcentaje [mg]:',info.lab_2.porcentaje)
