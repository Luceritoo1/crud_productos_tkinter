import tkinter as tk
from tkinter import messagebox
from gestor import GestorProductos
from utils import ProductoError, configurar_logging


class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Profesional de Inventario")
        self.root.geometry("750x600")

        configurar_logging()
        self.gestor = GestorProductos()

        self.crear_widgets()
        self.refrescar_lista()

    # -------------------------------------------------
    # INTERFAZ
    # -------------------------------------------------

    def crear_widgets(self):

        # FRAME SUPERIOR
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Nombre").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(frame_form)
        self.entry_nombre.grid(row=0, column=1)

        tk.Label(frame_form, text="Precio").grid(row=1, column=0)
        self.entry_precio = tk.Entry(frame_form)
        self.entry_precio.grid(row=1, column=1)

        tk.Label(frame_form, text="Cantidad").grid(row=2, column=0)
        self.entry_cantidad = tk.Entry(frame_form)
        self.entry_cantidad.grid(row=2, column=1)

        # BOTONES
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar", command=self.agregar_producto, bg="green", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Actualizar", command=self.actualizar_producto, bg="orange", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_producto, bg="red", fg="white").grid(row=0, column=2, padx=5)
        tk.Button(frame_botones, text="Exportar CSV", command=self.exportar_csv, bg="blue", fg="white").grid(row=0, column=3, padx=5)
        tk.Button(frame_botones, text="Ver Estadísticas", command=self.mostrar_estadisticas, bg="purple", fg="white").grid(row=0, column=4, padx=5)

        # BUSCADOR
        tk.Label(self.root, text="Buscar Producto").pack()
        self.entry_buscar = tk.Entry(self.root)
        self.entry_buscar.pack()
        self.entry_buscar.bind("<KeyRelease>", self.buscar_en_tiempo_real)

        # LISTA
        self.lista = tk.Listbox(self.root, width=90, height=15)
        self.lista.pack(pady=10)

        # BARRA DE ESTADO
        self.status = tk.Label(self.root, text="Sistema listo", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    # -------------------------------------------------
    # CRUD
    # -------------------------------------------------

    def agregar_producto(self):
        try:
            nombre = self.entry_nombre.get().strip()
            precio = float(self.entry_precio.get())
            cantidad = int(self.entry_cantidad.get())

            self.gestor.agregar_producto(nombre, precio, cantidad)

            messagebox.showinfo("Éxito", "Producto agregado correctamente")
            self.status.config(text="Producto agregado")

            self.limpiar_campos()
            self.refrescar_lista()

        except ProductoError as e:
            messagebox.showerror("Error", str(e))
        except ValueError:
            messagebox.showerror("Error", "Precio debe ser número y cantidad entero.")

    def actualizar_producto(self):
        try:
            seleccion = self.lista.curselection()
            if not seleccion:
                messagebox.showerror("Error", "Seleccione un producto")
                return

            indice = seleccion[0]
            producto = self.gestor.listar_productos()[indice]

            nombre = self.entry_nombre.get().strip()
            precio = float(self.entry_precio.get())
            cantidad = int(self.entry_cantidad.get())

            self.gestor.actualizar_producto(producto.id_producto, nombre, precio, cantidad)

            messagebox.showinfo("Éxito", "Producto actualizado")
            self.status.config(text="Producto actualizado")

            self.limpiar_campos()
            self.refrescar_lista()

        except ProductoError as e:
            messagebox.showerror("Error", str(e))
        except ValueError:
            messagebox.showerror("Error", "Precio debe ser número y cantidad entero.")

    def eliminar_producto(self):
        try:
            seleccion = self.lista.curselection()
            if not seleccion:
                messagebox.showerror("Error", "Seleccione un producto")
                return

            indice = seleccion[0]
            producto = self.gestor.listar_productos()[indice]

            self.gestor.eliminar_producto(producto.id_producto)

            messagebox.showinfo("Éxito", "Producto eliminado")
            self.status.config(text="Producto eliminado")

            self.refrescar_lista()

        except ProductoError as e:
            messagebox.showerror("Error", str(e))

    # -------------------------------------------------
    # EXPORTAR CSV
    # -------------------------------------------------

    def exportar_csv(self):
        try:
            self.gestor.exportar_csv()
            messagebox.showinfo("Éxito", "Productos exportados a productos_exportados.csv")
            self.status.config(text="CSV exportado correctamente")
        except ProductoError as e:
            messagebox.showerror("Error", str(e))

    # -------------------------------------------------
    # BUSCADOR
    # -------------------------------------------------

    def buscar_en_tiempo_real(self, event):
        texto = self.entry_buscar.get().lower()
        self.lista.delete(0, tk.END)

        for p in self.gestor.listar_productos():
            if texto in p.nombre.lower():
                self.lista.insert(tk.END,
                    f"ID:{p.id_producto} | {p.nombre} | S/.{p.precio} | Cantidad:{p.cantidad}"
                )

    # -------------------------------------------------
    # ESTADÍSTICAS
    # -------------------------------------------------

    def mostrar_estadisticas(self):
        total = self.gestor.total_productos()
        valor_total = self.gestor.valor_total_inventario()

        messagebox.showinfo(
            "Estadísticas",
            f"Total de productos: {total}\nValor total del inventario: S/. {valor_total}"
        )

    # -------------------------------------------------
    # UTILIDADES
    # -------------------------------------------------

    def refrescar_lista(self):
        self.lista.delete(0, tk.END)
        for p in self.gestor.listar_productos():
            self.lista.insert(
                tk.END,
                f"ID:{p.id_producto} | {p.nombre} | S/.{p.precio} | Cantidad:{p.cantidad}"
            )

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)


# -------------------------------------------------
# EJECUCIÓN
# -------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()