lista_nombres = ['Alberto','Maria','Estela','Celia','Carla','Alicia','Ainhoa']
lista_datos = [[500,100,1400],[153,345,974],[298,8974,4540],[123,3490, 30],[2343,34,504],[1609,56,500],[1056,98, 950]]
dict_datos = dict(zip(lista_nombres,lista_datos))
print(lista_nombres)

nombre = input('Introduce el nombre de un trabajador/a:')
class Cuenta():
    def __init__(self,ingreso, reintegro, transferencia): #transferencia):
        #self.nombre = nombre
        self.ingreso = ingreso
        self.reintegro = reintegro
        self.transferencia = transferencia
    #def get_nombre(self):
    #    return self.nombre
    def get_ingreso(self):
        return self.ingreso
    def get_reintegro(self):
        return self.reintegro
    def get_transferencia(self):
        return self.transferencia
info = Cuenta(dict_datos[nombre][0],dict_datos[nombre][1],dict_datos[nombre][1])
print('El/la trabajador/a:',nombre,'==> tiene como ingresos:',info.get_ingreso(),'euros, un reintegro de:',info.get_reintegro(),'euros y además, una transferencia de:',info.get_transferencia(),'euros.')
