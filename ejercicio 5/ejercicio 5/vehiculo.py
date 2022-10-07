class Vehiculo():

 

    def __init__(self, color, ruedas):

        self.color = color
        self.ruedas = ruedas
        

 

    def __str__(self):

        return "color {}, {} ruedas".format( self.color, self.ruedas )

 

 

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):

        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

 

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

 
class Camioneta(Vehiculo):

    def __init__(self, color, ruedas, carga):

        Vehiculo.__init__(self, color, ruedas)
        self.carga = carga

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} kg".format(self.carga)


class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):

        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return Vehiculo.__str__(self) + ", el tipo de bicicle es {} .".format(self.tipo)




class Motocicleta(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


c = Coche("azul", 4, 150, 1200)

ca= Camioneta("gris", 4, 3000)

b= Bicicleta("roja", 2, "urbana")

m = Motocicleta("roja", 2, 80, 800)

print(c)
print(ca)
print(b)
print(m)

