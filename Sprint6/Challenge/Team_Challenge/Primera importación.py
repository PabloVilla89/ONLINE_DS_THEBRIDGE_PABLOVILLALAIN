import sqlite3

# Conectar a la base de datos
connection = sqlite3.connect("ProveedoresV2.db")
cursor_gestion = connection.cursor()

# Función para eliminar registros existentes
def limpiar_tabla(nombre_tabla):
    cursor_gestion.execute(f"DELETE FROM {nombre_tabla}")
    connection.commit()
    print(f"Datos eliminados de la tabla {nombre_tabla}.")

# Función para insertar datos de ejemplo
def insertar_datos():
    # Limpiar las tablas
    limpiar_tabla("Proveedores")
    limpiar_tabla("Categorias")
    limpiar_tabla("Piezas")
    limpiar_tabla("Suministros")
    
    # Insertar datos de ejemplo en la tabla Proveedores
    datos_proveedores = [
        (1, 'Distribuciones Sureste', 'Calle Gran Vía, 28', 'Madrid', 'Madrid', 'COD001'),
        (2, 'Soluciones Industriales', 'Avenida de la Constitución, 10', 'Sevilla', 'Sevilla', 'COD002'),
        (3, 'AgroComponentes', 'Carrer de Balmes, 45', 'Barcelona', 'Barcelona', 'COD003'),
        (4, 'SuministrosAGRI', 'Calle Larios, 12', 'Málaga', 'Málaga', 'COD004'),
        (5, 'Distribuciones Murcia', 'Calle Mayor, 15', 'Murcia', 'Murcia', 'COD005')
    ]

    # Insertar datos de ejemplo en la tabla Categorías
    datos_categorias = [
        (1, 'Electrónica', 'CAT001'),
        (2, 'Mecánica', 'CAT002'),
        (3, 'Hidráulica', 'CAT003'),
        (4, 'Neumática', 'CAT004'),
        (5, 'Eléctrica', 'CAT005')
    ]

    # Insertar datos de ejemplo en la tabla Piezas
    datos_piezas = [
        (1, 'Rodamiento', 'Rojo', 0.10, 1),
        (2, 'Tornillo', 'Plateado', 0.05, 2),
        (3, 'Tubo led', 'Negro', 120.00, 3),
        (4, 'Actuador Neumático', 'Amarillo', 85.30, 4),
        (5, 'Reactancia', 'Negro', 50.99, 5)
    ]

    # Insertar datos de ejemplo en la tabla Suministros
    datos_suministros = [
        (1, 1, 1, 1000, '2024-12-01'),
        (2, 2, 2, 500, '2024-12-02'),
        (3, 3, 3, 75, '2024-12-03'),
        (4, 4, 4, 150, '2024-12-04'),
        (5, 5, 5, 200, '2024-12-05')
    ]
    
    # Insertar los datos en las tablas respectivas
    cursor_gestion.executemany("INSERT INTO Proveedores VALUES (?, ?, ?, ?, ?, ?)", datos_proveedores)
    cursor_gestion.executemany("INSERT INTO Categorias VALUES (?, ?, ?)", datos_categorias)
    cursor_gestion.executemany("INSERT INTO Piezas VALUES (?, ?, ?, ?, ?)", datos_piezas)
    cursor_gestion.executemany("INSERT INTO Suministros VALUES (?, ?, ?, ?, ?)", datos_suministros)
    connection.commit()
    print("Datos insertados correctamente.")

# Ejecutar la función para insertar datos
insertar_datos()

# Cerrar la conexión
connection.close()
