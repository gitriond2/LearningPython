import sqlite3
import pandas as pd

# Conectar a la base de datos
conn = sqlite3.connect('indumentaria_intima.db')

# Crear un DataFrame para mostrar los resultados de las consultas
def query_db(query):
    return pd.read_sql_query(query, conn)

# Consulta para obtener todos los clientes
clientes = query_db('SELECT * FROM Clientes')
print(clientes)

# Consulta para obtener todos los productos
productos = query_db('SELECT * FROM Productos')
print(productos)

# Consulta para obtener todas las ventas
ventas = query_db('SELECT * FROM Ventas')
print(ventas)

# Cerrar la conexión
conn.close()
