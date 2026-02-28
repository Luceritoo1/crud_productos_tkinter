from gestor import GestorProductos


def mostrar_menu():
    print("\n===== SISTEMA DE GESTIÓN DE PRODUCTOS =====")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")


def main():
    gestor = GestorProductos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                producto = gestor.agregar_producto(nombre, precio, cantidad)
                print(f"Producto agregado con ID {producto.id_producto}")
            except ValueError:
                print("Error: precio debe ser número y cantidad debe ser entero.")

        elif opcion == "2":
            productos = gestor.listar_productos()
            if not productos:
                print("No hay productos registrados.")
            else:
                for p in productos:
                    print(f"ID: {p.id_producto} | Nombre: {p.nombre} | Precio: {p.precio} | Cantidad: {p.cantidad}")

        elif opcion == "3":
            try:
                id_producto = int(input("Ingrese ID del producto: "))
                producto = gestor.buscar_producto(id_producto)
                if producto:
                    print(f"ID: {producto.id_producto}")
                    print(f"Nombre: {producto.nombre}")
                    print(f"Precio: {producto.precio}")
                    print(f"Cantidad: {producto.cantidad}")
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "4":
            try:
                id_producto = int(input("Ingrese ID del producto a actualizar: "))
                nombre = input("Nuevo nombre: ")
                precio = float(input("Nuevo precio: "))
                cantidad = int(input("Nueva cantidad: "))

                if gestor.actualizar_producto(id_producto, nombre, precio, cantidad):
                    print("Producto actualizado correctamente.")
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("Datos inválidos.")

        elif opcion == "5":
            try:
                id_producto = int(input("Ingrese ID del producto a eliminar: "))
                if gestor.eliminar_producto(id_producto):
                    print("Producto eliminado correctamente.")
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()