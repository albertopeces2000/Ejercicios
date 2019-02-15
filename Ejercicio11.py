print('Este programa va a proporcionarnos datos académicos de un estudiante al cual tenemos que introducir unas notas para comprobar si ha aprobado o no.')
nombre = input('Introduce el nombre el alumno:')
expediente = int(input('Introduce el número de expediente de dicho alumno:'))
contador = 1
datos_alumno = [nombre,expediente]

while contador <=3:
    notas = float(input('Introduzca una nota:'))
    datos_alumno.append(notas)
    contador = contador + 1

print(datos_alumno)
nota1 = datos_alumno[2]
nota2 = datos_alumno[3]
nota3 = datos_alumno[4]
class Evaluacion():
    def __init__(self,nombre,expediente,nota1,nota2,nota3):
        self.nombre = datos_alumno[0]
        self.expediente = datos_alumno[1]
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
#    def nombre(self):
#        return self.nombre
#    def expediente(self):
#        return self.expediente
    def nota_final(self):
        return (self.nota1 + self.nota2 + self.nota3)*(1/3)
    def media(self):
        nota_media = (self.nota1 + self.nota2 + self.nota3)*(1/3)
        if nota_media >= 4.8:
            return 'Enhorabuena, has aprobado.'
        else:
            return 'Vas a Junio con toda la asignatura.'
datos = Evaluacion(datos_alumno[0],datos_alumno[1],nota1,nota2,nota3)
print('\n','Nombre de estudiante:',datos.nombre,'\n','Número de expediente:',datos.expediente,'\n','Su nota final es:',datos.nota_final(),'\n','Y por último, pero no menos importante su evaluación es:',datos.media())
