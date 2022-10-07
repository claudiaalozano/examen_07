import csv

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        
        return "El alumno {}".format(self.nombre) + " ha obtenido la siguiente calificación {}".format(self.nota) 

class calificacion:
    def __init__(self):
        
        self.lista1 = ["Maria", 3]
        self.lista2 = ["Juan", 9]
        

        if self.lista1[1]>=5 and self.lista2[1] >=5:
            return "Han aprobado {}".format(self.lista1[0]) + " y {}".format(self.lista2[0])

        if self.lista1[1] < 5 and self.lista2[1]>= 5:
            return "Ha aprobado {}".format(self.lista2[0]) + " y ha suspendido {}".format(self.lista1[0])

        if self.lista1[1]>= 5 and self.lista2[1]< 5:
            return "Ha aprobado {}".format(self.lista1[0]) + " y ha suspendido {}".format(self.lista2[0])

        else:
            return "Han suspendido {}".format(self.lista1[0]) + " y  {}".format(self.lista2[0]) 
    


al = Alumno("Maria", 3)
al1 = Alumno("Juan", 9)
al2 = calificacion()
al3 = calificacion()
print(al)
print(al1)
print(al2)
print(al3)