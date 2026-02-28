import tkinter as tk
from tkinter import messagebox, ttk
from gestor import GestorProductos
from utils import configurar_logging


class AplicacionCRUD:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Productos")
        self.root.geometry("700x500")

        self.gestor = GestorProductos()

        self.crear_widgets()
        self.cargar_tabla()

    def crear_widgets(self):
        # ===== FRAME FORMULARIO =====
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5)
        self.entry_nombre = tk.Entry(frame_form)
        self.entry_nombre.grid(row=0, column=1, padx=5)

        tk.Label(frame_form, text="Precio:").grid(row=0, column=2, padx=5)
        self.entry_precio = tk.Entry(frame_form)
        self.entry_precio.grid(row=0, column=3, padx=5)

        tk.Label(frame_form, text="Cantidad:").grid(row=0, column=4, padx=5)
        self.entry_cantidad = tk.Entry(frame_form)
        self.entry_cantidad.grid(row=0, column=5, padx=5)

        # ===== BOTONES =====
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar", command=self.agregar_producto).grid(row=0, column=0, padx=10)
        tk.Button(frame_botones, text="Actualizar", command=self.actualizar_producto).grid(row=0, column=1, padx=10)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_producto).grid(row=0, column=2, padx=10)
        tk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos).grid(row=0, column=3, padx=10)

        # ===== TABLA =====
        self.tabla = ttk.Treeview(self.root, columns=("ID", "Nombre", "Precio", "Cantidad"), show="headings")
        self.tabla.pack(pady=20, fill="both", expand=True)

        for col in ("ID", "Nombre", "Precio", "Cantidad"):
            self.tabla.heading(col, text=col)

        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_producto)

    def cargar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for producto in self.gestor.listar_productos():
            self.tabla.insert("", "end", values=(
                producto.id_producto,
                producto.nombre,
                producto.precio,
                producto.cantidad
            ))

    def agregar_producto(self):
        try:
            nombre = self.entry_nombre.get()
            precio = float(self.entry_precio.get())
            cantidad = int(self.entry_cantidad.get())

            if precio < 0 or cantidad < 0:
                messagebox.showerror("Error", "Precio y cantidad no pueden ser negativos.")
                return

            self.gestor.agregar_producto(nombre, precio, cantidad)
            self.cargar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Producto agregado correctamente.")

        except ValueError:
            messagebox.showerror("Error", "Datos inválidos.")

    def actualizar_producto(self):
        try:
            seleccionado = self.tabla.selection()
            if not seleccionado:
                messagebox.showerror("Error", "Seleccione un producto.")
                return

            id_producto = int(self.tabla.item(seleccionado)["values"][0])
            nombre = self.entry_nombre.get()
            precio = float(self.entry_precio.get())
            cantidad = int(self.entry_cantidad.get())

            if self.gestor.actualizar_producto(id_producto, nombre, precio, cantidad):
                self.cargar_tabla()
                self.limpiar_campos()
                messagebox.showinfo("Éxito", "Producto actualizado.")
            else:
                messagebox.showerror("Error", "No se pudo actualizar.")

        except ValueError:
            messagebox.showerror("Error", "Datos inválidos.")

    def eliminar_producto(self):
        seleccionado = self.tabla.selection()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione un producto.")
            return

        id_producto = int(self.tabla.item(seleccionado)["values"][0])

        confirmacion = messagebox.askyesno("Confirmar", "¿Desea eliminar el producto?")
        if confirmacion:
            self.gestor.eliminar_producto(id_producto)
            self.cargar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Producto eliminado.")

    def seleccionar_producto(self, event):
        seleccionado = self.tabla.selection()
        if seleccionado:
            valores = self.tabla.item(seleccionado)["values"]
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, valores[1])
            self.entry_precio.delete(0, tk.END)
            self.entry_precio.insert(0, valores[2])
            self.entry_cantidad.delete(0, tk.END)
            self.entry_cantidad.insert(0, valores[3])

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)



    
if __name__ == "__main__":
    configurar_logging()
    root = tk.Tk()
    app = AplicacionCRUD(root)
    root.mainloop()