📦 Sistema Profesional de Inventario con Tkinter
📌 Descripción

Aplicación de escritorio desarrollada en Python utilizando Tkinter que permite gestionar un inventario de productos con funcionalidades CRUD completas, validaciones profesionales, exportación a CSV y pruebas automatizadas.

El sistema implementa buenas prácticas como:

Arquitectura modular

Manejo de excepciones personalizadas

Persistencia en JSON

Logging

Exportación de datos

Tests automatizados con pytest

🏗️ Arquitectura del Proyecto
crud_productos_pro/
│
├── main.py              # Interfaz gráfica (Tkinter)
├── gestor.py            # Lógica de negocio
├── modelo.py            # Clase Producto
├── utils.py             # Logging y excepciones
├── data.json            # Base de datos JSON
├── pytest.ini           # Configuración pytest
│
└── tests/
    └── test_gestor.py   # Pruebas automatizadas
🚀 Funcionalidades
✅ CRUD Completo

Agregar productos

Actualizar productos

Eliminar productos

Listar productos

✅ Validaciones Profesionales

Nombre vacío no permitido

Precio negativo no permitido

Cantidad negativa no permitida

✅ Buscador en Tiempo Real

Filtra productos automáticamente mientras escribes.

✅ Exportación a CSV

Genera archivo:

productos_exportados.csv
✅ Estadísticas

Total de productos

Valor total del inventario

✅ Logging

Se genera archivo:

sistema.log
✅ Tests Automatizados

Pruebas con pytest para validar:

Agregar producto

Validaciones

Actualización

Eliminación

Cálculo de inventario

🧪 Ejecutar Tests

Instalar pytest:

pip install pytest

Ejecutar:

pytest

Salida esperada:

6 passed
▶ Ejecutar la Aplicación

Desde la raíz del proyecto:

python main.py
🛠 Tecnologías Utilizadas

Python 3.x

Tkinter

JSON

CSV

Pytest

📊 Capturas que debes incluir en tu informe

Interfaz principal

Producto agregado

Validación de error

Exportación CSV

Ventana de estadísticas

Resultado de pytest

🎓 Conceptos Aplicados

Programación Orientada a Objetos

Arquitectura en capas

Manejo de excepciones

Persistencia de datos

Testing automatizado

Buenas prácticas de desarrollo

👨‍💻 Autor

Proyecto desarrollado como sistema profesional de gestión de inventario en Python.

🔥 AHORA SIGUIENTE NIVEL

Vamos a dejarlo aún más profesional:

📦 Convertirlo en ejecutable (.exe)

Instala:

pip install pyinstaller

Luego ejecuta:

pyinstaller --onefile --windowed main.py

Se creará carpeta:

dist/

Y dentro estará:

main.exe