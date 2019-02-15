lista_libros = ['la bella y la bestia','blancanieves','el mago de oz','cenicienta','bella durmiente','aladin','ariel']
lista_datos = [['Sí','No'],['Sí','No'],['Sí','Sí'],['No','Sí'],['No','No'],['Sí','No'],['Sí','No']]
dict_datos = dict(zip(lista_libros,lista_datos))

print(lista_libros)
dame_info = input('Introduce el nombre de un libro:')

class Libro():
    def __init__(self,dame_info, prestamo, devolucion ):
        self.dame_info = dame_info
        self.prestamo = prestamo
        self.devolucion = devolucion
    def info(self):
        return self.dame_info,self.prestamo,self.devolucion

info = Libro(dame_info,dict_datos[dame_info][0],dict_datos[dame_info][1])
print('Usted ha escogido el libro:',info.dame_info,'\n','Posibilidad de préstamo:',info.prestamo,'\n','El libro ha sido devuelto:',info.devolucion)
