class Producto():
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

    def __str__(self):
        return "El código de {} es {}, su precio es {} y el tipo es {}".format(self.nombre, self.codigo, self.precio, self.tipo)


p= Producto(231, "leche", 2, "lacteos")
print(p)