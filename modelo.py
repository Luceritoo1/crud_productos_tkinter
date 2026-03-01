class Producto:

    def __init__(self, id_producto, nombre, precio, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            data["id_producto"],
            data["nombre"],
            data["precio"],
            data["cantidad"]
        )