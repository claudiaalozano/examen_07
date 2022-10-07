import csv

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        
        return "El alumno {}".format(self.nombre) + " ha obtenido la siguiente calificación {}".format(self.nota) 

class calificacion:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
        lista1 = ["Maria", 3]
        lista2 = ["Juan", 9]
        
        def aprobado(lista1, lista2):

            if lista1[1]>=5 and lista2[1] >=5:
                return "Han aprobado {}".format(lista1[0]) + " y {}".format(lista2[0])

            if lista1[1] < 5 and lista2[1]>= 5:
                return "Ha aprobado {}".format(lista2[0]) + " y ha suspendido {}".format(lista1[0])

            if lista1[1]>= 5 and lista2[1]< 5:
                return "Ha aprobado {}".format(lista1[0]) + " y ha suspendido {}".format(lista2[0])

            else:
                return "Han suspendido {}".format(lista1[0]) + " y  {}".format(lista2[0]) 
    


al = Alumno("Maria", 3)
al1 = Alumno("Juan", 9)
al2 = calificacion("Maria", 3)
al3 = calificacion("Juan", 9)
print(al)
print(al1)
print(al2)
print(al3)