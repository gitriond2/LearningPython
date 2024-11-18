import sqlite3

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect('indumentaria_intima.db')
cursor = conn.cursor()

# Crear tablas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes(
    CLIENTE_ID INT PRIMARY KEY,
    NOMBRE TEXT,
    APELLIDO TEXT,
    DIRECCION TEXT,
    LOCALIDAD TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Productos(
    PRODUCTO_ID INT PRIMARY KEY,
    NOMBRE TEXT,
    MARCA TEXT,
    IMPORTE REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Ventas(
    ID_VENTA INT,
    FECHA TEXT,
    CLIENTE INT,
    PRODUCTO INT,
    CANTIDAD INT,
    IMPORTE REAL,
    TIPODEPAGO TEXT,
    FOREIGN KEY (CLIENTE) REFERENCES Clientes(CLIENTE_ID),
    FOREIGN KEY (PRODUCTO) REFERENCES Productos(PRODUCTO_ID),
    PRIMARY KEY (ID_VENTA, PRODUCTO)
)
''')

# Insertar datos iniciales
cursor.executemany('''
INSERT INTO Clientes (CLIENTE_ID, NOMBRE, APELLIDO, DIRECCION, LOCALIDAD) VALUES (?, ?, ?, ?, ?)
''', [
    (1, 'Carlos', 'Gonzalez', 'Calle 1', 'Madrid'),
    # Añadir los demás registros aquí...
])

cursor.executemany('''
INSERT INTO Productos (PRODUCTO_ID, NOMBRE, MARCA, IMPORTE) VALUES (?, ?, ?, ?)
''', [
    (1, 'Sostén', 'Victoria s Secret', 49.99),
    # Añadir los demás registros aquí...
])

cursor.executemany('''
INSERT INTO Ventas (ID_VENTA, FECHA, CLIENTE, PRODUCTO, CANTIDAD, IMPORTE, TIPODEPAGO) VALUES (?, ?, ?, ?, ?, ?, ?)
''', [
    (1, '2024-01-01', 1, 1, 2, 99.98, 'Tarjeta'),
    # Añadir los demás registros aquí...
])

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()
