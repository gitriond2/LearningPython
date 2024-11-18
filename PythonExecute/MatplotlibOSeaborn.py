import matplotlib.pyplot as plt
import seaborn as sns

# Conectar a la base de datos
conn = sqlite3.connect('indumentaria_intima.db')

# Consulta para obtener ventas por método de pago
ventas_metodo_pago = query_db('''
SELECT TIPODEPAGO, SUM(IMPORTE) as TotalVentas
FROM Ventas
GROUP BY TIPODEPAGO
''')

# Graficar los datos
plt.figure(figsize=(10, 6))
sns.barplot(x='TIPODEPAGO', y='TotalVentas', data=ventas_metodo_pago)
plt.title('Ventas por Método de Pago')
plt.xlabel('Método de Pago')
plt.ylabel('Total Ventas')
plt.show()

# Cerrar la conexión
conn.close()
