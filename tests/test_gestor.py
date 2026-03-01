import os
import pytest
from gestor import GestorProductos
from utils import ProductoError


ARCHIVO_TEST = "test_data.json"


@pytest.fixture
def gestor():
    # Crear gestor con archivo temporal
    gestor = GestorProductos(ARCHIVO_TEST)
    yield gestor

    # Limpiar archivo después del test
    if os.path.exists(ARCHIVO_TEST):
        os.remove(ARCHIVO_TEST)


def test_agregar_producto(gestor):
    producto = gestor.agregar_producto("Laptop", 2500.0, 5)
    assert producto.nombre == "Laptop"
    assert gestor.total_productos() == 1


def test_precio_negativo(gestor):
    with pytest.raises(ProductoError):
        gestor.agregar_producto("Mouse", -10, 5)


def test_cantidad_negativa(gestor):
    with pytest.raises(ProductoError):
        gestor.agregar_producto("Teclado", 50, -1)


def test_actualizar_producto(gestor):
    producto = gestor.agregar_producto("Monitor", 800, 3)
    gestor.actualizar_producto(producto.id_producto, "Monitor HD", 900, 4)

    actualizado = gestor.buscar_producto(producto.id_producto)
    assert actualizado.nombre == "Monitor HD"
    assert actualizado.precio == 900


def test_eliminar_producto(gestor):
    producto = gestor.agregar_producto("Impresora", 500, 2)
    gestor.eliminar_producto(producto.id_producto)
    assert gestor.total_productos() == 0


def test_valor_total_inventario(gestor):
    gestor.agregar_producto("A", 10, 2)  # 20
    gestor.agregar_producto("B", 5, 4)   # 20
    assert gestor.valor_total_inventario() == 40