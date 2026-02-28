import json
import os
import csv
from modelo import Producto
from utils import registrar_info, registrar_error, ProductoError


class GestorProductos:

    def __init__(self, archivo="data.json"):
        self.archivo = archivo
        self.productos = self.cargar_datos()

    def cargar_datos(self):
        if not os.path.exists(self.archivo):
            return []

        with open(self.archivo, "r", encoding="utf-8") as f:
            try:
                datos = json.load(f)
                return [Producto.from_dict(p) for p in datos]
            except json.JSONDecodeError:
                registrar_error("Error al leer el archivo JSON.")
                return []

    def guardar_datos(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.productos], f, indent=4)

    def generar_id(self):
        if not self.productos:
            return 1
        return max(p.id_producto for p in self.productos) + 1

    def validar_producto(self, nombre, precio, cantidad):
        if not nombre or not nombre.strip():
            raise ProductoError("El nombre no puede estar vacío.")

        if precio < 0:
            raise ProductoError("El precio no puede ser negativo.")

        if cantidad < 0:
            raise ProductoError("La cantidad no puede ser negativa.")

    def agregar_producto(self, nombre, precio, cantidad):
        self.validar_producto(nombre, precio, cantidad)

        nuevo_producto = Producto(
            self.generar_id(),
            nombre,
            precio,
            cantidad
        )

        self.productos.append(nuevo_producto)
        self.guardar_datos()
        registrar_info(f"Producto agregado: {nombre}")
        return nuevo_producto

    def listar_productos(self):
        return self.productos

    def buscar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    def actualizar_producto(self, id_producto, nombre, precio, cantidad):
        self.validar_producto(nombre, precio, cantidad)

        producto = self.buscar_producto(id_producto)
        if producto:
            producto.nombre = nombre
            producto.precio = precio
            producto.cantidad = cantidad
            self.guardar_datos()
            registrar_info(f"Producto actualizado: {id_producto}")
            return True

        raise ProductoError("Producto no encontrado.")

    def eliminar_producto(self, id_producto):
        producto = self.buscar_producto(id_producto)
        if producto:
            self.productos.remove(producto)
            self.guardar_datos()
            registrar_info(f"Producto eliminado: {id_producto}")
            return True

        raise ProductoError("Producto no encontrado.")

    def exportar_csv(self, archivo_csv="productos_exportados.csv"):
        with open(archivo_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Nombre", "Precio", "Cantidad"])
            for p in self.productos:
                writer.writerow([p.id_producto, p.nombre, p.precio, p.cantidad])

        registrar_info("Productos exportados a CSV")