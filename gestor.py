import json
import os
from modelo import Producto


class GestorProductos:
    """
    Clase que gestiona todas las operaciones CRUD de los productos.
    """

    def __init__(self, archivo="data.json"):
        self.archivo = archivo
        self.productos = self.cargar_datos()

    def cargar_datos(self):
        """
        Carga los productos desde el archivo JSON.
        """
        if not os.path.exists(self.archivo):
            return []

        with open(self.archivo, "r", encoding="utf-8") as f:
            try:
                datos = json.load(f)
                return [Producto.from_dict(p) for p in datos]
            except json.JSONDecodeError:
                return []

    def guardar_datos(self):
        """
        Guarda los productos en el archivo JSON.
        """
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.productos], f, indent=4)

    def generar_id(self):
        """
        Genera un ID automático.
        """
        if not self.productos:
            return 1
        return max(p.id_producto for p in self.productos) + 1

    def agregar_producto(self, nombre, precio, cantidad):
        """
        Agrega un nuevo producto.
        """
        nuevo_producto = Producto(
            self.generar_id(),
            nombre,
            precio,
            cantidad
        )
        self.productos.append(nuevo_producto)
        self.guardar_datos()
        return nuevo_producto

    def listar_productos(self):
        """
        Retorna la lista de productos.
        """
        return self.productos

    def buscar_producto(self, id_producto):
        """
        Busca un producto por ID.
        """
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    def actualizar_producto(self, id_producto, nombre, precio, cantidad):
        """
        Actualiza un producto existente.
        """
        producto = self.buscar_producto(id_producto)
        if producto:
            producto.nombre = nombre
            producto.precio = precio
            producto.cantidad = cantidad
            self.guardar_datos()
            return True
        return False

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por ID.
        """
        producto = self.buscar_producto(id_producto)
        if producto:
            self.productos.remove(producto)
            self.guardar_datos()
            return True
        return False