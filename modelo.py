class Producto:
    """
    Clase que representa un producto dentro del sistema.
    """

    def __init__(self, id_producto: int, nombre: str, precio: float, cantidad: int):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def to_dict(self):
        """
        Convierte el objeto Producto a diccionario para poder guardarlo en JSON.
        """
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Crea un objeto Producto a partir de un diccionario.
        """
        return Producto(
            data["id_producto"],
            data["nombre"],
            data["precio"],
            data["cantidad"]
        )