import unittest
import vehiculo


class Test(unittest.TestCase):

    def setUp(self):
        vehiculo.Vehiculo.lista = [
        vehiculo.Coche("azul", 4, 150, 1200),
        vehiculo.Camioneta("gris", 4, 3000),
        vehiculo.Bicicleta("roja", 2, "urbana"),
        vehiculo.Motocicleta("roja", 2, 80, 800)
        ]

    





if __name__ == "__main__":
    unittest.main()
